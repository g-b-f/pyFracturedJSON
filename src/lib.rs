use pyo3::prelude::*;
use fracturedjson::{Formatter, NumberListAlignment};

#[pyfunction]
fn reformat_string(
    input: String,
    indent:usize,
    line_length: usize,
    max_inline_complexity: isize,
    max_compact_array_complexity: isize,
    max_table_row_complexity: isize,
    number_list_alignment: &str
) -> String {
    let mut formatter = Formatter::new();
    formatter.options.max_total_line_length = line_length;
    formatter.options.indent_spaces = indent;
    formatter.options.max_inline_complexity = max_inline_complexity;
    formatter.options.max_compact_array_complexity = max_compact_array_complexity;
    formatter.options.max_table_row_complexity = max_table_row_complexity;

    match number_list_alignment {
        "left" => formatter.options.number_list_alignment = NumberListAlignment::Left,
        "right" => formatter.options.number_list_alignment = NumberListAlignment::Right,
        "decimal" => formatter.options.number_list_alignment = NumberListAlignment::Decimal,
        "normalize" => formatter.options.number_list_alignment = NumberListAlignment::Normalize,
        _ => formatter.options.number_list_alignment = NumberListAlignment::Decimal
    }

    let formatted = formatter.reformat(&input, 0);
    let output = formatted.expect("Unexpected output");
    return output
}

#[pymodule]
fn _rust_wrapper(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(reformat_string, m)?)?;
    Ok(())
}