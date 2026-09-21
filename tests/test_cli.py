from synthetic_social_signal_nlp.cli import main


def test_cli_prints_educational_boundary_and_metrics(capsys) -> None:
    exit_code = main()

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Educational synthetic-fixture metrics only" in output
    assert "not diagnostic" in output
    assert "macro_f1=" in output
