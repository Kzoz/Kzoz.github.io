//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "tdeecalc.h"
#include <iostream>
#include <string>
#include <cstdlib>
#include "tdeeResult.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TTDEEC *TDEEC;
//---------------------------------------------------------------------------
__fastcall TTDEEC::TTDEEC(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TTDEEC::CalculateBtnClick(TObject *Sender)
{
	double height = HeightEdit->Text.ToInt();
	double weight = WeightEdit->Text.ToInt();
	double age = AgeEdit->Text.ToInt();
	double bodyfat = BodyFatEdit->Text.ToInt();
	int idactivity = ActivityComboBox->ItemIndex;
	//String activity = ActivityComboBox->Items->Strings[idactivity];
	double daily_intake;
    double optimal_intake;
	double lbm = weight*(100-bodyfat)/100;  // Print the Lean Body Mass
	int idobjectives = ObjectivesComboBox->ItemIndex;
    String objectives = ObjectivesComboBox->Items->Strings[idobjectives];



	// Calculate BMI
	double mybmi= weight/height/height*10000;


	// Calculate BMR
	double mybmr;
	if (MaleRadio->Checked == true) {
		mybmr=88.362+(13.397*weight)+(4.799*height)-(5.677*age);
	}

	else if(FemaleRadio->Checked == true){
		mybmr=447.593+(9.247*weight)+(3.098*height)-(4.330*age);
	}


	// Calculate daily Intake

	if (bodyfat > 0) {

		if (idactivity == 0) {
			daily_intake = mybmr*1;
		}
		else if ((idactivity == 1)) {
				 daily_intake = mybmr*1.1;
			 }
		else if (idactivity == 2) {
				 daily_intake=mybmr*1.2;
			 }
		else if (idactivity == 3) {
				 daily_intake=mybmr*1.3;
			 }
		else if (idactivity == 4) {
				 daily_intake = mybmr*1.5;
		 }
	 }
	 else {
		 //Print incorrect input
	 }
	/*
				Sedentary(office job)
			Light Exercise (1-2 days/week)
			Moderate Exercise (3-5 dyas/week)
			Heavy Exercise (6-7 days/week)
			Athlete (2x per day)
	*/

	if (idobjectives == 0) {
		optimal_intake = daily_intake*0.91;
	}
	else if (idobjectives == 1) {
			 optimal_intake = daily_intake*1.02;
		 }
	else if (idobjectives ==2) {
			 optimal_intake = daily_intake*1.16;
		 }



	// Print out the results
	TDEER->ResultMemo->Lines->Add("Considering your weight: "+FloatToStrF(weight,ffFixed,8,0)+" kg, height: "+FloatToStrF(height,ffFixed,8,0)+" cm and age, your BMI is "+FloatToStrF(mybmi,ffFixed,8,2)+" and your BMR is "+FloatToStrF(mybmr,ffFixed,8,0)+" kcals per day.");
	TDEER->ResultMemo->Lines->Add("Your Lean Body Mass is " +FloatToStrF(lbm,ffFixed,8,2) +" kg.");
	//TDEER->ResultMemo->Lines->Add(IntToStr(idactivity)+" "+IntToStr(idobjectives));
	TDEER->ResultMemo->Lines->Add("If you are "+objectives+", you should aim a daily intake of "+ FloatToStrF(optimal_intake,ffFixed,8,0)+" kcals.\n");

	ModalResult = 0;
	TDEER->ShowModal();







}
//---------------------------------------------------------------------------

