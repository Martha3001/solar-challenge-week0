def get_numeric_columns(df, exclude=None):
    """
    Get numeric columns from DataFrame
    Args:
        df: DataFrame to analyze
        exclude: Columns to exclude
    Returns:
        List of numeric column names
    """
    exclude = exclude or []
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    return [col for col in numeric_cols if col not in exclude]