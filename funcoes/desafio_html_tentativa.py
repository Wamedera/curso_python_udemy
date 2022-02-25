# retorno esperado:
# <p class="alert"><span>Curso de Python 3, por </span><strong id="jf">Juracy Filho</strong><span> e </span><strong id="ll">Leonardo Leitão</strong><span>.</span></p>

def filtrar_atrs(atrs):
    return ''.join(f' {key.split("_")[-1]}="{value}"' for key, value in atrs.items())


def tag(tag, *args, **kwargs):
    html = ''.join((args if not callable(args) else args()))

    return f'<{tag}{filtrar_atrs(kwargs)}>{html}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
        tag('span', 'Curso de Python 3, por '),
        tag('strong', 'Juracy Filho', id='jf'),
        tag('span', ' e '),
        tag('strong', 'Leonardo Leitão', id='ll'),
        tag('span', '.'),
        html_class='alert')
    )
    