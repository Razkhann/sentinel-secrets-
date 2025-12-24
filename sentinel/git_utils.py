import subprocess


def get_staged_diff() -> str:
    """
    Returns git diff of staged files.
    Used for pre-commit hook scanning.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git diff failed: {e.stderr}")
