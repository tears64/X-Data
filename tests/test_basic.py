from xdata.modules.email import run

def test_email_normalization():
    result = run("Test@Example.COM")
    assert result["email"] == "test@example.com"
    assert result["valid_format"] is True
    assert result["domain"] == "example.com"
