from click.testing import CliRunner
from helloclick import hello


    
def test_search():
  runner = CliRunner()
  result = runner.invoke(hello)
  assert result.exit_code == 0