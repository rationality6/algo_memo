interface IDuck {
    name: string
    quack(): void
}

class MallarDuck implements IDuck {
    name: "mallarduck"
    age: 3
    quack() {
        console.log('Quack!')
    }
}

class RedheadDuck {
    quack() {
        console.log('q~uack!')
    }
}

function makeNoise(duck: IDuck): void {
    duck.quack()
}

makeNoise(new MallarDuck())
makeNoise(new RedheadDuck())
