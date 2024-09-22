from script import main

def test_main(capsys):
    # Run the main function
    main()
    captured = capsys.readouterr()
    
    # Expected outputs
    assert "Descriptive Statistics for 'mean radius':" in captured.out
    assert "Mean: 14.127" in captured.out
    assert "Median: 13.37" in captured.out
    assert "Standard Deviation: 3.524" in captured.out
