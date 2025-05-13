from test.integration.webapp import base_url
import requests
import re

def test_landing(base_url):
    response = requests.get(f"{base_url}/")
    html = response.text
    
    assert response.status_code == 200
    
    match = re.search(r"Hello World! I have been seen (\d+) times\.", html)
    assert match is not None, "No se encontró el patrón del contador en la respuesta"
    
    initial_count = int(match.group(1))
    
    response = requests.get(f"{base_url}/")
    html = response.text
    
    assert response.status_code == 200
    
    expected_text = f"Hello World! I have been seen {initial_count + 1} times."
    assert expected_text in html, f"El contador no se incrementó correctamente. Esperado: '{expected_text}', Actual: '{html}'"
