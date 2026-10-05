"""Regenerate the English and Bulgarian profile pages."""
from portfolio.readme import generate


if __name__=='__main__':
    for path in generate():
        print(f'Generated {path.name}')
