import {Component, Input, OnInit} from '@angular/core';
import {Product, products} from "../products";
import {ActivatedRoute} from "@angular/router";
import {Category} from "../categories";

@Component({
  selector: 'app-category-products',
  templateUrl: './category-products.component.html',
  styleUrls: ['./category-products.component.css'],
})
export class CategoryProductsComponent implements OnInit {
  products: Product[] | undefined;
  constructor(private route: ActivatedRoute) {}

  // products = [...products];

  ngOnInit(): void {
    const routeParams = this.route.snapshot.paramMap;
    const catIdFromRoute = Number(routeParams.get('categoryId'));
    // console.log(catIdFromRoute);
    this.products = products.filter((p) => p.category.id == catIdFromRoute);
  }

  share(link: string | URL | undefined) {
    window.open(
      'https://t.me/+rO6kV466qV1jMDE6' + link,
      'menubar=off, toolbar=off'
    );
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}