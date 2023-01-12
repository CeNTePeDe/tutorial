root = {'data': 'A', 'children': [{'data': 'B', 'children': [{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
    [{'data': 'E', 'children': [{'data': 'G', 'children': []}, {'data': 'H', 'children': []}]},
     {'data': 'F', 'children': []}]}]}


def inorderTraverse(node):
    if len(node['children']) >= 1:
        # RECURSIVE CASE
        inorderTraverse(node['children'][0])  # traverse the left child
    print(node['data'], end=' ')  # Access this node's data
    if len(node['children']) >= 2:
        # RECURSIVE CASE
        inorderTraverse(node['children'][1])
    return


def preorderTraverse(node):
    print(node['data'], end=' ')  # Access this node's data
    if len(node['children']) > 0:
        for child in node['children']:  # Traverse child nodes
            preorderTraverse(child)
    return


def postorderTraverse(node):
    for child in node['children']:
        postorderTraverse(child)  # Traverse child nodes
    print(node['data'], end=' ')  # Access this node's data
    # Base case
    return


if __name__ == '__main__':
    inorderTraverse(root)
    print('***********', end=' ')
    preorderTraverse(root)
    print('***********', end=' ')
    postorderTraverse(root)
