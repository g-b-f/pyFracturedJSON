use pyo3::prelude::*;
use fracturedjson::Formatter;

#[pyfunction]
fn reformat_string(input: String) -> String {
    let mut formatter = Formatter::new();
    let formatted = formatter.reformat(&input, 0);
    let output = formatted.expect("Unexpected output");
    return output
}

#[pymodule]
fn fractured_json_rust_wrapper(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(reformat_string, m)?)?;
    Ok(())
}