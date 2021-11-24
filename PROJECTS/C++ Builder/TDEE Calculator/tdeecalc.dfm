object TDEEC: TTDEEC
  Left = 0
  Top = 0
  Caption = 'TDEE CALCULATOR'
  ClientHeight = 436
  ClientWidth = 418
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -13
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 16
  object TitleLabel: TLabel
    Left = 0
    Top = 0
    Width = 418
    Height = 24
    Align = alTop
    Alignment = taCenter
    Caption = 'Learn How Many Calories You Need Every Day'
    Font.Charset = ANSI_CHARSET
    Font.Color = clBlue
    Font.Height = -19
    Font.Name = 'Tempus Sans ITC'
    Font.Style = []
    ParentFont = False
    ExplicitWidth = 379
  end
  object GenderLabel: TLabel
    Left = 103
    Top = 62
    Width = 41
    Height = 16
    Caption = 'Gender'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object AgeLabel: TLabel
    Left = 122
    Top = 105
    Width = 22
    Height = 16
    Caption = 'Age'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object WeightLabel: TLabel
    Left = 104
    Top = 153
    Width = 40
    Height = 16
    Caption = 'Weight'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object HeightLabel: TLabel
    Left = 108
    Top = 201
    Width = 36
    Height = 16
    Caption = 'Height'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object ActivityLabel: TLabel
    Left = 104
    Top = 246
    Width = 40
    Height = 16
    Caption = 'Activity'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object BodyFatLabel: TLabel
    Left = 16
    Top = 345
    Width = 126
    Height = 16
    Caption = 'Body Fat % (Optional)'
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Tahoma'
    Font.Style = []
    ParentFont = False
  end
  object ObjectiveLabel: TLabel
    Left = 85
    Top = 296
    Width = 59
    Height = 16
    Caption = 'Objectives'
  end
  object CmLabel: TLabel
    Left = 223
    Top = 201
    Width = 17
    Height = 16
    Caption = 'cm'
  end
  object kgLabel: TLabel
    Left = 223
    Top = 153
    Width = 13
    Height = 16
    Caption = 'kg'
  end
  object CalculateBtn: TButton
    Left = 0
    Top = 386
    Width = 418
    Height = 50
    Align = alBottom
    Caption = 'Calculate'
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -27
    Font.Name = 'Century'
    Font.Style = []
    ParentFont = False
    TabOrder = 0
    OnClick = CalculateBtnClick
  end
  object AgeEdit: TEdit
    Left = 168
    Top = 104
    Width = 49
    Height = 24
    TabOrder = 1
  end
  object WeightEdit: TEdit
    Left = 168
    Top = 152
    Width = 49
    Height = 24
    TabOrder = 2
  end
  object HeightEdit: TEdit
    Left = 168
    Top = 200
    Width = 49
    Height = 24
    TabOrder = 3
  end
  object BodyFatEdit: TEdit
    Left = 168
    Top = 342
    Width = 49
    Height = 24
    TabOrder = 4
  end
  object MaleRadio: TRadioButton
    Left = 168
    Top = 63
    Width = 49
    Height = 17
    Caption = 'Male'
    Checked = True
    TabOrder = 5
    TabStop = True
  end
  object FemaleRadio: TRadioButton
    Left = 223
    Top = 63
    Width = 66
    Height = 17
    Caption = 'Female'
    TabOrder = 6
  end
  object ActivityComboBox: TComboBox
    Left = 168
    Top = 245
    Width = 217
    Height = 24
    Cursor = crHandPoint
    Style = csDropDownList
    TabOrder = 7
    Items.Strings = (
      'Sedentary(office job)'
      'Light Exercise (1-2 days/week)'
      'Moderate Exercise (3-5 days/week)'
      'Heavy Exercise (6-7 days/week)'
      'Athlete (2x per day)')
  end
  object ObjectivesComboBox: TComboBox
    Left = 168
    Top = 293
    Width = 121
    Height = 24
    Cursor = crHandPoint
    Hint = 'Select from below'
    Style = csDropDownList
    TabOrder = 8
    Items.Strings = (
      'Cutting'
      'Maintaining'
      'Bulking')
  end
end
