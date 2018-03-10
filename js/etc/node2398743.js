class Node {
  constructor(data, left = null, right = null) {
    this.data = data
    this.left = left
    this.right = right
  }
}

const create_leafs = () => {
  const leafs = []
  for (let i = 4; i < 8; i += 1) {
    leafs.push(new Node(i))
  }
  return leafs
}

const leafs = create_leafs()

const left = new Node(2, leafs[0], leafs[1])
const right = new Node(3, leafs[2], leafs[3])
const root_node = new Node(1, left, right)

const preorder_traverse = node => {
  if (node === null) {
    return;
  }
  console.log(node.data);
  preorder_traverse(node.left)
  preorder_traverse(node.right)
}

const inorder_traverse = node => {
  if (node === null) {
    return;
  }
  preorder_traverse(node.left)
  console.log(node.data);
  preorder_traverse(node.right)
}

const postorder_traverse = node => {
  if (node === null) {
    return;
  }
  preorder_traverse(node.left)
  preorder_traverse(node.right)
  console.log(node.data);
}

// preorder_traverse(root_node)
// inorder_traverse(root_node)
// postorder_traverse(root_node)

const find_min = (node) => {
  if (node === null) {
    return;
  }
  console.log(node.data);
  find_min(node.left)
}

const find_max = (node) => {
  if (node === null) {
    return;
  }
  console.log(node.data);
  find_max(node.right)
}

// find_min(root_node)
// find_max(root_node)
