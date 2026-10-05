"""Compatibility entrypoint for the deterministic portfolio generator."""
from portfolio.build import generate


def main() -> None:
    print(f'Generated {len(generate())} bilingual SVG assets')


if __name__=='__main__':
    main()
