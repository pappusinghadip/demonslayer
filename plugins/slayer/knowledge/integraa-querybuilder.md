# IntegraaNetwork Query Builder

Apply ONLY when the repo has `gestione/class/class.sql.php` and
`gestione/class/class.base.php` (the `SQLManager` + `Base` framework). Skip on
Laravel/Symfony/PDO projects — this is a custom wpdb-style layer, not an ORM.

**Rule: query through the model builder, not raw SQL.** In this codebase the
model layer is used ~10x more than `SQL()` (≈6800 `->get()` / 1100 `->save()`
vs ≈340 `SQL()->query()`). Match that. Never concatenate a value into SQL.

## Model layer — the default. Use this.

Every table has a `Base` subclass reached through a global accessor:
`Entity()`, `Agency()`, `Invoice()`, `Status()`, `Meta()`, … Pass a filter
array; the model builds and escapes the SQL. A plain `key => value` is `WHERE
key = value`.

```php
// SELECT
$rows = Agency()->get([
    'select'  => ['tipologia', 'carrier_id'],  // string or array; omit = all fields
    'typology'=> 'VE',                           // WHERE typology = 'VE'  (escaped)
    'orderby' => ['process_id' => 'ASC'],        // string | ['col'=>'ASC'|'DESC'] | false
    'limit'   => 50,
])->items();

$id = Carrier()->get(['select' => 'carrier_id', 'external' => 1])->int('carrier_id');
$one = ApiRequest()->get(['select' => ['date_insert'], 'ID' => $id])->item();
```

### WHERE operators — `field => ['op' => value]`

Bare value = equals. For anything else, wrap in an op array (both `['in'=>…]`
and `array('in'=>…)` are fine). By real frequency:

| Op | Meaning | Example |
|---|---|---|
| `in` | IN (list) | `'status' => ['in' => [1,2,3]]` |
| `neq` | `!=` | `'external' => ['neq' => 1]` |
| `gte` / `lte` | `>=` / `<=` | `'date' => ['gte' => $from]` |
| `gt` / `lt` | `>` / `<` | `'qty' => ['gt' => 0]` |
| `like` | LIKE `%v%` | `'name' => ['like' => $term]` |
| `notnull` | IS NOT NULL | `'closed_at' => ['notnull' => 1]` |

OR / grouped conditions use `logics` (array of condition-arrays) + `logic`:
```php
Flow()->get([
    'logic'  => 'OR',
    'logics' => [['to_retrieve_status' => '0'], ['to_retrieve_status' => '2']],
]);
```
Other keys seen in real use: `group`, `having`, `join`, `nested`,
`allow_archived => 1` (include soft-deleted), `cache => 1`,
`get_col => 'field'` (return one column as array), `get_var` (one scalar),
`row_index => 'field'` (key rows by a column).

### Reading results

`->items()` all, `->item()` first, `->found_rows()` total match count. Field
extractors off a single-row result take a field name or column index (default =
first column): `->val($f)`, `->get($f, $default)`, `->int($f)`, `->float($f)`,
`->str($f)`, `->bool($f)`, `->has($f)` (exists?). Note: `->value()` takes NO
argument (internal scalar slot) — it is not a field getter; use `->val($f)`.

### Writing — `save()` and `delete()`

`save()` INSERTs with no id, UPDATEs when `ID` (or `where`) is present. Never
hand-write INSERT/UPDATE for a table that has a model.

```php
$new = Employee()->save(['livello' => 'C', 'name' => $n]);   // INSERT → $new->ID
Employee()->save(['ID' => $id, 'livello' => 'E']);            // UPDATE by id
Meta()->save(['status' => 'closed', 'where' => ['batch' => $b]]); // UPDATE by filter

AsyncStatus()->delete(['id' => $id]);
Meta()->delete(['where' => ['table_id' => $rid, 'meta_key' => 'container']]);
```

Soft-delete (`archived`) is automatic on both read and delete; pass
`allow_archived => 1` to bypass.

## `SQL()` helpers — only without a model

Use for stored procedures, bulk/reporting SQL, or tables with no `Base`
subclass. `SQL()` is the global `SQLManager`. Pass assoc arrays, not strings:

```php
SQL()->insert($table, ['col' => $val]);                 // insert_ignore(), replace()
SQL()->update($table, ['col' => $val], ['ID' => $id]);  // data, then WHERE array
SQL()->delete($table, ['ID' => $id]);
SQL()->insert_id;  SQL()->rows_affected;

SQL()->get_results($sql);   // rows; ARRAY_A for assoc. get_row/get_var/get_col too
```

## Unavoidable raw SQL — always `prepare()`

Only when it can't be expressed above (complex JOIN reports, subqueries). Build
with placeholders; never inline a variable.

```php
$sql = SQL()->prepare(
    "SELECT * FROM ordini WHERE distinta_id = %d AND code = %s",
    [$distinta_id, $code]
);
SQL()->get_results($sql);
```
`%d` int · `%f` float · `%s` string (quoted+escaped) · `%r` raw (identifiers/SQL
fragments ONLY — never a user value).

## Anti-patterns — never write these

```php
SQL()->get_results("SELECT * FROM ordini WHERE id = " . $id);    // concatenation
SQL()->query("UPDATE ordini SET status='$status' WHERE id=$id");  // interpolation
```
Rewrite as `Ordini()->get(['ID' => $id])` / `Ordini()->save(['ID' => $id,
'status' => $status])`, or `SQL()->get_results(SQL()->prepare(...))` if there is
genuinely no model.
