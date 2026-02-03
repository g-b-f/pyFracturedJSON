#![allow(non_snake_case)]
use pyo3::prelude::*;
use fracturedjson::Formatter;

#[pyfunction]
fn reformat(input: String) -> String {
    let mut formatter = Formatter::new();
    let formatted = formatter.reformat(&input, 0);
    let output = formatted.expect("Unexpected output");
    return output

}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn pyFracturedJSON(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(reformat, m)?)?;

    Ok(())
}