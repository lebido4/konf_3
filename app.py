import toml
import sys
import re

# Функция для обработки словарей
def process_dict(value):
    output = ["{"]
    for key, v in value.items():
        output.append(f"  {key} : {parse_value(v)},")
    output.append("}")
    return "\n".join(output)

# Функция для обработки значений
def parse_value(value):
    # Проверка для константных выражений вида "$+ x y$"
    if isinstance(value, str) and re.match(r"\$[+\-*] .* \$", value):
        return value  # Пропускаем выражение как строку, без преобразования
    
    # Обычные случаи
    if isinstance(value, dict):
        return process_dict(value)
    elif isinstance(value, str):
        return f'[[{value}]]'
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return f"Error: Unsupported value type: {type(value)}"

# Функция для обработки данных из TOML файла
def parse_toml_to_config(toml_content):
    output = []
    
    for key, value in toml_content.items():
        if isinstance(value, dict):
            output.append(f"{key} is {process_dict(value)}")
        else:
            output.append(f"{key} is {parse_value(value)}")

    return "\n".join(output)

def main():
    if len(sys.argv) < 3:
        print("Usage: python config_tool.py input_file output_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Чтение входного файла в формате TOML
    try:
        with open(input_file, 'r') as f:
            toml_content = toml.load(f)
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        sys.exit(1)
    
    # Преобразование контента в нужный формат
    config_content = parse_toml_to_config(toml_content)
    
    # Запись в выходной файл
    with open(output_file, 'w') as f:
        f.write(config_content)

if __name__ == "__main__":
    main()
