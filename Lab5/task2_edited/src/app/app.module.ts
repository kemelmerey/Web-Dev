import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductDetailsComponent } from './product-details/product-details.component';
import { HttpClientModule } from '@angular/common/http';
import { CategoriesComponent } from './categories/categories.component';
import {Categories} from "./categories";
import { CategoryProductsComponent } from './category-products/category-products.component';

@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      {path: '', component: CategoriesComponent },
      {path:'category/:categoryId/products', component: CategoryProductsComponent},
      {path: 'products/:productId', component: ProductDetailsComponent },
      {path: 'products', component: ProductListComponent},
    ])
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    ProductListComponent,
    ProductDetailsComponent,
    CategoriesComponent,
    CategoryProductsComponent
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }