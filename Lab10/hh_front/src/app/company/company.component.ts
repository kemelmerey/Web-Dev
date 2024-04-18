import {CommonModule} from "@angular/common";
import {Component, OnInit} from '@angular/core';
import {Company} from "../models";
import {CompanyService} from "../company.service";
import {FormsModule} from "@angular/forms";
import {RouterModule} from "@angular/router";

@Component({
  selector: 'app-company',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './company.component.html',
  styleUrl: './company.component.css'
})

export class CompanyComponent implements OnInit{
  companies: Company[] = []

  ngOnInit() {
    this.getCompanies()
  }

  constructor(private companyService: CompanyService) {
  }

  getCompanies(){
    this.companyService.getCompanies().subscribe( (companies) => {
      this.companies = companies
    })
  }

}

