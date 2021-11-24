//---------------------------------------------------------------------------

#ifndef tdeeResultH
#define tdeeResultH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
//---------------------------------------------------------------------------
class TTDEER : public TForm
{
__published:	// IDE-managed Components
	TMemo *ResultMemo;
private:	// User declarations
public:		// User declarations
	__fastcall TTDEER(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TTDEER *TDEER;
//---------------------------------------------------------------------------
#endif
