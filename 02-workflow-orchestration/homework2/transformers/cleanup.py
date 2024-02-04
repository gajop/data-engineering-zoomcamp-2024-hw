if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    print(data["VendorID"].unique())

    data = data[(data["passenger_count"] > 0) & (data["trip_distance"] > 0)]
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date
    print(data.columns)
    columns_original = data.columns
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )
    print('Columns changed:', sum([1 for i in range(len(columns_original)) if columns_original[i] != data.columns[i]]))

    print(data["vendor_id"].unique())

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert "vendor_id" in output.columns
    assert len(output[output["passenger_count"] == 0]) == 0
    assert len(output[output["trip_distance"] == 0]) == 0
    assert output is not None, 'The output is undefined'
