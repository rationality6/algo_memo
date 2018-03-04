class Animal {
  public name: string;
  public constructor(theName: string) {
    this.name = theName
  }
  public move(distanceInMeters: number): Number {
    console.log(`${this.name} moved ${distanceInMeters}m.`)
    return 3
  }
}

const cat = new Animal('hume')
console.log(cat.move(3))
