import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})

export class ProductListComponent {

  products = [...products];

  share(link:string|URL|undefined) {
    window.open("https://t.me/+rO6kV466qV1jMDE6" + link,'menubar=off, toolbar=off');
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}