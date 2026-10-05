from pathlib import Path

from mkdocs.config.defaults import MkDocsConfig


ROOT = Path(__file__).resolve().parent


def _copy_if_changed(source: Path, destination: Path) -> None:
    content = source.read_bytes()
    if not destination.exists() or destination.read_bytes() != content:
        destination.write_bytes(content)


def on_pre_build(config: MkDocsConfig) -> None:
    docs = Path(config.docs_dir)
    _copy_if_changed(ROOT / "README.md", docs / "index.md")
    _copy_if_changed(
        ROOT / "Research-project-plan.md", docs / "Research-project-plan.md"
    )

    source_pages = {page.name: page for page in (ROOT / "guide").glob("*.md")}
    if not source_pages:
        raise RuntimeError("No research guide pages found")

    staged_guide = docs / "guide"
    staged_guide.mkdir(exist_ok=True)
    for page in staged_guide.glob("*.md"):
        if page.name not in source_pages:
            page.unlink()
    for name, page in sorted(source_pages.items()):
        _copy_if_changed(page, staged_guide / name)
