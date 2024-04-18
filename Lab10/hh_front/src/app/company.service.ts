import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {Company, Vacancy} from "./models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  BASE_URL = 'http://localhost:8000'
  constructor(private client: HttpClient) { }

  getCompany(id: number): Observable<Company>{
    return this.client.get<Company>(
      `${this.BASE_URL}/api/companies/${id}/`
    )
  }

  getCompanies(): Observable<Company[]>{
    return this.client.get<Company[]>(
      `${this.BASE_URL}/api/companies/`
    )
  }

  getVacancies(id: number): Observable<Vacancy[]>{
    return this.client.get<Vacancy[]>(
      `${this.BASE_URL}/api/companies/${id}/vacancies/`
    )
  }

}
