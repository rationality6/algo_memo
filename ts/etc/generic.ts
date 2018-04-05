class Queue<T>{
    protected data = [];
    push(item: T) {
        this.data.push(item)
    }
    pop(): T {
        return this.data.shift()
    }
}

const numberQueue = new Queue<number>();

// numberQueue.push(0)
// numberQueue.push(+'1')
// numberQueue.push(+'1')
// numberQueue.push(+'1')

// console.log(numberQueue)

// console.log(numberQueue.pop())
// console.log(numberQueue.pop())
// console.log(numberQueue.pop())
// console.log(numberQueue.pop())

// console.log(numberQueue)

const stringQueue = new Queue<string>();

stringQueue.push('hello');
stringQueue.push('world');
console.log(stringQueue)

console.log(stringQueue.pop().toUpperCase());
console.log(stringQueue.pop().toUpperCase());

const myQueue = new Queue<{ name: string, age: number }>();

myQueue.push({ name: 'Lee', age: 10 });
// myQueue.push({ name: 'foo' })

console.log(myQueue)


function reverse<T>(items: T[]): T[] {
    return items.reverse()
}

const arg = [{ name: 'Lee' }, { name: 'Kim' }, { name: 'Park' }]

const reversed = reverse(arg)
console.log(reversed)

reversed.push({name:33})
