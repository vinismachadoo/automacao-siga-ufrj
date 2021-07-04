import time, io
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def create_menu():

    menu = {
        1: 'Regularmente Matriculado',
        2: 'Passe Livre Universitário',
        3: 'Historico',
        4: 'Boletim',
        5: 'BOA',
        6: 'CRID'
    }
    
    print('--------------------')
    print('        MENU        ')
    print('--------------------')
    for key in menu:
        print(f'{key}. {menu[key]}')
    print('7. Sair')

    return menu

def getDocumento_siga(usuario, senha, documento):

    menu = {
        'Regularmente Matriculado': {'j_id103:0:j_id104':'j_id103:0:j_id104'},
        'Passe Livre Universitário': {'j_id103:2:j_id104':'j_id103:2:j_id104'},
        'Historico': {'botaoHistorico':'botaoHistorico'},
        'Boletim': {'botaoBoletim':'botaoBoletim'},
        'BOA': {'j_id123': 'j_id123'},
        'CRID': {'j_id127': 'j_id127'} 
    }
    
    session = HTMLSession()
    
    headers_main = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
    }

    main_page = session.get('https://portal.ufrj.br/Portal/', headers=headers_main, stream=True)

    headers_auth = {
        'authority': 'portal.ufrj.br',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'documento',
        'Referer': 'https://portal.ufrj.br/Portal/',
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; JSESSIONID={session.cookies.get_dict()['JSESSIONID']}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utmc=263428936; __utma=263428936.1617855722.1610505084.1623806842.1623809568.8; __utmb=263428936.7.10.1623809568",
    }

    authorization = session.get('https://portal.ufrj.br/Portal/auth.seam', headers=headers_auth, allow_redirects=False)

    authorization2 = session.get(authorization.headers['Location'], headers=headers_auth)

    headers_login = {
        'authority': 'portal.ufrj.br',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://portal.ufrj.br',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'documento',
        'Referer': authorization.headers['Location'],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; JSESSIONID={session.cookies.get_dict()['JSESSIONID']}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utmc=263428936; __utma=263428936.1617855722.1610505084.1623806842.1623809568.8; __utmb=263428936.7.10.1623809568",
    }

    data_login = {
      'gnosys-login-form': 'gnosys-login-form',
      'inputUsername': usuario,
      'inputPassword': senha,
      'btnEntrar': 'Entrar',
      'javax.faces.ViewState': 'j_id1'
    }

    login = session.post('https://portal.ufrj.br/Portal/acesso', headers=headers_login, data=data_login, allow_redirects=False)
    
    headers_login['cookie'] += f"; {login.headers['Set-Cookie'].split(';')[0]}"

    login2 = session.get(login.headers['Location'], headers=headers_login)
    soup_login = BeautifulSoup(login2.text, 'html.parser')

    headers_docs = {
        'authority': 'portal.ufrj.br',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'documento',
        'Referer': login.headers['Location'],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"_fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utma=263428936.1617855722.1610505084.1623809568.1623888920.9; __utmc=263428936; {login.headers['Set-Cookie'].split(';')[0]}; __utmb=263428936.2.10.1623888920",
    }

    docs = session.get('https://portal.ufrj.br/Documentos', headers=headers_docs, allow_redirects=False)

    headers_docs2 = {
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'Referer': login.headers['Location'],
    }

    docs2 = session.get(docs.headers['Location'], headers=headers_docs2)

    headers_docs3 = {
        'authority': 'portal.ufrj.br',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'documento',
        'Referer': docs.headers['Location'],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utma=263428936.1617855722.1610505084.1623809568.1623888920.9; __utmc=263428936; {login.headers['Set-Cookie'].split(';')[0]}; __utmb=263428936.2.10.1623888920",
    }

    docs3 = session.get('https://portal.ufrj.br/Documentos/auth.seam', headers=headers_docs3, allow_redirects=False)

    headers_docs4 = {
        'authority': 'portal.ufrj.br',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'documento',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Referer': docs.headers['Location'],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; {docs3.headers['Set-Cookie'].split(';')[0]}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utma=263428936.1617855722.1610505084.1623809568.1623888920.9; __utmc=263428936; {login.headers['Set-Cookie'].split(';')[0]}; __utmb=263428936.2.10.1623888920",
    }

    docs4 = session.get(docs3.headers['Location'], headers=headers_docs4)
        
    headers_emit = {
        'authority': 'portal.ufrj.br',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://portal.ufrj.br',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'documento',
        'Referer': docs3.headers['Location'].split(';')[0] + '?' + docs3.headers['Location'].split('?')[1],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; {docs3.headers['Set-Cookie'].split(';')[0]}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utma=263428936.1617855722.1610505084.1623809568.1623888920.9; __utmc=263428936; {login.headers['Set-Cookie'].split(';')[0]}; fileDownload=true; __utmb=263428936.2.10.1623888920",
    }

    data_emit = {
        'gnosys-decor-vis-seletor-matricula-aluno': '0',
        'gnosys-decor-vis-seletor-matricula-form': 'gnosys-decor-vis-seletor-matricula-form',
        'autoScroll': '',
        'javax.faces.ViewState': 'j_id1',
        **menu[documento]
    }

    emit = session.post('https://portal.ufrj.br/Documentos/certidoes/emitir', headers=headers_emit, data=data_emit, allow_redirects=False)

    headers_emit2 = {
        'authority': 'portal.ufrj.br',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'documento',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'Referer': docs3.headers['Location'].split(';')[0] + '?' + docs3.headers['Location'].split('?')[1],
        'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': f"cookie-portal={session.cookies.get_dict()['cookie-portal']}; {docs3.headers['Set-Cookie'].split(';')[0]}; _fbp=fb.1.1615472306244.1890742625; __utmz=263428936.1618402335.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_4RHYVS74FT=GS1.1.1620952983.4.1.1620953013.0; _ga=GA1.2.1617855722.1610505084; __utma=263428936.1617855722.1610505084.1623809568.1623888920.9; __utmc=263428936; {emit.headers['Set-Cookie'].split(';')[0]}; fileDownload=true; __utmb=263428936.2.10.1623888920",
    }

    final_doc = session.get(emit.headers['Location'], headers=headers_emit2)
    
    strIO = io.BytesIO(final_doc.content)
    strIO.seek(0)
    strIO.name = f"{soup_login.find('div', {'class':'gnosys-login-nome'}).text} - {documento}.pdf"

    return strIO

if __name__ == '__main__':

    print('Bem vindo ao portal SIGA UFRJ\n')

    print('Por favor insira seu usuário')
    usuario = input()
    print('Por favor insira sua senha')
    senha = input()

    menu = create_menu()

    while True:    
        print('\nQual o número de sua solicitação?')
        documento = int(input())

        if documento > 0 and documento < 7:
            doc = getDocumento_siga(usuario, senha, menu[documento])
            open(doc.name, 'wb').write(doc.getvalue())
        elif documento == 7:
            print('\nTenha um bom dia!')
            break
        else:
            print('Solicitação não encontrada. Por favor tente novamente\n')
