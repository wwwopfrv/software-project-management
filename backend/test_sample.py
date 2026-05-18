import pytest

def test_example():
    """Простой тест для демонстрации CI/CD"""
    assert 1 + 1 == 2

def test_project_structure():
    """Проверка, что проект имеет нужные папки"""
    import os
    folders = ['backend', 'frontend', 'docs']
    for folder in folders:
        assert os.path.exists(folder), f"Папка {folder} не найдена"