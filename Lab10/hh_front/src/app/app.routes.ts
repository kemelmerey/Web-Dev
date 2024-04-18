import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AppComponent} from "./app.component";
import {VacancyComponent} from "./vacancy/vacancy.component";
import {CompanyComponent} from "./company/company.component";


export const routes: Routes = [
  {path: 'home', component: AppComponent},
  {path: 'companies', component: CompanyComponent},
  {path: 'companies/:id/vacancies', component: VacancyComponent},
];
