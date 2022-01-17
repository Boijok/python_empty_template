import pytest
from _pytest.capture import CaptureFixture
from dstar_local_data_repo.main import print_text


@pytest.mark.parametrize(
    "text_to_print, expected_output",
    [
        (
            "a_text_to_print",
            "a_text_to_print\n",
        ),
        (
            "another_text_to_print",
            "another_text_to_print\n",
        ),
    ],
)
def test_print_text(
    capfd: CaptureFixture[str], text_to_print: str, expected_output: str
) -> None:
    # Given

    # When
    print_text(text_to_print)

    # Then
    out, err = capfd.readouterr()
    assert out == expected_output
