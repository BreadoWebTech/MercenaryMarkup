## MercenaryMarkup - HTML Generator for MercenaryLabs.net Articles
MercenaryMarkup is a  HTML generator designed to simplify the process of creating well-formatted articles for MercenaryLabs.net.  goodbye to the pain of manually formatting HTML content and get to work efficently with this html generator.

### Overview
Creating articles with complex HTML structures can be time-consuming and error-prone. My HTML generator aims to allowing you to focus on your article's content while automatically generating the necessary HTML structure.

### Features
Effortless Formatting: MercenaryMarkup handles the generation of intricate HTML structures, ensuring your articles look polished without the hassle of manual formatting.
Consistency: Maintain a consistent article style and layout across your article for ML!
Time-Saving: Spend less time dealing with HTML tags and formatting and more time creating compelling content.
Ease of Use: Even if you're not an HTML expert, MercenaryMarkup enables you to create professional-looking articles without extensive coding knowledge.
Getting Started
Install MercenaryMarkup: No installation required; simply follow the usage instructions below.

### Write Your Content: Focus on creating your article's content without worrying about HTML formatting.

Use MercenaryMarkup: Embed your article's content within MercenaryMarkup syntax to generate the necessary HTML structure. See usage instructions below.

Copy and Paste: Copy the generated HTML code and paste it into your MercenaryLabs.net article. It already generates a full modified Article HTML too, the only thing youd have to edit would be the Article name and creator!

Usage Instructions
You need: a file called input.mlm, which contains the "MercenaryLabs Markup", template.html ( the mercenarylabs article template, inlucded in this repo ), HTMLformatter.py ( the main program, that turns your mlm into the html document you need!)

if you are done, just run the python file! after generation it will tell you that it is done, and you can open the generated html file.

# MLM Syntax

## input.mlm already includes a simple example article about programming that you can generate!

Headers: Start a line with "Header, X:" where X is the header level (1 to 6). For example:

```
Header, 1: Hello there
Header, 2: Hello therrrree
Header, 3: Hello 
Header, 4: hi
Header, 5: ayy
Header, 6: lool
```
Images: Use "Image: Alt text here, image.jpg" to insert images, providing the alt text and image source. For example:

```
Image: Alt text here, image.jpg
```
Text: Use "Text: " followed by your content. Newlines within the quotes will be translated into <br> tags. For example:

```
Text: "Hey there\n
Newlines in between the quotes are taken as is into the html,\n
so there would be 2 br tags instead of a newline here."
````
Code: Use "Code, language: " followed by your code. For example:

```css
Code, python: print("hello world")
Code, python: "print('hello world')"
````
Example
Here's a simple example of how you can use MercenaryMarkup to format your article content:

```
Header, 1: Introduction to MercenaryMarkup
Text: "MercenaryMarkup is a revolutionary tool that simplifies the process of creating HTML content for MercenaryLabs.net articles."
Header, 2: Features
Text: "With MercenaryMarkup, you can quickly format headers, images, text, and code snippets without the need for complex HTML tags."
Code, python: print("Hello, MercenaryMarkup!")
Image: MercenaryMarkup in action, example.jpg
```

# there will be new features coming at somepoint, including table support!
