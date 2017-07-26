export class Locationhistory {
	constructor(
    public name: string,
    public locations: string,
    // Will have to see how we get the images, store as hash? or url to image?
    public _id?: string,
  ) { }
}
