import { Component, OnInit } from '@angular/core';
import {Categories, Category} from '../categories';

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.css']
})

export class CategoriesComponent implements OnInit {
  categories: Category[] = Categories;
  ngOnInit(): void{
  }
}