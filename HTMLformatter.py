class HTMLGenerator:
    def __init__(self):
        self.html = ""

    def generate_header(self, size, text):
        if size in {"1", "2", "3", "4", "5", "6"}:
            self.html += f"<h{size}>{text}</h{size}>\n"
        else:
            # Default to h1 if size is not recognized
            self.html += f"<h1>{text}</h1>\n"

    def generate_text(self, text):
        formatted_text = text.replace("\\n", "<br>")
        self.html += f"<p>{formatted_text}</p>\n"

    def generate_code(self, language, code):
        code_lines = code.split("\\n")
        formatted_code = "\n".join(code_lines)
        self.html += f'<pre class="align-items-center"><code class="language-{language}">{formatted_code}</code></pre>\n'

    def generate_image(self, alt_text, image_url):
        self.html += f'<img src="{image_url}" alt="{alt_text}">\n'

    def process_file(self, input_file):
        with open(input_file, 'r') as f:
            lines = f.readlines()

        current_instruction = None
        current_input = ""

        for line in lines:
            parts = line.strip().split(":")
            if len(parts) == 2:
                instruction, content = parts[0].strip(), parts[1].strip()
                if current_instruction:
                    self.process_instruction_with_input(
                        current_instruction, current_input)
                current_instruction = instruction
                current_input = content
            else:
                current_input += line

        if current_instruction:
            self.process_instruction_with_input(
                current_instruction, current_input)

    def process_instruction_with_input(self, instruction, content):
        if content.startswith('"') and content.endswith('"'):
            content = content[1:-1].replace("\\n", "<br>")
        self.process_single_line_instruction(instruction, content)

    def process_single_line_instruction(self, instruction, content):
        content = content.strip()
        if instruction.startswith("Header"):
            parts = instruction.split(",")
            if len(parts) > 1:
                size = parts[1].strip()
                self.generate_header(size, content)
            else:
                # Default to h1 if size is not provided
                self.generate_header("1", content)
        elif instruction == "Text":
            self.generate_text(content)
        elif instruction.startswith("Code"):
            language = instruction.split(",")[1].strip()
            self.generate_code(language, content)
        elif instruction.startswith("Image"):
            parts = content.split(",")
            if len(parts) == 2:
                alt_text, image_url = parts[0].strip(), parts[1].strip()
                self.generate_image(alt_text, image_url)

    def generate_html(self):
        return self.html


if __name__ == "__main__":
    input_file = "input.mlm"  # Replace with your input file name

    if input_file.endswith(".mlm"):
        generator = HTMLGenerator()
        generator.process_file(input_file)
        output_html = generator.generate_html()

        with open("template.html", "r") as existing_file:
            existing_html = existing_file.read()

        start_marker = "<!-- Start of Content-->"
        end_marker = "<!-- End of Content-->"

        start_pos = existing_html.find(start_marker) + len(start_marker)
        end_pos = existing_html.find(end_marker)

        updated_html = (
            existing_html[:start_pos]
            + "\n"
            + output_html
            + "\n"
            + existing_html[end_pos:]
        )

        with open("updated_html.html", "w") as output_file:
            output_file.write(updated_html)

        print("Updated HTML has been saved to updated_html.html")
    else:
        print("Input file is not a '.mlm' file. No HTML will be generated.")
