import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {CompanyService} from "./company.service";
import {Company} from "./models";
import {CommonModule} from "@angular/common";
import {RouterModule} from "@angular/router";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, RouterModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent implements OnInit {
  title = 'hh_front';
  companies: Company[] = [];

  ngOnInit() {
      // this.getCompanies();
  }

  constructor(private companyService: CompanyService){}

  // getCompanies() {
  //   this.companyService
  //     .getCompanies()
  //     .subscribe((data) => {
  //       console.log(data);
  //       this.companies = data;
  //     });
  // }
}


