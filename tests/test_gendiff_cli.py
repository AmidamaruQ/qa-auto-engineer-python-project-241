import subprocess
import sys


def test_cli_prints_diff(test_data_dir):
    first_file = test_data_dir / "file1.json"
    second_file = test_data_dir / "file2.json"
    expected = (test_data_dir / "expected_cli_output.txt").read_text().rstrip("\n") + "\n"

    completed = subprocess.run(
        [sys.executable, "-m",
         "gendiff.scripts.gendiff", first_file, second_file],
        capture_output=True,
        text=True,
        check=True,
    )

    assert completed.stdout == expected
