import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, RouterModule} from "@angular/router";
import {CompanyService} from "../company.service";
import {Company, Vacancy} from "../models";
import { FormsModule } from '@angular/forms';
import {CommonModule} from "@angular/common";
@Component({
  selector: 'app-vacancy',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css'
})


export class VacancyComponent implements OnInit{
  companyID: number = -1
  company = {} as Company
  vacancies: Vacancy[] = []
  constructor(private route: ActivatedRoute, private companyService: CompanyService) {
  }

  ngOnInit() {
    this.companyID = Number(this.route.snapshot.paramMap.get('id'));
    this.getVacancies(this.companyID)
    this.getCompany(this.companyID)
  }

  getCompany(id: number){
    this.companyService.getCompany(id).subscribe( (company) => {
      this.company = company
    })
  }

  getVacancies(id: number){
    console.log(id)
    this.companyService.getVacancies(id).subscribe(( (vacancies) => {
      this.vacancies = vacancies;
      console.log(vacancies)
    }))
  }

}

