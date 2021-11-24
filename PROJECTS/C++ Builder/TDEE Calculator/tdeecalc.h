//---------------------------------------------------------------------------

#ifndef tdeecalcH
#define tdeecalcH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TTDEEC : public TForm
{
__published:	// IDE-managed Components
	TLabel *TitleLabel;
	TLabel *GenderLabel;
	TLabel *AgeLabel;
	TLabel *WeightLabel;
	TLabel *HeightLabel;
	TLabel *ActivityLabel;
	TLabel *BodyFatLabel;
	TButton *CalculateBtn;
	TEdit *AgeEdit;
	TEdit *WeightEdit;
	TEdit *HeightEdit;
	TEdit *BodyFatEdit;
	TRadioButton *MaleRadio;
	TRadioButton *FemaleRadio;
	TComboBox *ActivityComboBox;
	TLabel *ObjectiveLabel;
	TComboBox *ObjectivesComboBox;
	TLabel *CmLabel;
	TLabel *kgLabel;
	void __fastcall CalculateBtnClick(TObject *Sender);
private:	// User declarations
public:		// User declarations
	__fastcall TTDEEC(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TTDEEC *TDEEC;
//---------------------------------------------------------------------------
#endif
