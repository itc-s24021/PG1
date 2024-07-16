def show_args(*args):
    print('Positional arguments:', args)
    return args
show_args(1, 2, 3, 'da!')


def show_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)
    return kwargs
show_kwargs(pasta='ペンネ', drink='赤ワイン', main_dish='肉料理', n_customers=3)
