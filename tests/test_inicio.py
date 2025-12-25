def test_google(page):
    # Paso 1: Ir a Google
    page.goto("https://www.google.com")
    
    # Paso 2: Verificar que el título es correcto
    assert "Google" in page.title()
    print("¡La prueba pasó! El navegador se abrió y navegó correctamente.")