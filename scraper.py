from playwright.sync_api import sync_playwright

def login():

    with sync_playwright() as p:
        email = 'allisson@professor.educacao.sp.gov.br' #input('Digite o e-mail da sua conta no LinkedIn: ')
        senha = 'linkedinsenha' #input('Digite a senha da sua conta do LinkedIn: ')
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://www.linkedin.com/login')
        page.fill('input#username', email)
        page.fill('input#password', senha)
        page.click('.btn__primary--large.from__button--floating')

        try:
        # Espera até que o campo de busca do LinkedIn esteja presente na página
            page.wait_for_selector('.search-global-typeahead__input', timeout=30000)
            print("Login bem-sucedido!")

        except Exception as e:
            print(f"Falha no login ou elemento não encontrado: {e}")

        input('Pressione ENTER para fechar o navegador...')
        browser.close()

login()