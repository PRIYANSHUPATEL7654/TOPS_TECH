examples = [
    ('My order arrived 50 minutes late.', 'Late Delivery'),
    ('I received noodles instead of pizza.', 'Wrong Item'),
    ('The fries listed on my order were not in the bag.', 'Missing Item'),
    ('The food was cold and tasted stale.', 'Poor Quality'),
]
def add_example(text, label): examples.append((text, label))
def build_few_shot_prompt(complaint_text):
    lines = ['Classify the complaint into exactly one label: Late Delivery, Wrong Item, Missing Item, Poor Quality.', '']
    for text, label in examples: lines += [f'Input: {text}', f'Output: {label}', '']
    lines += [f'Input: {complaint_text}', 'Output:']
    return '\n'.join(lines)
if __name__ == '__main__':
    for complaint in ['My drink was missing.', 'The delivery took two hours.']:
        print(build_few_shot_prompt(complaint), '\n---')
    add_example('The restaurant sent a different curry.', 'Wrong Item')
    print('New example included:', 'The restaurant sent a different curry.' in build_few_shot_prompt('Test complaint'))
