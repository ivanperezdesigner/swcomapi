"""Stub for swcomapi.enums. Generated, do not edit.

Source: SOLIDWORKS 2026 type libraries (cosworks.tlb, sldcostingapi.tlb, sldworks.tlb,
  sustainability.tlb, swcommands.tlb, swconst.tlb, swdimxpert.tlb,
  swmotionstudy.tlb, swpublished.tlb, SWRoutingLib.tlb)
"""

from enum import IntEnum

class sw3DExperienceCfgType_e(IntEnum):
    """sw3DExperienceCfgType_e (3 constants, from SwConst)."""
    swNot3DExperienceType = 0
    swPhysicalProduct = 1
    swRepresentation = 2

class sw3DExperienceModelType_e(IntEnum):
    """sw3DExperienceModelType_e (4 constants, from SwConst)."""
    sw3DExperienceModelType_Standard = 0
    sw3DExperienceModelType_PartSupply = 1
    sw3DExperienceModelType_3DExperience = 2
    sw3DExperienceModelType_xCad = 3

class sw3DExperienceState_e(IntEnum):
    """sw3DExperienceState_e (3 constants, from SwConst)."""
    sw3DExperienceState_None = 0
    sw3DExperienceState_Online = 1
    sw3DExperienceState_Offline = 2

class sw3DInterconnectImportErrors_e(IntEnum):
    """sw3DInterconnectImportErrors_e (7 constants, from SwConst)."""
    sw3DInterconnectImportErrors_None = 0
    sw3DInterconnectImportErrors_Disabled = 1
    sw3DInterconnectImportErrors_IncompatibleType = 2
    sw3DInterconnectImportErrors_AssemblyNotSaved = 3
    sw3DInterconnectImportErrors_BreakLinkUnavailable = 4
    sw3DInterconnectImportErrors_ParametersUnavailable = 5
    sw3DInterconnectImportErrors_TransferOptionNeeded = 6

class sw3DPDFAccuracy_e(IntEnum):
    """sw3DPDFAccuracy_e (4 constants, from SwConst)."""
    swMaximum = 0
    swHigh = 1
    swMedium = 2
    swLow = 3

class sw3DPMISaveOptions_e(IntEnum):
    """sw3DPMISaveOptions_e (4 constants, from SwConst)."""
    swAddReportToDesignBinder = 1
    swViewReportOnSave = 2
    swDimXpertData = 4
    swReferenceData = 8

class swASMSLDPRTCompPref_e(IntEnum):
    """swASMSLDPRTCompPref_e (3 constants, from SwConst)."""
    swUseSystemSettings = 0
    swAlwaysInclude = 1
    swAlwaysExclude = 2

class swAcisOutputGeometryPreference_e(IntEnum):
    """swAcisOutputGeometryPreference_e (3 constants, from SwConst)."""
    swAcisOutputAsSolidAndSurface = 0
    swAcisOutputAs3DCurves = 1
    swAcisOutputAs3DCurves_IncludeSketchEnts = 2

class swAcisOutputVersion_e(IntEnum):
    """swAcisOutputVersion_e (25 constants, from SwConst)."""
    swAcisOutputVersion_16 = 0
    swAcisOutputVersion_17 = 1
    swAcisOutputVersion_20 = 2
    swAcisOutputVersion_21 = 3
    swAcisOutputVersion_30 = 4
    swAcisOutputVersion_40 = 5
    swAcisOutputVersion_50 = 6
    swAcisOutputVersion_60 = 7
    swAcisOutputVersion_70 = 8
    swAcisOutputVersion_80 = 9
    swAcisOutputVersion_100 = 10
    swAcisOutputVersion_110 = 11
    swAcisOutputVersion_120 = 12
    swAcisOutputVersion_130 = 13
    swAcisOutputVersion_140 = 14
    swAcisOutputVersion_150 = 15
    swAcisOutputVersion_160 = 16
    swAcisOutputVersion_170 = 17
    swAcisOutputVersion_180 = 18
    swAcisOutputVersion_190 = 19
    swAcisOutputVersion_200 = 20
    swAcisOutputVersion_210 = 21
    swAcisOutputVersion_220 = 22
    swAcisOutputVersion_270 = 23
    swAcisOutputVersion_330 = 24

class swActivateDocError_e(IntEnum):
    """swActivateDocError_e (2 constants, from SwConst)."""
    swGenericActivateError = 1
    swDocNeedsRebuildWarning = 2

class swAddComponentConfigOptions_e(IntEnum):
    """swAddComponentConfigOptions_e (3 constants, from SwConst)."""
    swAddComponentConfigOptions_CurrentSelectedConfig = 0
    swAddComponentConfigOptions_NewConfigWithAllReferenceModels = 1
    swAddComponentConfigOptions_NewConfigWithAsmStructure = 2

class swAddControlOptions_e(IntEnum):
    """swAddControlOptions_e (3 constants, from SwConst)."""
    swControlOptions_Visible = 1
    swControlOptions_Enabled = 2
    swControlOptions_SmallGapAbove = 4

class swAddDvePageForCommand_e(IntEnum):
    """swAddDvePageForCommand_e (1 constants, from SwConst)."""
    swAddDvePageFor_SketchPicture = 1

class swAddGroupBoxOptions_e(IntEnum):
    """swAddGroupBoxOptions_e (4 constants, from SwConst)."""
    swGroupBoxOptions_Checkbox = 1
    swGroupBoxOptions_Checked = 2
    swGroupBoxOptions_Visible = 4
    swGroupBoxOptions_Expanded = 8

class swAddMateError_e(IntEnum):
    """swAddMateError_e (7 constants, from SwConst)."""
    swAddMateError_ErrorUknown = 0
    swAddMateError_NoError = 1
    swAddMateError_IncorrectMateType = 2
    swAddMateError_IncorrectAlignment = 3
    swAddMateError_IncorrectSelections = 4
    swAddMateError_OverDefinedAssembly = 5
    swAddMateError_IncorrectGearRatios = 6

class swAddOrdinateDims_e(IntEnum):
    """swAddOrdinateDims_e (4 constants, from SwConst)."""
    swOrdinate = 1
    swVerticalOrdinate = 2
    swHorizontalOrdinate = 3
    swAngularOrdinate = 4

class swAddSpecificDimension_e(IntEnum):
    """swAddSpecificDimension_e (2 constants, from SwConst)."""
    swAddSpecificDimension_Success = 0
    swAddSpecificDimension_DimTypeMismatch = 1

class swAddToRecentDocumentList_e(IntEnum):
    """swAddToRecentDocumentList_e (3 constants, from SwConst)."""
    swAddToRecentDocumentList_Default = 0
    swAddToRecentDocumentList_Add = 1
    swAddToRecentDocumentList_DontAdd = 2

class swAddinBrokerBBoxOption_e(IntEnum):
    """swAddinBrokerBBoxOption_e (1 constants, from SwConst)."""
    swAddinBrokerBBoxOption_Default = 0

class swAdditionalSymbol_e(IntEnum):
    """swAdditionalSymbol_e (7 constants, from SwConst)."""
    swAdditionalSymbol_None = 0
    swAdditionalSymbol_Unknown = 1
    swAdditionalSymbol_TangentPlane = 2
    swAdditionalSymbol_FreeState = 3
    swAdditionalSymbol_Statistical = 4
    swAdditionalSymbol_MaximumUpperTolerance = 5
    swAdditionalSymbol_MinimumLowerTolerance = 6

class swAdvSelectType_e(IntEnum):
    """swAdvSelectType_e (16 constants, from SwConst)."""
    swAdvSelectType_And = 1
    swAdvSelectType_Or = 2
    swAdvSelectType_Is_Yes = 16384
    swAdvSelectType_Is_No = 32768
    swAdvSelectType_Is_Not = 8
    swAdvSelectType_Contains = 16
    swAdvSelectType_Is_Ccontained_By = 32
    swAdvSelectType_Interferes_With = 64
    swAdvSelectType_Does_Not_Interferes_With = 128
    swAdvSelectType_Is_Exactly = 4
    swAdvSelectType_Is_Not_Equal = 8192
    swAdvSelectType_Less_Than = 512
    swAdvSelectType_Less_Than_OR_Equal = 2048
    swAdvSelectType_Equals = 4096
    swAdvSelectType_Greater_Than_OR_Equal = 1024
    swAdvSelectType_Greater_Than = 256

class swAdvWzdGeneralHoleTypes_e(IntEnum):
    """swAdvWzdGeneralHoleTypes_e (5 constants, from SwConst)."""
    swAdvWzdCounterBore = 0
    swAdvWzdCounterSink = 1
    swAdvWzdStraight = 2
    swAdvWzdStraightTap = 3
    swAdvWzdTaperTap = 4

class swAdvancedHoleResults_e(IntEnum):
    """swAdvancedHoleResults_e (2 constants, from SwConst)."""
    swAdvancedHoleResults_Success = 0
    swAdvancedHoleResults_FailedIncorrectHoleElementParameters = 1

class swAdvancedRouteSelectionOutput_e(IntEnum):
    """swAdvancedRouteSelectionOutput_e (3 constants, from SWRoutingLib)."""
    swBoth = 0
    swSelectOnly = 1
    swDataOnly = 2

class swAlignDimensionType_e(IntEnum):
    """swAlignDimensionType_e (8 constants, from SwConst)."""
    swAlignDimensionType_AutoArrange = 0
    swAlignDimensionType_SpaceEvenly = 1
    swAlignDimensionType_Colinear = 2
    swAlignDimensionType_Stagger = 3
    swAlignDimensionType_TopAlignText = 4
    swAlignDimensionType_BottomAlignText = 5
    swAlignDimensionType_LeftAlignText = 6
    swAlignDimensionType_RightAligntext = 7

class swAlignDrawingViewTypes_e(IntEnum):
    """swAlignDrawingViewTypes_e (4 constants, from SwConst)."""
    swHorizontalToSheetClockwise = 0
    swHorizontalToSheetCounterclockwise = 1
    swDefaultAlignment = 2
    swProjectedAngle = 3

class swAlignViewTypes_e(IntEnum):
    """swAlignViewTypes_e (6 constants, from SwConst)."""
    swNoViewAlignment = 0
    swDefaultViewAlignment = 1
    swAlignViewHorizontalCenter = 2
    swAlignViewVerticalCenter = 3
    swAlignViewHorizontalOrigin = 4
    swAlignViewVerticalOrigin = 5

class swAngleUnit_e(IntEnum):
    """swAngleUnit_e (4 constants, from SwConst)."""
    swDEGREES = 0
    swDEG_MIN = 1
    swDEG_MIN_SEC = 2
    swRADIANS = 3

class swAngularEquationUnits_e(IntEnum):
    """swAngularEquationUnits_e (3 constants, from SwConst)."""
    swAngularEquationUnitsUnrecognized = 0
    swAngularEquationUnitsDegrees = 1
    swAngularEquationUnitsRadians = 2

class swAnimationOutputType_e(IntEnum):
    """swAnimationOutputType_e (10 constants, from SwConst)."""
    swAnimationOutput_AVI = 1
    swAnimationOutput_Series_of_BMP = 2
    swAnimationOutput_Series_of_TGA = 3
    swAnimationOutput_Series_of_PNG = 4
    swAnimationOutput_Series_of_JPG = 5
    swAnimationOutput_Series_of_TIF = 6
    swAnimationOutput_Series_of_MP4 = 7
    swAnimationOutput_Series_of_MKV = 8
    swAnimationOutput_Series_of_FLV = 9
    swAnimationOutput_Series_of_LXO = 10

class swAnimationPlayMode_e(IntEnum):
    """swAnimationPlayMode_e (3 constants, from SwConst)."""
    swAnimationPlayModeNormal = 1
    swAnimationPlayModeLoop = 2
    swAnimationPlayModeReciprocate = 3

class swAnimationPlaySpeed_e(IntEnum):
    """swAnimationPlaySpeed_e (3 constants, from SwConst)."""
    swAnimationPlaySpeedNormal = 1
    swAnimationPlaySpeedSlow = 2
    swAnimationPlaySpeedFast = 3

class swAnimatorAxisOfRotation_e(IntEnum):
    """swAnimatorAxisOfRotation_e (3 constants, from SwConst)."""
    swRotationAboutXAxis = 0
    swRotationAboutYAxis = 1
    swRotationAboutZAxis = 2

class swAnimatorDirectionOfRotation_e(IntEnum):
    """swAnimatorDirectionOfRotation_e (2 constants, from SwConst)."""
    swRotationClockwise = 0
    swRotationCounterClockwise = 1

class swAnnotationOwner_e(IntEnum):
    """swAnnotationOwner_e (5 constants, from SwConst)."""
    swAnnotationOwner_DrawingView = 0
    swAnnotationOwner_DrawingSheet = 1
    swAnnotationOwner_DrawingTemplate = 2
    swAnnotationOwner_Part = 3
    swAnnotationOwner_Assembly = 4

class swAnnotationType_e(IntEnum):
    """swAnnotationType_e (19 constants, from SwConst)."""
    swCThread = 1
    swDatumTag = 2
    swDatumTargetSym = 3
    swDisplayDimension = 4
    swGTol = 5
    swNote = 6
    swSFSymbol = 7
    swWeldSymbol = 8
    swCustomSymbol = 9
    swDowelSym = 10
    swLeader = 11
    swBlock = 12
    swCenterMarkSym = 13
    swTableAnnotation = 14
    swCenterLine = 15
    swDatumOrigin = 16
    swWeldBeadSymbol = 17
    swRevisionCloud = 18
    swPMIOnly = 19

class swAnnotationVisibilityState_e(IntEnum):
    """swAnnotationVisibilityState_e (4 constants, from SwConst)."""
    swAnnotationVisibilityUnknown = 0
    swAnnotationVisible = 1
    swAnnotationHalfHidden = 2
    swAnnotationHidden = 3

class swApiHoleWizardItemExportStatus_e(IntEnum):
    """swApiHoleWizardItemExportStatus_e (3 constants, from SwConst)."""
    swApiHoleWizardItemExportStatus_Success = 0
    swApiHoleWizardItemExportStatus_InvalidArgument = 1
    swApiHoleWizardItemExportStatus_MicrosoftExcelNotInstalled = 2

class swApiHoleWizardItemImportStatus_e(IntEnum):
    """swApiHoleWizardItemImportStatus_e (9 constants, from SwConst)."""
    swApiHoleWizardItemImportStatus_Success = 0
    swApiHoleWizardItemImportStatus_InvalidArgument = 1
    swApiHoleWizardItemImportStatus_MicrosoftExcelNotInstalled = 2
    swApiHoleWizardItemImportStatus_FailedToSaveFile = 3
    swApiHoleWizardItemImportStatus_ExcelCouldNotOpenFile = 4
    swApiHoleWizardItemImportStatus_ExcelSheetNameError = 5
    swApiHoleWizardItemImportStatus_FailedToSaveReportFile = 6
    swApiHoleWizardItemImportStatus_DataError = 7
    swApiHoleWizardItemImportStatus_UnspecifiedError = 8

class swApiToolboxItemExportStatus_e(IntEnum):
    """swApiToolboxItemExportStatus_e (5 constants, from SwConst)."""
    swApiToolboxItemExportStatus_Success = 0
    swApiToolboxItemExportStatus_InvalidArgument = 1
    swApiToolboxItemExportStatus_MicrosoftExcelNotInstalled = 2
    swApiToolboxItemExportStatus_FailedToSaveFile = 3
    swApiToolboxItemExportStatus_InvalidPartNumber = 4

class swApiToolboxItemImportStatus_e(IntEnum):
    """swApiToolboxItemImportStatus_e (9 constants, from SwConst)."""
    swApiToolboxItemImportStatus_Success = 0
    swApiToolboxItemImportStatus_InvalidArgument = 1
    swApiToolboxItemImportStatus_MicrosoftExcelNotInstalled = 2
    swApiToolboxItemImportStatus_FailedToSaveFile = 3
    swApiToolboxItemImportStatus_ExcelImportDidNotFindColumn = 4
    swApiToolboxItemImportStatus_ExcelImportWrongFile = 5
    swApiToolboxItemImportStatus_ExcelCouldNotOpenFile = 6
    swApiToolboxItemImportStatus_InvalidPartNumber = 7
    swApiToolboxItemImportStatus_FailedUnspecifiedError = 8

class swAppCallBackCmd_e(IntEnum):
    """swAppCallBackCmd_e (5 constants, from SwConst)."""
    swAppIsNewCmd = 1
    swAppWhatsNewDescription = 2
    swAppHelpContext = 3
    swAppIsCmdEnabled = 4
    swAppPostNotifyEvent = 5

class swAppNotify_e(IntEnum):
    """swAppNotify_e (46 constants, from SwConst)."""
    swAppFileOpenNotify = 1
    swAppFileNewNotify = 2
    swAppDestroyNotify = 3
    swAppActiveDocChangeNotify = 4
    swAppActiveModelDocChangeNotify = 5
    swAppPropertySheetCreateNotify = 6
    swAppNonNativeFileOpenNotify = 7
    swAppLightSheetCreateNotify = 8
    swAppDocumentConversionNotify = 9
    swAppLightweightComponentOpenNotify = 10
    swAppDocumentLoadNotify = 11
    swAppFileNewNotify2 = 12
    swAppFileOpenNotify2 = 13
    swAppReferenceNotFoundNotify = 14
    swAppPromptForFilenameNotify = 15
    swAppBeginTranslationNotify = 16
    swAppEndTranslationNotify = 17
    swAppLightPMCreateNotify = 18
    swAppStandardsDatabaseChangeNotify = 19
    swAppOnIdleNotify = 20
    swAppFileOpenPreNotify = 21
    swAppFileOpenPostNotify = 22
    swAppReferencedFilePreNotify = 23
    swAppBeginRecordNotify = 24
    swAppEndRecordNotify = 25
    swAppFileNewPreNotify = 26
    swAppJournalWriteNotify = 27
    swAppDocumentLoadNotify2 = 28
    swAppCommandCloseNotify = 29
    swAppPromptForMultipleFilenamesNotify = 30
    swAppCommandOpenPreNotify = 31
    swAppFileCloseNotify = 32
    swAppBackgroundProcessingStartNotify = 33
    swAppBackgroundProcessingEndNotify = 34
    swAppInterfaceBrightnessThemeChangeNotify = 35
    swAppReferencedFilePreNotify2 = 36
    swAppBegin3DInterconnectTranslationNotify = 37
    swAppEnd3DInterconnectTranslationNotify = 38
    swAppTaskPanePinnedNotify = 39
    swAppTaskPaneUnpinnedNotify = 40
    swAppTaskPaneHideNotify = 41
    swAppTaskPaneShowNotify = 42
    swAppTaskPaneExpandNotify = 43
    swAppTaskPaneCollapseNotify = 44
    swAppDisplayPaneActivationNotify = 45
    swAppOn3DExperienceStateChangeNotify = 46

class swAppearanceSurfaceFinishShaderTypes_e(IntEnum):
    """swAppearanceSurfaceFinishShaderTypes_e (21 constants, from SwConst)."""
    swAppearanceSurfaceFinishShaderType_DefaultColor = 0
    swAppearanceSurfaceFinishShaderType_None = 1
    swAppearanceSurfaceFinishShaderType_FromFile = 2
    swAppearanceSurfaceFinishShaderType_Brushed = 3
    swAppearanceSurfaceFinishShaderType_Burnished = 4
    swAppearanceSurfaceFinishShaderType_Cast = 5
    swAppearanceSurfaceFinishShaderType_Wrought = 6
    swAppearanceSurfaceFinishShaderType_Machined = 7
    swAppearanceSurfaceFinishShaderType_Knurled = 8
    swAppearanceSurfaceFinishShaderType_Treadplate1 = 9
    swAppearanceSurfaceFinishShaderType_Dimpled = 10
    swAppearanceSurfaceFinishShaderType_ChainLink = 11
    swAppearanceSurfaceFinishShaderType_Sandblasted = 12
    swAppearanceSurfaceFinishShaderType_Rough1 = 13
    swAppearanceSurfaceFinishShaderType_Rough2 = 14
    swAppearanceSurfaceFinishShaderType_DiamondTreadplate = 15
    swAppearanceSurfaceFinishShaderType_Treadplate2 = 16
    swAppearanceSurfaceFinishShaderType_DiamondHoleMesh = 17
    swAppearanceSurfaceFinishShaderType_CircularHoleMesh = 18
    swAppearanceSurfaceFinishShaderType_CustomHoleMesh = 19
    swAppearanceSurfaceFinishShaderType_Undefined = 20

class swAppearanceTargetType_e(IntEnum):
    """swAppearanceTargetType_e (6 constants, from SwConst)."""
    swAppearanceTargetFace = 0
    swAppearanceTargetFeature = 1
    swAppearanceTargetBody = 2
    swAppearanceTargetPart = 3
    swAppearanceTargetComponent = 4
    swAppearanceTargetAppearanceFilter = 5

class swApplicationType_e(IntEnum):
    """swApplicationType_e (3 constants, from SwConst)."""
    swApplicationType_Desktop = 0
    swApplicationType_3DEXPERIENCE = 1
    swApplicationType_WithConnector = 2

class swArcEndCondition_e(IntEnum):
    """swArcEndCondition_e (4 constants, from SwConst)."""
    swArcEndConditionNone = 0
    swArcEndConditionCenter = 1
    swArcEndConditionMin = 2
    swArcEndConditionMax = 3

class swArcLengthLeaderType_e(IntEnum):
    """swArcLengthLeaderType_e (2 constants, from SwConst)."""
    swArcLengthLeaderParallel = 1
    swArcLengthLeaderRadial = 2

class swAreaHatchFillStyle_e(IntEnum):
    """swAreaHatchFillStyle_e (3 constants, from SwConst)."""
    swAreaHatchFillStyle_None = 1
    swAreaHatchFillStyle_Pattern = 2
    swAreaHatchFillStyle_Solid = 3

class swAreaHatchingScope_e(IntEnum):
    """swAreaHatchingScope_e (4 constants, from SwConst)."""
    swAreaHatchingScope_Region = 0
    swAreaHatchingScope_Component = 1
    swAreaHatchingScope_View = 2
    swAreaHatchingScope_Body = 3

class swArrowDirection_e(IntEnum):
    """swArrowDirection_e (3 constants, from SwConst)."""
    swINSIDE = 0
    swOUTSIDE = 1
    swSMART = 2

class swArrowPlacement_e(IntEnum):
    """swArrowPlacement_e (3 constants, from SwConst)."""
    swArrowPlacementLegacy = 0
    swArrowPlacementSmartArrowFollowText = 1
    swArrowPlacementSmartArrowRemainAttachedToArc = 2

class swArrowPosition(IntEnum):
    """swArrowPosition (16 constants, from SwConst)."""
    swArrowLeftTop = 0
    swArrowLeftBottom = 1
    swArrowRightTop = 2
    swArrowRightBottom = 3
    swArrowUpTopLeft = 4
    swArrowUpTopRight = 5
    swArrowDownBottomLeft = 6
    swArrowDownBottomRight = 7
    swArrowLeftOrRightTop = 8
    swArrowLeftOrRightBottom = 9
    swArrowLeftOrRight = 10
    swArrowUpOrDownLeft = 11
    swArrowUpOrDownRight = 12
    swArrowUpOrDown = 13
    swArrowNone = 14
    swArrowUnknown = 15

class swArrowStyle_e(IntEnum):
    """swArrowStyle_e (13 constants, from SwConst)."""
    swOPEN_ARROWHEAD = 0
    swCLOSED_ARROWHEAD = 1
    swSLASH_ARROWHEAD = 2
    swDOT_ARROWHEAD = 3
    swORIGIN_ARROWHEAD = 4
    swWIDE_ARROWHEAD = 5
    swISOWIDE_ARROWHEAD = 6
    swRUS_ARROWHEAD = 7
    swCLOSETOP_ARROWHEAD = 8
    swCLOSEBOT_ARROWHEAD = 9
    swNO_ARROWHEAD = 10
    swSHOULDER_ARROWHEAD = 11
    swSMART_ARROWHEAD = 12

class swAssemblyDeleteOptions_e(IntEnum):
    """swAssemblyDeleteOptions_e (2 constants, from SwConst)."""
    swDelete_SubAssembly = 1
    swDelete_SelectedComponents = 0

class swAssemblyExplodeStepType(IntEnum):
    """swAssemblyExplodeStepType (3 constants, from SwConst)."""
    swAssemblyExplodeStepType_Translate = 0
    swAssemblyExplodeStepType_Radial = 1
    swAssemblyExplodeStepType_SubAssembly = 2

class swAssemblyLevelToUpdate_e(IntEnum):
    """swAssemblyLevelToUpdate_e (3 constants, from SwConst)."""
    swAssemblyLevelToUpdate_TopLevelAssemblyOnly = 0
    swAssemblyLevelToUpdate_SubLevelAssemblyOnly = 1
    swAssemblyLevelToUpdate_AllLevels = 2

class swAssemblyLoadComponents_e(IntEnum):
    """swAssemblyLoadComponents_e (2 constants, from SwConst)."""
    swAssemblyLoadComponents_AutoLoad = 0
    swAssemblyLoadComponents_ManualLoad = 1

class swAssemblyMode_e(IntEnum):
    """swAssemblyMode_e (5 constants, from SwConst)."""
    swAssemblyMode_None = 0
    swAssemblyMode_Resolved = 1
    swAssemblyMode_LightWeight = 2
    swAssemblyMode_LDR = 3
    swAssemblyMode_LDR_EditAssembly = 4

class swAssemblyNotify_e(IntEnum):
    """swAssemblyNotify_e (104 constants, from SwConst)."""
    swAssemblyRegenNotify = 1
    swAssemblyDestroyNotify = 2
    swAssemblyRegenPostNotify = 3
    swAssemblyViewNewNotify = 4
    swAssemblyNewSelectionNotify = 5
    swAssemblyFileSaveNotify = 6
    swAssemblyFileSaveAsNotify = 7
    swAssemblyLoadFromStorageNotify = 8
    swAssemblySaveToStorageNotify = 9
    swAssemblyConfigChangeNotify = 10
    swAssemblyConfigChangePostNotify = 11
    swAssemblyAutoSaveNotify = 12
    swAssemblyAutoSaveToStorageNotify = 13
    swAssemblyBeginInContextEditNotify = 14
    swAssemblyEndInContextEditNotify = 15
    swAssemblyViewNewNotify2 = 16
    swAssemblyLightingDialogCreateNotify = 17
    swAssemblyAddItemNotify = 18
    swAssemblyRenameItemNotify = 19
    swAssemblyDeleteItemNotify = 20
    swAssemblyModifyNotify = 21
    swAssemblyComponentStateChangeNotify = 22
    swAssemblyFileDropNotify = 23
    swAssemblyFileReloadNotify = 24
    swAssemblyComponentStateChangeNotify2 = 25
    swAssemblyAddCustomPropertyNotify = 26
    swAssemblyChangeCustomPropertyNotify = 27
    swAssemblyDeleteCustomPropertyNotify = 28
    swAssemblyFeatureEditPreNotify = 29
    swAssemblyFeatureSketchEditPreNotify = 30
    swAssemblyFileSaveAsNotify2 = 31
    swAssemblyInterferenceNotify = 32
    swAssemblyDeleteSelectionPreNotify = 33
    swAssemblyFileReloadPreNotify = 34
    swAssemblyComponentMoveNotify = 35
    swAssemblyComponentVisibleChangeNotify = 36
    swAssemblyBodyVisibleChangeNotify = 37
    swAssemblyFileDropPreNotify = 38
    swAssemblyFileSavePostNotify = 39
    swAssemblyLoadFromStorageStoreNotify = 40
    swAssemblySaveToStorageStoreNotify = 41
    swAssemblyFeatureManagerTreeRebuildNotify = 42
    swAssemblyElectricalDataUpdateNotify = 43
    swAssemblyComponentMoveNotify2 = 44
    swAssemblyDynamicHighlightNotify = 45
    swAssemblyComponentVisualPropertiesChangeNotify = 46
    swAssemblyComponentDisplayStateChangeNotify = 47
    swAssemblyDimensionChangeNotify = 48
    swAssemblyFileReloadCancelNotify = 49
    swAssemblyFileSavePostCancelNotify = 50
    swAssemblySketchSolveNotify = 51
    swAssemblyDeleteItemPreNotify = 52
    swAssemblyClearSelectionsNotify = 53
    swAssemblyFileDropPostNotify = 54
    swAssemblyEquationEditorPreNotify = 55
    swAssemblyEquationEditorPostNotify = 56
    swAssemblyOpenDesignTableNotify = 57
    swAssemblyCloseDesignTableNotify = 58
    swAssemblyPromptBodiesToKeepNotify = 59
    swAssemblyAddDvePagePreNotify = 60
    swAssemblyUnitsChangeNotify = 61
    swAssemblyDestroyNotify2 = 62
    swAssemblyConfigurationChangeNotify = 63
    swAssemblyComponentReorganizeNotify = 64
    swAssemblySuppressionStateChangeNotify = 65
    swAssemblyActiveViewChangeNotify = 66
    swAssemblyFeatureManagerFilterStringChangeNotify = 67
    swAssemblyFlipLoopNotify = 68
    swAssemblySensorAlertPreNotify = 69
    swAssemblyActiveDisplayStateChangePreNotify = 70
    swAssemblyActiveDisplayStateChangePostNotify = 71
    swAssemblyAddMatePostNotify = 72
    swAssemblyComponentConfigurationChangeNotify = 73
    swAssemblyUndoPostNotify = 74
    swAssemblyUserSelectionPreNotify = 75
    swAssemblyRedoPostNotify = 76
    swAssemblyRedoPreNotify = 77
    swAssemblyUndoPreNotify = 78
    swAssemblyComponentReferredDisplayStateChangeNotify = 79
    swAssemblySelectiveOpenPostNotify = 80
    swAssemblyRegenPostNotify2 = 81
    swAssemblyAutoSaveToStorageStoreNotify = 82
    swAssemblyDragStateChangeNotify = 83
    swAssemblyInsertTableNotify = 84
    swAssemblyModifyTableNotify = 85
    swAssemblyUserSelectionPostNotify = 86
    swAssemblyComponentDisplayModeChangePreNotify = 87
    swAssemblyComponentDisplayModeChangePostNotify = 88
    swAssemblyCommandManagerTabActivatedPreNotify = 89
    swAssemblyPreRenameItemNotify = 90
    swAssemblyRenamedDocumentNotify = 91
    swAssemblyFeatureManagerTabActivatedPreNotify = 92
    swAssemblyFeatureManagerTabActivatedNotify = 93
    swAssemblyPublishTo3DPDFNotify = 94
    swAssemblyAddMatePostNotify2 = 95
    swAssemblyComponentStateChangeNotify3 = 96
    swAssemblyRenameDisplayTitleNotify = 97
    swAssemblyActiveAnnotationViewChangeNotify = 98
    swAssemblyDisplayPaneExpandNotify = 99
    swAssemblyDisplayPaneCollapseNotify = 100
    swAssemblyLargeDesignReviewStateChangeNotify = 101
    swAssemblySolidBodyFolderReorderNotify = 102
    swAssemblyAddDependencyNotify = 103
    swAssemblyDeleteDependencyNotify = 104

class swAssemblyUpdateToolboxComponentStatus_e(IntEnum):
    """swAssemblyUpdateToolboxComponentStatus_e (3 constants, from SwConst)."""
    swAssemblyUpdateToolboxComponentStatus_Success = 0
    swAssemblyUpdateToolboxComponentStatus_Failed = 1
    swAssemblyUpdateToolboxComponentStatus_ToolboxNotRegistered = 2

class swAssociatedEntityStates_e(IntEnum):
    """swAssociatedEntityStates_e (4 constants, from SwConst)."""
    swIsEntityInvalid = 0
    swIsEntitySuppressed = 1
    swIsEntityAmbiguous = 2
    swIsEntityDeleted = 3

class swAttachAnnotationOption_e(IntEnum):
    """swAttachAnnotationOption_e (2 constants, from SwConst)."""
    swAttachAnnotationOption_Sheet = 1
    swAttachAnnotationOption_View = 2

class swAttributeCallbackOptions_e(IntEnum):
    """swAttributeCallbackOptions_e (1 constants, from SwConst)."""
    swACBRequiresCallback = 1

class swAttributeCallbackReturnValues_e(IntEnum):
    """swAttributeCallbackReturnValues_e (1 constants, from SwConst)."""
    swACBDeleteIt = 1

class swAttributeCallbackTypes_e(IntEnum):
    """swAttributeCallbackTypes_e (1 constants, from SwConst)."""
    swACBDelete = 0

class swAutoHideShowResponse_e(IntEnum):
    """swAutoHideShowResponse_e (3 constants, from SwConst)."""
    swAutoHideShowResponse_Automatic = 1
    swAutoHideShowResponse_Hide = 2
    swAutoHideShowResponse_Show = 3

class swAutoInsertCenterMarkTypes_e(IntEnum):
    """swAutoInsertCenterMarkTypes_e (3 constants, from SwConst)."""
    swAutoInsertCenterMarkType_Hole = 1
    swAutoInsertCenterMarkType_Fillets = 2
    swAutoInsertCenterMarkType_Slots = 4

class swAutoMateRepairErrors_e(IntEnum):
    """swAutoMateRepairErrors_e (6 constants, from SwConst)."""
    swAutoMateRepairErrors_Unknown = -1
    swAutoMateRepairErrors_Success = 0
    swAutoMateRepairErrors_PartialSuccess = 1
    swAutoMateRepairErrors_NoSelection = 2
    swAutoMateRepairErrors_InvalidSelection = 3
    swAutoMateRepairErrors_Failed = 4

class swAutoRouteAutoTangencyMode_e(IntEnum):
    """swAutoRouteAutoTangencyMode_e (2 constants, from SWRoutingLib)."""
    swAutoTangencyMode_OFF = 0
    swAutoTangencyMode_ON = 1

class swAutoRouteConversionMode_e(IntEnum):
    """swAutoRouteConversionMode_e (2 constants, from SWRoutingLib)."""
    swFlexibleAutoRouteMode = 1
    swOrthogonalAutoRouteMode = 2

class swAutoRouteErrorType_e(IntEnum):
    """swAutoRouteErrorType_e (3 constants, from SWRoutingLib)."""
    swAutoRouteSuccess = 0
    swAutoRouteEntityTypeAndEntityIdMismatch = 1
    swAutoRouteFailed = 2

class swAutoRouteSketchEntitiesTypes_e(IntEnum):
    """swAutoRouteSketchEntitiesTypes_e (4 constants, from SWRoutingLib)."""
    swAutoRouteSketchEntitiesType_Point = 0
    swAutoRouteSketchEntitiesType_Line = 1
    swAutoRouteSketchEntitiesType_Arc = 2
    swAutoRouteSketchEntitiesType_Spline = 3

class swAutoSaveIntervalMode_e(IntEnum):
    """swAutoSaveIntervalMode_e (2 constants, from SwConst)."""
    swAutoSaveIntervalMode_Changes = 1
    swAutoSaveIntervalMode_Minutes = 2

class swAutodimEntities_e(IntEnum):
    """swAutodimEntities_e (3 constants, from SwConst)."""
    swAutodimEntitiesBasedOnPreselect = 0
    swAutodimEntitiesAll = 1
    swAutodimEntitiesSelected = 2

class swAutodimHorizontalPlacement_e(IntEnum):
    """swAutodimHorizontalPlacement_e (2 constants, from SwConst)."""
    swAutodimHorizontalPlacementBelow = -1
    swAutodimHorizontalPlacementAbove = 1

class swAutodimMark_e(IntEnum):
    """swAutodimMark_e (4 constants, from SwConst)."""
    swAutodimMarkEntities = 1
    swAutodimMarkHorizontalDatum = 2
    swAutodimMarkVerticalDatum = 4
    swAutodimMarkOriginDatum = 8

class swAutodimScheme_e(IntEnum):
    """swAutodimScheme_e (4 constants, from SwConst)."""
    swAutodimSchemeBaseline = 1
    swAutodimSchemeOrdinate = 2
    swAutodimSchemeChain = 3
    swAutodimSchemeCenterline = 4

class swAutodimStatus_e(IntEnum):
    """swAutodimStatus_e (19 constants, from SwConst)."""
    swAutodimStatusSuccess = 0
    swAutodimStatusBadOptionValue = 1
    swAutodimStatusNoActiveDoc = 2
    swAutodimStatusDocTypeNotSupported = 3
    swAutodimStatusNoActiveSketch = 4
    swAutodimStatus3DSketchNotSupported = 5
    swAutodimStatusSketchIsEmpty = 6
    swAutodimStatusSketchIsOverDefined = 7
    swAutodimStatusNoEntities = 8
    swAutodimStatusEntitiesNotValid = 9
    swAutodimStatusCenterlineNotAllowed = 10
    swAutodimStatusDatumNotSupplied = 11
    swAutodimStatusDatumNotUnique = 12
    swAutodimStatusDatumNotValidType = 13
    swAutodimStatusDatumLineNotCenterline = 14
    swAutodimStatusDatumLineNotVertical = 15
    swAutodimStatusDatumLineNotHorizontal = 16
    swAutodimStatusAlgorithmFailed = 17
    swAutodimStatusSketchNoSolutionFound = 18

class swAutodimVerticalPlacement_e(IntEnum):
    """swAutodimVerticalPlacement_e (2 constants, from SwConst)."""
    swAutodimVerticalPlacementLeft = -1
    swAutodimVerticalPlacementRight = 1

class swBBoxDescriptionApplyMethod_e(IntEnum):
    """swBBoxDescriptionApplyMethod_e (2 constants, from SwConst)."""
    swBBoxDescriptionApplyMethod_New = 0
    swBBoxDescriptionApplyMethod_ExistingAndNew = 1

class swBOMConfigurationAnchorType_e(IntEnum):
    """swBOMConfigurationAnchorType_e (4 constants, from SwConst)."""
    swBOMConfigurationAnchor_TopLeft = 1
    swBOMConfigurationAnchor_TopRight = 2
    swBOMConfigurationAnchor_BottomLeft = 3
    swBOMConfigurationAnchor_BottomRight = 4

class swBOMConfigurationCreationErrors_e(IntEnum):
    """swBOMConfigurationCreationErrors_e (7 constants, from SwConst)."""
    swBOMTableCreation_Okay = 0
    swBOMTableCreation_UnspecifiedError = -1
    swBOMTableCreation_MustBeDrawingView = -2
    swBOMTableCreation_AlreadyExists = -3
    swBOMTableCreation_ExcelDisabled = -4
    swBOMTableCreation_Failed = -5
    swBOMTableCreation_NoModelForView = -6

class swBOMConfigurationWhatToShow_e(IntEnum):
    """swBOMConfigurationWhatToShow_e (3 constants, from SwConst)."""
    swBOMConfiguration_ShowPartsOnly = 1
    swBOMConfiguration_ShowPartsAndTopLevelAsm = 2
    swBOMConfiguration_ShowAllInIndentedList = 3

class swBOMControlMissingRowDisplay_e(IntEnum):
    """swBOMControlMissingRowDisplay_e (3 constants, from SwConst)."""
    swBOMControlShowMissingRow = 1
    swBOMControlHideMissingRow = 2
    swBOMControlStrikeMissingRow = 3

class swBOMControlSplitDirection_e(IntEnum):
    """swBOMControlSplitDirection_e (2 constants, from SwConst)."""
    swBOMControlSplitRight = 1
    swBOMControlSplitLeft = 2

class swBOMPartNumberSource_e(IntEnum):
    """swBOMPartNumberSource_e (4 constants, from SwConst)."""
    swBOMPartNumber_DocumentName = 1
    swBOMPartNumber_ConfigurationName = 2
    swBOMPartNumber_ParentName = 4
    swBOMPartNumber_UserSpecified = 8

class swBOMTableObjectType_e(IntEnum):
    """swBOMTableObjectType_e (2 constants, from SwConst)."""
    swBOMTableObjectType_RowIndex = 1
    swBOMTableObjectType_CutList = 2

class swBackgroundProcessOption_e(IntEnum):
    """swBackgroundProcessOption_e (3 constants, from SwConst)."""
    swBackgroundProcessing_Disabled = 0
    swBackgroundProcessing_Enabled = 1
    swBackgroundProcessing_DeferToApplication = 2

class swBalloonFit_e(IntEnum):
    """swBalloonFit_e (7 constants, from SwConst)."""
    swBF_Tightest = 0
    swBF_1Char = 1
    swBF_2Chars = 2
    swBF_3Chars = 3
    swBF_4Chars = 4
    swBF_5Chars = 5
    swBF_UserDef = 6

class swBalloonItemNumbersOrder_e(IntEnum):
    """swBalloonItemNumbersOrder_e (4 constants, from SwConst)."""
    swBalloonItemNumbers_DoNotChangeItemNumbers = 1
    swBalloonItemNumbers_FollowAssemblyOrder = 2
    swBalloonItemNumbers_OrderSequentially = 4
    swBalloonItemNumbers_NotApplicable = 4096

class swBalloonLayoutType_e(IntEnum):
    """swBalloonLayoutType_e (6 constants, from SwConst)."""
    swDetailingBalloonLayout_Square = 1
    swDetailingBalloonLayout_Circle = 2
    swDetailingBalloonLayout_Top = 3
    swDetailingBalloonLayout_Bottom = 4
    swDetailingBalloonLayout_Right = 5
    swDetailingBalloonLayout_Left = 6

class swBalloonQuantityPlacement_e(IntEnum):
    """swBalloonQuantityPlacement_e (5 constants, from SwConst)."""
    swBalloonQuantityPlacement_Left = 0
    swBalloonQuantityPlacement_Right = 1
    swBalloonQuantityPlacement_Top = 2
    swBalloonQuantityPlacement_Bottom = 3
    swBalloonQuantityPlacement_NotApplicable = -1

class swBalloonStyle_e(IntEnum):
    """swBalloonStyle_e (21 constants, from SwConst)."""
    swBS_None = 0
    swBS_Circular = 1
    swBS_Triangle = 2
    swBS_Hexagon = 3
    swBS_Box = 4
    swBS_Diamond = 5
    swBS_Pentagon = 6
    swBS_SplitCirc = 7
    swBS_FlagPentagon = 8
    swBS_FlagTriangle = 9
    swBS_Underline = 10
    swBS_Square = 11
    swBS_SCircle = 12
    swBS_Inspection = 13
    swBS_ArcBracket = 14
    swBS_RectBracket = 15
    swBS_ArclenSym = 16
    swBS_FixedSym = 17
    swBS_DoubleArrow = 18
    swBS_SplitSquare = 19
    swBS_Verbose = 20

class swBalloonTextContent_e(IntEnum):
    """swBalloonTextContent_e (13 constants, from SwConst)."""
    swBalloonTextCustom = 0
    swBalloonTextItemNumber = 1
    swBalloonTextQuantity = 2
    swBalloonTextCustomProperties = 3
    swBalloonTextComponentReference = 4
    swBalloonTextSpoolReference = 5
    swBalloonTextPartNumberBOM = 6
    swBalloonTextFileName = 7
    swBalloonTextCutlistProperties = 8
    swBalloonTextViewSheet = 9
    swBalloonTextViewSheetWithLabel = 10
    swBalloonTextViewZone = 11
    swBalloonTextViewViewLetter = 12

class swBasicDimType_e(IntEnum):
    """swBasicDimType_e (3 constants, from SwConst)."""
    swBasicDimType_Chain = 0
    swBasicDimType_Baseline = 1
    swBasicDimType_Polar = 2

class swBendAllowanceTypes_e(IntEnum):
    """swBendAllowanceTypes_e (6 constants, from SwConst)."""
    swBendAllowanceBendTable = 1
    swBendAllowanceKFactor = 2
    swBendAllowanceDirect = 3
    swBendAllowanceDeduction = 4
    swBendAllowanceBendCalculationTable = 5
    swBendAllowanceGaugeTable = 6

class swBendDirection_e(IntEnum):
    """swBendDirection_e (3 constants, from SwConst)."""
    swBendDirection_ERROR = 0
    swBendDirection_UP = 1
    swBendDirection_DOWN = 2

class swBendLineControlOption_e(IntEnum):
    """swBendLineControlOption_e (2 constants, from SwConst)."""
    swBendLineControl_NumberOfBendLine = 0
    swBendLineControl_MaximumDeviation = 1

class swBendLineDirection_e(IntEnum):
    """swBendLineDirection_e (3 constants, from SwConst)."""
    swNotBendLine = 0
    swUpDirection = 1
    swDownDirection = 2

class swBendNoteAttribute_e(IntEnum):
    """swBendNoteAttribute_e (6 constants, from SwConst)."""
    swBendNoteAttribute_BendDirection = 1
    swBendNoteAttribute_SupplementaryAngle = 2
    swBendNoteAttribute_ComplementaryAngle = 3
    swBendNoteAttribute_BendRadius = 4
    swBendNoteAttribute_BendOrder = 5
    swBendNoteAttribute_BendAllowance = 6

class swBendNoteStyle_e(IntEnum):
    """swBendNoteStyle_e (3 constants, from SwConst)."""
    swAboveBendLine = 0
    swBelowBendLine = 1
    swWithLeader = 2

class swBendTableTagStyle_e(IntEnum):
    """swBendTableTagStyle_e (2 constants, from SwConst)."""
    swBendTable_AlphaNumericTags = 1
    swBendTable_NumericTags = 2

class swBendType_e(IntEnum):
    """swBendType_e (13 constants, from SwConst)."""
    swSharpBend = 0
    swRoundBend = 1
    swFlatBend = 2
    swNoneBend = 3
    swBaseBend = 4
    swMiterBend = 5
    swFlat3dBend = 6
    swMirrorBend = 7
    swEdgeFlangeBend = 8
    swHemBend = 9
    swFreeFormBend = 10
    swRuledBend = 11
    swLoftedBend = 12

class swBitMaps(IntEnum):
    """swBitMaps (3 constants, from SwConst)."""
    swBitMapNone = 0
    swBitMapUserDefined = 1
    swBitMapTreeError = 2

class swBitmapControlStandardTypes_e(IntEnum):
    """swBitmapControlStandardTypes_e (1 constants, from SwConst)."""
    swBitmapControl_Volume = 1

class swBlockDefinitionExtFileStatus_e(IntEnum):
    """swBlockDefinitionExtFileStatus_e (5 constants, from SwConst)."""
    swBlockDefinitionExtFile_Failed = -1
    swBlockDefinitionExtFile_Success = 0
    swBlockDefinitionExtFile_NotLinked = 1
    swBlockDefinitionExtFile_MissingReference = 2
    swBlockDefinitionExtFile_OutOfDateReference = 3

class swBlockInstanceTextDisplay_e(IntEnum):
    """swBlockInstanceTextDisplay_e (3 constants, from SwConst)."""
    swBlockInstanceTextDisplayNone = 1
    swBlockInstanceTextDisplayAll = 2
    swBlockInstanceTextDisplayNormal = 3

class swBlockingStates_e(IntEnum):
    """swBlockingStates_e (9 constants, from SwConst)."""
    swNoBlock = 0
    swFullBlock = 1
    swModifyBlock = 2
    swPartialModifyBlock = 3
    swEditorBlock = 4
    swEditSketchBlock = 5
    swSystemBlock = 6
    swViewOnlyBlock = 7
    swEditSketchAllowExitBlock = 8

class swBodyFolderFeatureType_e(IntEnum):
    """swBodyFolderFeatureType_e (5 constants, from SwConst)."""
    swSolidBodyFolder = 1
    swSurfaceBodyFolder = 2
    swBodySubFolder = 3
    swWeldmentSubFolder = 4
    swWeldmentCutListFolder = 5

class swBodyInfo_e(IntEnum):
    """swBodyInfo_e (2 constants, from SwConst)."""
    swUserBody_e = 0
    swNormalBody_e = 1

class swBodyMaterialApplicationError_e(IntEnum):
    """swBodyMaterialApplicationError_e (7 constants, from SwConst)."""
    swBodyMaterialApplicationError_UnknownError = -1
    swBodyMaterialApplicationError_NoError = 1
    swBodyMaterialApplicationError_ReadOnly = 2
    swBodyMaterialApplicationError_ExternalReference = 3
    swBodyMaterialApplicationError_RolledBackState = 4
    swBodyMaterialApplicationError_InvalidConfigName = 5
    swBodyMaterialApplicationError_InvalidMaterialNameOrDbName = 6

class swBodyOperationError_e(IntEnum):
    """swBodyOperationError_e (19 constants, from SwConst)."""
    swBodyOperationUnknownError = -1
    swBodyOperationNoError = 0
    swBodyOperationNonApiBody = 1
    swBodyOperationWrongType = 2
    swBodyOperationBooleanFail = 1058
    swBodyOperationNoIntersect = 1067
    swBodyOperationNonManifold = 547
    swBodyOperationPartialCoincidence = 1040
    swBodyOperationIntersectSolidWithSheets = 972
    swBodyOperationUniteSolidSheet = 543
    swBodyOperationMissingGeom = 96
    swBodyOperationSameToolAndTarget = 545
    swBodyOperationFailGeomCondition = 3
    swBodyOperationFailToCutBody = 4
    swBodyOperationDisjointBodies = 5
    swBodyOperationEmptyBody = 6
    swBodyOperationEmptyInputBody = 7
    swBodyOperationInvalidInputBody = 8
    swBodyOperationOpposedSheets = 951

class swBodyOperationType_e(IntEnum):
    """swBodyOperationType_e (3 constants, from SwConst)."""
    SWBODYINTERSECT = 15901
    SWBODYCUT = 15902
    SWBODYADD = 15903

class swBodyType_e(IntEnum):
    """swBodyType_e (9 constants, from SwConst)."""
    swAllBodies = -1
    swSolidBody = 0
    swSheetBody = 1
    swWireBody = 2
    swMinimumBody = 3
    swGeneralBody = 4
    swEmptyBody = 5
    swMeshBody = 6
    swGraphicsBody = 7

class swBomTableSortItemGroup_e(IntEnum):
    """swBomTableSortItemGroup_e (4 constants, from SwConst)."""
    swBomTableSortItemGroup_None = 0
    swBomTableSortItemGroup_Assemblies = 1
    swBomTableSortItemGroup_Parts = 2
    swBomTableSortItemGroup_Other = 3

class swBomTableSortMethod_e(IntEnum):
    """swBomTableSortMethod_e (2 constants, from SwConst)."""
    swBomTableSortMethod_Literal = 0
    swBomTableSortMethod_Numeric = 1

class swBomType_e(IntEnum):
    """swBomType_e (4 constants, from SwConst)."""
    swBomType_PartsOnly = 1
    swBomType_TopLevelOnly = 2
    swBomType_Indented = 3
    swBomType_Flattened = 4

class swBoundType_e(IntEnum):
    """swBoundType_e (6 constants, from SwConst)."""
    swBoundType_Infinite = 13733
    swBoundType_Extendable = 13734
    swBoundType_NotExtendable = 13735
    swBoundType_Periodic = 13701
    swBoundType_PeriodicNotDifferentiable = 13736
    swBoundType_Degenerate = 13741

class swBoundaryBossAlignment_e(IntEnum):
    """swBoundaryBossAlignment_e (4 constants, from SwConst)."""
    swAlignWithSectionNormal = 0
    swAlignWithNextSection = 1
    swAlignWithOtherGeometry = 2
    swAlignWithIsoParameter = 3

class swBoundaryBossCurveInfluenceType_e(IntEnum):
    """swBoundaryBossCurveInfluenceType_e (5 constants, from SwConst)."""
    swBoundaryBossCurve_ToNextCurveInfluence = 0
    swBoundaryBossCurve_ToNextSharpInfluence = 16
    swBoundaryBossCurve_GlobalInfluence = 32
    swBoundaryBossCurve_ToEdgeInfluence = 64
    swBoundaryBossCurve_LinearInfluence = 144

class swBoundaryBossDirection_e(IntEnum):
    """swBoundaryBossDirection_e (3 constants, from SwConst)."""
    swBoundaryBossDirection_First = 0
    swBoundaryBossDirection_Second = 1
    swBoundaryBossDirection_Both = 2

class swBoundaryBossTangencyType_e(IntEnum):
    """swBoundaryBossTangencyType_e (6 constants, from SwConst)."""
    swBoundaryBossTangency_None = 0
    swBoundaryBossTangency_NormalToProfile = 1
    swBoundaryBossTangency_DirectionVector = 2
    swBoundaryBossTangency_TangencyToFace = 3
    swBoundaryBossTangency_CurvatureToFace = 4
    swBoundaryBossTangency_Default = 6

class swBoundingBoxOptions_e(IntEnum):
    """swBoundingBoxOptions_e (2 constants, from SwConst)."""
    swBoundingBoxIncludeRefPlanes = 1
    swBoundingBoxIncludeSketches = 2

class swBreakCornerTypes_e(IntEnum):
    """swBreakCornerTypes_e (2 constants, from SwConst)."""
    swBreakCornerTypeFillet = 0
    swBreakCornerTypeChamfer = 1

class swBreakLineOrientation_e(IntEnum):
    """swBreakLineOrientation_e (2 constants, from SwConst)."""
    swBreakLineHorizontal = 1
    swBreakLineVertical = 2

class swBreakLineStyle_e(IntEnum):
    """swBreakLineStyle_e (5 constants, from SwConst)."""
    swBreakLine_Straight = 1
    swBreakLine_ZigZag = 2
    swBreakLine_Curve = 3
    swBreakLine_SmallZigZag = 4
    swBreakLine_Jagged = 5

class swButtonSize_e(IntEnum):
    """swButtonSize_e (3 constants, from SwConst)."""
    swButtonSize_Small = 0
    swButtonSize_Medium = 1
    swButtonSize_Large = 2

class swCADFamilyCfgOptions_e(IntEnum):
    """swCADFamilyCfgOptions_e (3 constants, from SwConst)."""
    swCADFamilyCfgOption_SuppressNewFeatures = 1
    swCADFamilyCfgOption_SuppressNewComponents = 2
    swCADFamilyCfgOption_DontActivate = 4

class swCPointConfig_e(IntEnum):
    """swCPointConfig_e (3 constants, from SWRoutingLib)."""
    swCPointConfig_AddAllCPoint = 1
    swCPointConfig_DoNotAddCPoint = 2
    swCPointConfig_SelectCPoints = 3

class swCalloutTargetStyle_e(IntEnum):
    """swCalloutTargetStyle_e (5 constants, from SwConst)."""
    swCalloutTargetStyle_None = 0
    swCalloutTargetStyle_Square = 1
    swCalloutTargetStyle_Circle = 2
    swCalloutTargetStyle_Triangle = 3
    swCalloutTargetStyle_Arrow = 4

class swCalloutVariableType_e(IntEnum):
    """swCalloutVariableType_e (3 constants, from SwConst)."""
    swCalloutVariableType_Length = 1
    swCalloutVariableType_Angle = 2
    swCalloutVariableType_String = 3

class swCalloutVariable_e(IntEnum):
    """swCalloutVariable_e (90 constants, from SwConst)."""
    swCalloutVariable_Standard = 4
    swCalloutVariable_Fastener_Type = 5
    swCalloutVariable_Fastener_Size = 6
    swCalloutVariable_Counterbore_Depth = 7
    swCalloutVariable_Counterbore_Diameter = 8
    swCalloutVariable_Counterdrill_Angle = 9
    swCalloutVariable_Counterdrill_Depth = 10
    swCalloutVariable_Counterdrill_Diameter = 11
    swCalloutVariable_Countersink_Angle = 12
    swCalloutVariable_Countersink_Diameter = 13
    swCalloutVariable_Depth = 14
    swCalloutVariable_Diameter = 15
    swCalloutVariable_Drill_Angle = 16
    swCalloutVariable_Far_Side_Countersink_Angle = 17
    swCalloutVariable_Far_Side_Countersink_Diameter = 18
    swCalloutVariable_Head_Clearance = 19
    swCalloutVariable_Hole_Diameter = 20
    swCalloutVariable_Hole_Depth = 21
    swCalloutVariable_Major_Diameter = 22
    swCalloutVariable_Middle_Countersink_Angle = 23
    swCalloutVariable_Middle_Countersink_Diameter = 24
    swCalloutVariable_Minor_Diameter = 25
    swCalloutVariable_Near_Side_Countersink_Angle = 26
    swCalloutVariable_Near_Side_Countersink_Diameter = 27
    swCalloutVariable_Tap_Drill_Depth = 28
    swCalloutVariable_Tap_Drill_Diameter = 29
    swCalloutVariable_Thread_Angle = 30
    swCalloutVariable_Thread_Diameter = 31
    swCalloutVariable_Thread_Depth = 32
    swCalloutVariable_Thru_Hole_Depth = 33
    swCalloutVariable_Thru_Hole_Diameter = 34
    swCalloutVariable_Thru_Tap_Depth = 35
    swCalloutVariable_Thru_Tap_Drill_Diameter = 36
    swCalloutVariable_Description = 37
    swCalloutVariable_Msg_Near_Side = 38
    swCalloutVariable_Msg_Mid_Side = 39
    swCalloutVariable_Msg_Far_Side = 40
    swCalloutVariable_Thread_Description = 41
    swCalloutVariable_Thread_Size = 42
    swCalloutVariable_Thread_Series = 43
    swCalloutVariable_Thru = 44
    swCalloutVariable_NUM_INST = 45
    swCalloutVariable_Thread_Class = 46
    swCalloutVariable_Counterbore = 47
    swCalloutVariable_Thread_Diameter_Only = 48
    swCalloutVariable_Slot_Length = 49
    swCalloutVariable_Slot_Width = 50
    swCalloutVariable_AH_Counterbore_Diameter = 51
    swCalloutVariable_AH_Counterbore_Depth = 52
    swCalloutVariable_AH_Counterbore_Nearside_Msg = 53
    swCalloutVariable_AH_Counterbore_Farside_Msg = 54
    swCalloutVariable_AH_Counterbore_Side = 55
    swCalloutVariable_AH_Countersink_Diameter = 56
    swCalloutVariable_AH_Countersink_Angle = 57
    swCalloutVariable_AH_Countersink_Depth = 58
    swCalloutVariable_AH_Countersink_Nearside_Msg = 59
    swCalloutVariable_AH_Countersink_Farside_Msg = 60
    swCalloutVariable_AH_Countersink_Side = 61
    swCalloutVariable_AH_StraightThread_Tap_Drill_Diameter = 62
    swCalloutVariable_AH_StraightThread_Major_Diameter = 63
    swCalloutVariable_AH_StraightThread_Size = 64
    swCalloutVariable_AH_StraightThread_Depth = 65
    swCalloutVariable_AH_StraightThread_Nearside_Msg = 66
    swCalloutVariable_AH_StraightThread_Farside_Msg = 67
    swCalloutVariable_AH_StraightThread_Side = 68
    swCalloutVariable_AH_TaperedThread_Tap_Drill_Diameter = 69
    swCalloutVariable_AH_TaperedThread_Major_Diameter = 70
    swCalloutVariable_AH_TaperedThread_Depth = 71
    swCalloutVariable_AH_TaperedThread_Size = 72
    swCalloutVariable_AH_TaperedThread_Nearside_Msg = 73
    swCalloutVariable_AH_TaperedThread_Farside_Msg = 74
    swCalloutVariable_AH_TaperedThread_Side = 75
    swCalloutVariable_AH_Straight_Diameter = 76
    swCalloutVariable_AH_Straight_Depth = 77
    swCalloutVariable_AH_Dowel_HoleFit = 78
    swCalloutVariable_AH_Dowel_ShaftFit = 79
    swCalloutVariable_AH_Straight_Nearside_Msg = 80
    swCalloutVariable_AH_Straight_Farside_Msg = 81
    swCalloutVariable_AH_Straight_Side = 82
    swCalloutVariable_AH_DrillPoint_Angle = 83
    swCalloutVariable_AH_DrillPoint_Msg = 84
    swCalloutVariable_AH_FlatBottom_Msg = 85
    swCalloutVariable_AH_Blind_Msg = 86
    swCalloutVariable_AH_UptoNext_Msg = 87
    swCalloutVariable_AH_UptoNextElement_Msg = 88
    swCalloutVariable_AH_UptoSelection_Msg = 89
    swCalloutVariable_AH_OffsetFromSurface_Msg = 90
    swCalloutVariable_AH_ThroughAll_Msg = 91
    swCalloutVariable_AH_Thread_Description = 92
    swCalloutVariable_AH_ThreadAdvance = 93

class swCamMateEntityType_e(IntEnum):
    """swCamMateEntityType_e (2 constants, from SwConst)."""
    swCamMateEntityType_CamPath = 0
    swCamMateEntityType_CamFollower = 1

class swCameraPositionType_e(IntEnum):
    """swCameraPositionType_e (2 constants, from SwConst)."""
    swCameraPosition_Cartesian = 1
    swCameraPosition_Spherical = 2

class swCameraType_e(IntEnum):
    """swCameraType_e (2 constants, from SwConst)."""
    swCameraType_AimedAtTarget = 1
    swCameraType_Floating = 2

class swCavityScaleType_e(IntEnum):
    """swCavityScaleType_e (4 constants, from SwConst)."""
    swAboutCentroid = 0
    swAboutOrigin = 1
    swAboutMoldBaseOrigin = 2
    swAboutCoordinateSystem = 3

class swCellEquationStatus_e(IntEnum):
    """swCellEquationStatus_e (3 constants, from SwConst)."""
    swCellEquationStatus_Success = 0
    swCellEquationStatus_InvalidIndex = 1
    swCellEquationStatus_InvalidEquation = 2

class swCenterLineMarkOrient_e(IntEnum):
    """swCenterLineMarkOrient_e (2 constants, from SwConst)."""
    swCenterLineMarkOrientToSlot = 0
    swCenterLineMarkOrientToSheet = 1

class swCenterMarkConnectionLine_e(IntEnum):
    """swCenterMarkConnectionLine_e (5 constants, from SwConst)."""
    swCenterMark_ShowNoConnectLines = 0
    swCenterMark_ShowLinearConnectLines = 1
    swCenterMark_ShowCircularConnectLines = 2
    swCenterMark_ShowRadialConnectLines = 4
    swCenterMark_ShowBaseCenterMarkLines = 8

class swCenterMarkHandle_e(IntEnum):
    """swCenterMarkHandle_e (4 constants, from SwConst)."""
    swCenterMarkHandle_Up = 0
    swCenterMarkHandle_Left = 1
    swCenterMarkHandle_Down = 2
    swCenterMarkHandle_Right = 3

class swCenterMarkStyle_e(IntEnum):
    """swCenterMarkStyle_e (4 constants, from SwConst)."""
    swCenterMark_NonAnnotation = 1
    swCenterMark_Single = 2
    swCenterMark_LinearGroup = 3
    swCenterMark_CircularGroup = 4

class swChainPatternAlignment_e(IntEnum):
    """swChainPatternAlignment_e (2 constants, from SwConst)."""
    swChainPatternAlignToSeed = 0
    swChainPatternTangentToCurve = 1

class swChainPatternOptions_e(IntEnum):
    """swChainPatternOptions_e (2 constants, from SwConst)."""
    swChainPatternStatic = 0
    swChainPatternDynamic = 1

class swChainPatternPitchMethod_e(IntEnum):
    """swChainPatternPitchMethod_e (3 constants, from SwConst)."""
    swChainPatternDistance = 0
    swChainPatternDistanceLinkage = 1
    swChainPatternConnectedLinkage = 2

class swChamferType_e(IntEnum):
    """swChamferType_e (4 constants, from SwConst)."""
    swChamferAngleDistance = 1
    swChamferDistanceDistance = 2
    swChamferVertex = 3
    swChamferEqualDistance = 16

class swCheckClearanceBetween_e(IntEnum):
    """swCheckClearanceBetween_e (2 constants, from SwConst)."""
    swCheckClearanceBetweenSelectedItems = 0
    swCheckClearanceBetweenSelectedItemsAndRestAssembly = 1

class swCheckInterferenceOption_e(IntEnum):
    """swCheckInterferenceOption_e (3 constants, from SwConst)."""
    swBodyInterference_OptionDefault = 1
    swBodyInterference_IncludeCoincidentFaces = 2
    swBodyInterference_ReturnInterferingObject = 4

class swCheckOutOfDate_e(IntEnum):
    """swCheckOutOfDate_e (3 constants, from SwConst)."""
    swCheckOutOfDate_DoNotCheck = 0
    swCheckOutOfDate_Indicate = 1
    swCheckOutOfDate_AlwaysResolve = 2

class swCheckSpellingOptions_e(IntEnum):
    """swCheckSpellingOptions_e (6 constants, from SwConst)."""
    swSpellingIgnoreUpperCase = 1
    swSpellingIgnoreMixedCase = 2
    swSpellingIgnoreWordsWithNumbers = 4
    swSpellingIgnoreCapitalizedWords = 8
    swSpellingIgnoreInternetAndFiles = 16
    swSpellingLeaveEngineRunning = 32

class swChildComponentInBOMOption_e(IntEnum):
    """swChildComponentInBOMOption_e (3 constants, from SwConst)."""
    swChildComponent_Hide = 1
    swChildComponent_Show = 2
    swChildComponent_Promote = 3

class swClearanceType_e(IntEnum):
    """swClearanceType_e (2 constants, from SwConst)."""
    swClearanceType_Distance = 0
    swClearanceType_Coincident = 1

class swClearanceVerificationSetEntityErrors_e(IntEnum):
    """swClearanceVerificationSetEntityErrors_e (7 constants, from SwConst)."""
    swClearanceVerification_Unknown = -1
    swClearanceVerification_swSuccess = 0
    swClearanceVerification_swFacesAlreadySelected = 1
    swClearanceVerification_swComponentAlreadySelected = 2
    swClearanceVerification_swInvalidComponent = 3
    swClearanceVerification_swInvalidFace = 4
    swClearanceVerification_swInsufficientEntities = 5

class swCloseReopenError_e(IntEnum):
    """swCloseReopenError_e (15 constants, from SwConst)."""
    swCloseReopenNoError = 0
    swCloseReopenUnknownError = 1
    swCloseReopenNoInputDocError = 2
    swCloseReopenOutputDocPointerError = 3
    swCloseReopenInvalidDocError = 4
    swCloseReopenCloseDocError = 5
    swCloseReopenLoadGenericError = 6
    swCloseReopenLoadFileNotFoundError = 7
    swCloseReopenLoadInvalidFileTypeError = 8
    swCloseReopenLoadFutureVersionError = 9
    swCloseReopenLoadSameTitleAlreadyOpenError = 10
    swCloseReopenLoadLiquidMachineDocError = 11
    swCloseReopenModifiedError = 12
    swCloseReopenLoadFilePathEmptyError = 13
    swCloseReopenLoadFilePathNonDrawingError = 14

class swCloseReopenOption_e(IntEnum):
    """swCloseReopenOption_e (4 constants, from SwConst)."""
    swCloseReopenOption_ReadOnly = 1
    swCloseReopenOption_DiscardChanges = 2
    swCloseReopenOption_MatchSheet = 4
    swCloseReopenOption_ExitDetailingMode = 8

class swClosedCornerTypes_e(IntEnum):
    """swClosedCornerTypes_e (3 constants, from SwConst)."""
    swClosedCornerTypeButt = 1
    swClosedCornerTypeOverlap = 2
    swClosedCornerTypeUnderlap = 3

class swCollabCheckReadOnlyModifiedInterval_e(IntEnum):
    """swCollabCheckReadOnlyModifiedInterval_e (10 constants, from SwConst)."""
    swCollabCheckReadOnlyModifiedInterval_1min = 1
    swCollabCheckReadOnlyModifiedInterval_2min = 2
    swCollabCheckReadOnlyModifiedInterval_3min = 3
    swCollabCheckReadOnlyModifiedInterval_5min = 4
    swCollabCheckReadOnlyModifiedInterval_10min = 5
    swCollabCheckReadOnlyModifiedInterval_15min = 6
    swCollabCheckReadOnlyModifiedInterval_20min = 7
    swCollabCheckReadOnlyModifiedInterval_30min = 8
    swCollabCheckReadOnlyModifiedInterval_45min = 9
    swCollabCheckReadOnlyModifiedInterval_60min = 10

class swCollinearChainDimArrowHeadStyle_e(IntEnum):
    """swCollinearChainDimArrowHeadStyle_e (2 constants, from SwConst)."""
    swCollinearChainDimArrowHeadStyle_Point = 0
    swCollinearChainDimArrowHeadStyle_Oblique = 1

class swCollisionDetectionResults_e(IntEnum):
    """swCollisionDetectionResults_e (3 constants, from SwConst)."""
    swCollisionDetectionResult_NoCollision = 0
    swCollisionDetectionResult_CollisionDetected = 1
    swCollisionDetectionResult_FailedNotEnoughGroups = -1

class swCollisionGroupApplyTransformErrors_e(IntEnum):
    """swCollisionGroupApplyTransformErrors_e (4 constants, from SwConst)."""
    swCollisionGroupApplyTransformErrors_None = 0
    swCollisionGroupApplyTransformErrors_SizeMismatch = 1
    swCollisionGroupApplyTransformErrors_InvalidTransforms = 2
    swCollisionGroupApplyTransformErrors_GroupRemoved = 3

class swCollisionGroupSetComponentsErrors_e(IntEnum):
    """swCollisionGroupSetComponentsErrors_e (4 constants, from SwConst)."""
    swCollisionGroupSetComponentsErrors_None = 0
    swCollisionGroupSetComponentsErrors_InvalidComponents = 1
    swCollisionGroupSetComponentsErrors_ComponentsAddedElsewhere = 2
    swCollisionGroupSetComponentsErrors_GroupRemoved = 3

class swCollisionManagerSetAssemblyErrors_e(IntEnum):
    """swCollisionManagerSetAssemblyErrors_e (3 constants, from SwConst)."""
    swCollisionManagerSetAssemblyErrors_Success = 0
    swCollisionManagerSetAssemblyErrors_InvalidModelDocument = 1
    swCollisionManagerSetAssemblyErrors_OtherAssemblyActive = 2

class swColorsBackgroundAppearance_e(IntEnum):
    """swColorsBackgroundAppearance_e (4 constants, from SwConst)."""
    swColorsBackgroundAppearance_Plain = 0
    swColorsBackgroundAppearance_Gradient = 1
    swColorsBackgroundAppearance_Image = 2
    swColorsBackgroundAppearance_DocumentScene = 3

class swColumnTypeStatus_e(IntEnum):
    """swColumnTypeStatus_e (3 constants, from SwConst)."""
    swColumnTypeStatus_Success = 0
    swColumnTypeStatus_InvalidIndex = 1
    swColumnTypeStatus_InvalidPropertyType = 2

class swCombineBodiesOperationType_e(IntEnum):
    """swCombineBodiesOperationType_e (3 constants, from SwConst)."""
    swCombineBodiesOperationAdd = 0
    swCombineBodiesOperationSubtract = 1
    swCombineBodiesOperationCommon = 2

class swCommandFlyoutStyle_e(IntEnum):
    """swCommandFlyoutStyle_e (3 constants, from SwConst)."""
    swCommandFlyoutStyle_Simple = 0
    swCommandFlyoutStyle_Favorite = 1
    swCommandFlyoutStyle_LastUsed = 2

class swCommandItemType_e(IntEnum):
    """swCommandItemType_e (2 constants, from SwConst)."""
    swMenuItem = 1
    swToolbarItem = 2

class swCommandTabButtonFlyoutStyle_e(IntEnum):
    """swCommandTabButtonFlyoutStyle_e (3 constants, from SwConst)."""
    swCommandTabButton_NoFlyout = 8
    swCommandTabButton_SimpleFlyout = 16
    swCommandTabButton_ActionFlyout = 32

class swCommandTabButtonTextDisplay_e(IntEnum):
    """swCommandTabButtonTextDisplay_e (3 constants, from SwConst)."""
    swCommandTabButton_NoText = 1
    swCommandTabButton_TextBelow = 2
    swCommandTabButton_TextHorizontal = 4

class swCommand_e(IntEnum):
    """swCommand_e (12 constants, from SwConst)."""
    swFileOpen = 0
    swFileNew = 1
    swOpenRecentFile = 2
    swOpenHTMLHelp = 3
    swReserved = 4
    swVerticalMkt = 5
    swUserExperienceLevel = 6
    swNextTipOfDayString = 7
    swCurrentTipOfDayString = 8
    swPrevTipOfDayString = 9
    swFontSize = 10
    swInterfaceBrightnessTheme = 11

class swCommands_e(IntEnum):
    """swCommands_e (3525 constants, from SwCommands)."""
    swCommands_NoCommand = -3
    swCommands_PmOK = -2
    swCommands_PmCancel = -1
    swCommands_Open = 0
    swCommands_New = 1
    swCommands_Save = 2
    swCommands_AssemblyTransparency = 3
    swCommands_ShowCurvatureCombs = 4
    swCommands_ClickHereToSeeThePreview = 5
    swCommands_EnterTheOffsetOfTheSupportArea = 6
    swCommands_SmartFasteners = 7
    swCommands_ExtrudedBossBase = 8
    swCommands_Fillet = 9
    swCommands_ExtrudedCut = 10
    swCommands_Chamfer = 11
    swCommands_SimpleHole = 12
    swCommands_InsertComponents = 13
    swCommands_Suppress = 14
    swCommands_Unsuppress = 15
    swCommands_Delete = 16
    swCommands_Rebuild = 17
    swCommands_LinearPattern = 18
    swCommands_SaveAll = 19
    swCommands_MoveComponent = 20
    swCommands_RotateComponent = 21
    swCommands_Axis = 22
    swCommands_InsertPlane = 23
    swCommands_RevolvedBossBase = 24
    swCommands_LoftedBossBase = 25
    swCommands_InsertPart = 26
    swCommands_RelativeView = 27
    swCommands_ProjectedView = 28
    swCommands_RecordPauseMacro = 29
    swCommands_RunMacro = 30
    swCommands_StopMacro = 31
    swCommands_Shell = 32
    swCommands_AuxiliaryView = 33
    swCommands_InsertDrawingviewSection = 34
    swCommands_DetailView = 35
    swCommands_Note = 36
    swCommands_Balloon = 37
    swCommands_SmartDimension = 38
    swCommands_HoleWizard = 39
    swCommands_InsertFaceDraft = 40
    swCommands_GridSnap = 41
    swCommands_Standard3View = 42
    swCommands_Line = 43
    swCommands_CenterpointArc = 44
    swCommands_Sketch = 45
    swCommands_Circle = 46
    swCommands_Spline = 47
    swCommands_RevolvedCut = 48
    swCommands_Centerline = 49
    swCommands_UnsuppressWithDependents = 50
    swCommands_Equations = 51
    swCommands_AutomaticRelations = 52
    swCommands_ConvertEntities = 57
    swCommands_GeometricTolerance = 58
    swCommands_TrimEntities = 59
    swCommands_DisplayDeleteRelations = 60
    swCommands_MirrorEntities = 61
    swCommands_SketchFillet = 62
    swCommands_ExtendEntities = 63
    swCommands_SweptBossBase = 64
    swCommands_SweptCut = 65
    swCommands_HorizontalDimension = 66
    swCommands_HideShowAnnotations = 67
    swCommands_VerticalDimension = 68
    swCommands_TangentArc = 69
    swCommands_FeatureImportDiagnosis = 70
    swCommands_AddRelation = 71
    swCommands_Point = 72
    swCommands_CircularPattern = 73
    swCommands_ProjectCurve = 74
    swCommands_Properties = 75
    swCommands_OffsetEntities = 76
    swCommands_ModelView = 77
    swCommands_ScanEqual = 78
    swCommands_Rectangle = 79
    swCommands_3PointArc = 80
    swCommands_BaselineDimension = 81
    swCommands_LoftedCut = 82
    swCommands_Mirror = 83
    swCommands_EditMacro = 84
    swCommands_HideShowComponents = 85
    swCommands_PartialEllipse = 86
    swCommands_Ellipse = 87
    swCommands_BillOfMaterials = 88
    swCommands_3DSketch = 89
    swCommands_Mate = 90
    swCommands_NewPart = 91
    swCommands_Measure = 92
    swCommands_Cavity = 93
    swCommands_HelixAndSpiral = 94
    swCommands_CenterMark = 95
    swCommands_ImportedGeometry = 96
    swCommands_Thicken = 97
    swCommands_ThickenedCut = 98
    swCommands_ViewTemporaryAxes = 99
    swCommands_ModifySketch = 100
    swCommands_CutWithSurface = 101
    swCommands_ConstructionGeometry = 102
    swCommands_SweptSurface = 103
    swCommands_RevolvedSurface = 104
    swCommands_InsertOffsetRefSurface = 105
    swCommands_ExtrudedSurface = 106
    swCommands_LoftedSurface = 107
    swCommands_AlignedSectionView = 108
    swCommands_Text = 109
    swCommands_VerticalBreak = 110
    swCommands_InsertPartingLine = 111
    swCommands_SurfaceFinish = 112
    swCommands_FileReload = 113
    swCommands_DatumFeature = 114
    swCommands_CosmeticThread = 115
    swCommands_Join = 116
    swCommands_MidSurface = 117
    swCommands_InsertBends = 118
    swCommands_EditComponent = 119
    swCommands_ChangeTransparency = 120
    swCommands_HoleCallout = 121
    swCommands_DatumTarget = 122
    swCommands_CurveThroughReferencePoints = 123
    swCommands_SectionView = 124
    swCommands_Rib = 125
    swCommands_ViewOrigins = 126
    swCommands_CameraView = 127
    swCommands_CurveThroughXYZPoints = 128
    swCommands_StopCurrentJump = 129
    swCommands_OpenInternetAddress = 130
    swCommands_WeldSymbol = 131
    swCommands_Curvature = 132
    swCommands_Check = 133
    swCommands_InsertHyperlink = 134
    swCommands_ExplodedView = 135
    swCommands_WebToolbar = 136
    swCommands_Dome = 137
    swCommands_Flatten = 138
    swCommands_NoBends = 139
    swCommands_InsertSplinePoint = 140
    swCommands_LineColor = 141
    swCommands_LineThickness = 142
    swCommands_LineStyle = 143
    swCommands_SimplifySpline = 144
    swCommands_AlignCollinearRadial = 145
    swCommands_AlignParallelConcentric = 146
    swCommands_Bold = 147
    swCommands_Italic = 148
    swCommands_Underline = 149
    swCommands_ChangeSuppressionState = 150
    swCommands_Parabola = 151
    swCommands_Block = 152
    swCommands_ViewCoordinateSystems = 153
    swCommands_CoordinateSystem = 154
    swCommands_InsertRefsurfaceRadiate = 155
    swCommands_InsertRefsurfaceSew = 156
    swCommands_Shape = 157
    swCommands_CompositeCurve = 158
    swCommands_PreviousView = 159
    swCommands_MateReference = 160
    swCommands_Front = 161
    swCommands_Back = 162
    swCommands_Top = 163
    swCommands_Left = 164
    swCommands_Right = 165
    swCommands_Bottom = 166
    swCommands_Isometric = 167
    swCommands_InsertPlanarSurface = 168
    swCommands_NormalTo = 169
    swCommands_EditColor = 170
    swCommands_NoSolveMove = 171
    swCommands_LinearSketchPattern = 172
    swCommands_CircularSketchPattern = 173
    swCommands_UserMacro01 = 174
    swCommands_UserMacro02 = 175
    swCommands_UserMacro03 = 176
    swCommands_UserMacro04 = 177
    swCommands_UserMacro05 = 178
    swCommands_UserMacro06 = 179
    swCommands_UserMacro07 = 180
    swCommands_UserMacro08 = 181
    swCommands_UserMacro09 = 182
    swCommands_UserMacro10 = 183
    swCommands_UserMacro11 = 184
    swCommands_UserMacro12 = 185
    swCommands_UserMacro13 = 186
    swCommands_UserMacro14 = 187
    swCommands_UserMacro15 = 188
    swCommands_UserMacro16 = 189
    swCommands_UserMacro17 = 190
    swCommands_UserMacro18 = 191
    swCommands_UserMacro19 = 192
    swCommands_UserMacro20 = 193
    swCommands_UserMacro21 = 194
    swCommands_UserMacro22 = 195
    swCommands_UserMacro23 = 196
    swCommands_UserMacro24 = 197
    swCommands_UserMacro25 = 198
    swCommands_UserMacro26 = 199
    swCommands_UserMacro27 = 200
    swCommands_UserMacro28 = 201
    swCommands_UserMacro29 = 202
    swCommands_UserMacro30 = 203
    swCommands_UserMacro31 = 204
    swCommands_UserMacro32 = 205
    swCommands_UserMacro33 = 206
    swCommands_UserMacro34 = 207
    swCommands_UserMacro35 = 208
    swCommands_UserMacro36 = 209
    swCommands_UserMacro37 = 210
    swCommands_UserMacro38 = 211
    swCommands_UserMacro39 = 212
    swCommands_UserMacro40 = 213
    swCommands_UserMacro41 = 214
    swCommands_UserMacro42 = 215
    swCommands_UserMacro43 = 216
    swCommands_UserMacro44 = 217
    swCommands_UserMacro45 = 218
    swCommands_UserMacro46 = 219
    swCommands_UserMacro47 = 220
    swCommands_UserMacro48 = 221
    swCommands_UserMacro49 = 222
    swCommands_UserMacro50 = 223
    swCommands_UserMacro51 = 224
    swCommands_UserMacro52 = 225
    swCommands_UserMacro53 = 226
    swCommands_UserMacro54 = 227
    swCommands_UserMacro55 = 228
    swCommands_UserMacro56 = 229
    swCommands_UserMacro57 = 230
    swCommands_UserMacro58 = 231
    swCommands_UserMacro59 = 232
    swCommands_UserMacro60 = 233
    swCommands_UserMacro61 = 234
    swCommands_UserMacro62 = 235
    swCommands_UserMacro63 = 236
    swCommands_UserMacro64 = 237
    swCommands_UserMacro65 = 238
    swCommands_UserMacro66 = 239
    swCommands_UserMacro67 = 240
    swCommands_UserMacro68 = 241
    swCommands_UserMacro69 = 242
    swCommands_UserMacro70 = 243
    swCommands_UserMacro71 = 244
    swCommands_UserMacro72 = 245
    swCommands_UserMacro73 = 246
    swCommands_UserMacro74 = 247
    swCommands_UserMacro75 = 248
    swCommands_UserMacro76 = 249
    swCommands_UserMacro77 = 250
    swCommands_UserMacro78 = 251
    swCommands_UserMacro79 = 252
    swCommands_UserMacro80 = 253
    swCommands_UserMacro81 = 254
    swCommands_UserMacro82 = 255
    swCommands_UserMacro83 = 256
    swCommands_UserMacro84 = 257
    swCommands_UserMacro85 = 258
    swCommands_UserMacro86 = 259
    swCommands_UserMacro87 = 260
    swCommands_UserMacro88 = 261
    swCommands_UserMacro89 = 262
    swCommands_UserMacro90 = 263
    swCommands_UserMacro91 = 264
    swCommands_UserMacro92 = 265
    swCommands_UserMacro93 = 266
    swCommands_UserMacro94 = 267
    swCommands_UserMacro95 = 268
    swCommands_UserMacro96 = 269
    swCommands_UserMacro97 = 270
    swCommands_UserMacro98 = 271
    swCommands_NewMacroButton = 272
    swCommands_ToggleSelectionFilters = 273
    swCommands_ClearAllFilters = 274
    swCommands_SelectAllFilters = 275
    swCommands_FilterVertices = 276
    swCommands_FilterEdges = 277
    swCommands_FilterFaces = 278
    swCommands_FilterAxes = 279
    swCommands_FilterPlanes = 280
    swCommands_FilterSketchPoints = 281
    swCommands_FilterSketchSegments = 282
    swCommands_FilterMidpoints = 283
    swCommands_FilterCenterMarks = 284
    swCommands_FilterDimensionsHoleCallouts = 285
    swCommands_FilterSurfaceFinishSymbols = 286
    swCommands_FilterGeometricTolerances = 287
    swCommands_FilterNotesBalloons = 288
    swCommands_FilterDatumFeatures = 289
    swCommands_FilterWeldSymbols = 290
    swCommands_FilterDatumTargets = 291
    swCommands_FilterCosmeticThreads = 292
    swCommands_SplitEntities = 293
    swCommands_Parallelogram = 294
    swCommands_NewAssembly = 295
    swCommands_LayerProperties = 296
    swCommands_Rip = 297
    swCommands_DraftQualityHlrHlv = 298
    swCommands_ColorDisplayMode = 299
    swCommands_TableDrivenPattern = 300
    swCommands_ExtendSurface = 301
    swCommands_TrimSurface = 302
    swCommands_FilterSurfaceBodies = 303
    swCommands_SketchDrivenPattern = 304
    swCommands_Polygon = 305
    swCommands_IntersectionCurve = 306
    swCommands_AnnotationAlignLeft = 307
    swCommands_AnnotationAlignRight = 308
    swCommands_AlignTop = 309
    swCommands_AlignBottom = 310
    swCommands_CropView = 311
    swCommands_SpaceEvenlyAcross = 312
    swCommands_SpaceEvenlyDown = 313
    swCommands_AlignHorizontal = 314
    swCommands_AlignVertical = 315
    swCommands_SpaceTightlyAcross = 316
    swCommands_SpaceTightlyDown = 317
    swCommands_Group = 318
    swCommands_StackedBalloons = 319
    swCommands_BaseFlangeTab = 320
    swCommands_FaceCurves = 321
    swCommands_InsertFeatureBlend = 322
    swCommands_SketchedBend = 323
    swCommands_MiterFlange = 324
    swCommands_Fold = 325
    swCommands_Unfold = 326
    swCommands_Ungroup = 327
    swCommands_BrokenOutSection = 328
    swCommands_RotateView = 329
    swCommands_Pan = 330
    swCommands_ZoomInOut = 331
    swCommands_ZoomToFit = 332
    swCommands_ZoomToArea = 333
    swCommands_Wireframe = 334
    swCommands_HiddenLinesRemoved = 335
    swCommands_HiddenLinesVisible = 336
    swCommands_Shaded = 337
    swCommands_ViewPlanes = 338
    swCommands_ViewAxes = 339
    swCommands_Help = 340
    swCommands_ViewOrientation = 341
    swCommands_Options = 342
    swCommands_MassProperties = 343
    swCommands_InterferenceDetection = 344
    swCommands_PickMode = 345
    swCommands_OrdinateDimension = 346
    swCommands_HorizontalOrdinateDimension = 347
    swCommands_VerticalOrdinateDimension = 348
    swCommands_Perspective = 349
    swCommands_InsertScale = 350
    swCommands_EmptyView = 351
    swCommands_ShowEdge = 352
    swCommands_HideEdge = 353
    swCommands_ZoomToSelection = 354
    swCommands_Redraw = 355
    swCommands_ToggleSelectionFilterToolbar = 356
    swCommands_AlternatePositionView = 357
    swCommands_SketchChamfer = 358
    swCommands_EdgeFlange = 359
    swCommands_ClosedCorner = 360
    swCommands_FilterBlocks = 361
    swCommands_CurveDrivenPattern = 362
    swCommands_Hem = 363
    swCommands_BreakCornerCornerTrim = 364
    swCommands_ZebraStripes = 365
    swCommands_ChamferDimension = 366
    swCommands_MultiJogLeader = 367
    swCommands_SketchPicture = 368
    swCommands_DowelPinSymbol = 369
    swCommands_ReplaceFace = 371
    swCommands_Jog = 372
    swCommands_2DTo3DMakeRefsketchFront = 373
    swCommands_2DTo3DMakeRefsketchTop = 374
    swCommands_2DTo3DMakeRefsketchRight = 375
    swCommands_2DTo3DMakeRefsketchBottom = 376
    swCommands_2DTo3DMakeRefsketchLeft = 377
    swCommands_2DTo3DMakeRefsketchBack = 378
    swCommands_AlignSketch = 379
    swCommands_RepairSketch = 380
    swCommands_CreateSketchFromSelections = 381
    swCommands_FilterDowelPinSymbols = 382
    swCommands_SectionProperties = 383
    swCommands_AreaHatchFill = 384
    swCommands_UpdateView = 385
    swCommands_MoveSizeFeatures = 386
    swCommands_DocumentFont = 387
    swCommands_AlignRight = 388
    swCommands_AlignLeft = 389
    swCommands_Center = 390
    swCommands_Auxiliary = 391
    swCommands_Extrude = 392
    swCommands_DeleteFace = 393
    swCommands_2DTo3DCut = 394
    swCommands_ExplodeLineSketch = 395
    swCommands_RouteLine = 396
    swCommands_InsertSplitFeat = 397
    swCommands_JogLine = 398
    swCommands_ShadowsInShadedMode = 399
    swCommands_UntrimSurface = 400
    swCommands_AutoDimension = 401
    swCommands_ViewCurves = 402
    swCommands_ViewSketches = 403
    swCommands_ViewAllAnnotations = 404
    swCommands_LargeAssemblyMode = 405
    swCommands_LoftedBend = 406
    swCommands_Combine = 407
    swCommands_MoveCopyBodies = 408
    swCommands_Flex = 409
    swCommands_InsertFamilyTable = 410
    swCommands_DeviationAnalysis = 411
    swCommands_GeneralTable = 412
    swCommands_DesignTable = 413
    swCommands_MoldflowxpressAnalysisWizard = 414
    swCommands_AddTangencyControl = 415
    swCommands_AddCurvatureControl = 416
    swCommands_ShowInflectionPoints = 417
    swCommands_ShowMinimumRadius = 418
    swCommands_FilterSolidBodies = 419
    swCommands_Gravity = 420
    swCommands_StopRecordOrPlayback = 421
    swCommands_LinearMotor = 422
    swCommands_RotaryMotor = 423
    swCommands_DeleteSolidSurface = 424
    swCommands_InsertDetailCenterLine = 425
    swCommands_FitSpline = 426
    swCommands_Statistics = 427
    swCommands_PredefinedView = 428
    swCommands_SimulationToolbar = 429
    swCommands_CalculateSimulation = 430
    swCommands_ReplaySimulation = 431
    swCommands_PhotoView = 432
    swCommands_SolidworksAnimator = 433
    swCommands_3DInstantWebsite = 434
    swCommands_eDrawings = 435
    swCommands_SolidworksUtilities = 436
    swCommands_SolidworksToolbox = 437
    swCommands_Featureworks = 438
    swCommands_CosmosxpressAnalysisWizard = 439
    swCommands_ViewSketchRelations = 440
    swCommands_FilterCenterlines = 441
    swCommands_Wrap = 442
    swCommands_ShowSplineHandles = 443
    swCommands_LinearSpring = 444
    swCommands_PartingLines = 445
    swCommands_HoleTable = 446
    swCommands_AutoBalloon = 447
    swCommands_InsertRuledSurfaceFromEdge = 448
    swCommands_InsertPartingPlane = 449
    swCommands_Weldment = 450
    swCommands_ContextSelection = 451
    swCommands_ShutOffSurfaces = 452
    swCommands_Gusset = 453
    swCommands_Deform = 454
    swCommands_InsertRefpoint = 455
    swCommands_RevisionTable = 456
    swCommands_RevisionSymbol = 457
    swCommands_FilterConnectionPoints = 458
    swCommands_FilterRoutingPoints = 459
    swCommands_DesignChecker = 460
    swCommands_MakeDrawingFromPartAssembly = 461
    swCommands_MakeAssemblyFromPartAssembly = 462
    swCommands_WeldmentCutList = 463
    swCommands_ToolingSplit = 464
    swCommands_StructuralMember = 465
    swCommands_TrimExtend = 466
    swCommands_Trimetric = 467
    swCommands_Dimetric = 468
    swCommands_MakeBlock = 469
    swCommands_InsertBlock = 470
    swCommands_EditBlock = 471
    swCommands_ExplodeBlock = 472
    swCommands_SaveBlock = 473
    swCommands_Align = 474
    swCommands_Annotations = 475
    swCommands_Assemblies = 476
    swCommands_Curves = 477
    swCommands_Drawings = 478
    swCommands_Features = 479
    swCommands_Fonts = 480
    swCommands_LineFormats = 481
    swCommands_Macros = 482
    swCommands_Molds = 483
    swCommands_ReferenceGeometry = 484
    swCommands_ExplodeSketch = 485
    swCommands_SelectionFilters = 486
    swCommands_SheetMetal = 487
    swCommands_Simulation = 488
    swCommands_SketchToolbar = 489
    swCommands_DimensionRelations = 490
    swCommands_SolidworksOffice = 491
    swCommands_Splines = 492
    swCommands_Standard = 493
    swCommands_StandardViews = 494
    swCommands_Surfaces = 495
    swCommands_Tools = 496
    swCommands_Web = 497
    swCommands_View = 498
    swCommands_RealviewGraphics = 499
    swCommands_RealViewPlusGraphics = 500
    swCommands_EditMaterial = 501
    swCommands_MoveEntities = 502
    swCommands_RotateEntities = 503
    swCommands_ScaleEntities = 504
    swCommands_FilletBead = 505
    swCommands_ShadedWithEdges = 506
    swCommands_EditTexture = 507
    swCommands_Weldments = 508
    swCommands_2DTo3D = 509
    swCommands_ViewRoutingPoints = 510
    swCommands_ViewPoints = 511
    swCommands_ExcelBasedBillOfMaterials = 512
    swCommands_ModelItems = 513
    swCommands_Core = 514
    swCommands_AddRemove = 515
    swCommands_Caterpillar = 516
    swCommands_EndTreatment = 517
    swCommands_HealEdges = 518
    swCommands_InferTBGrid = 519
    swCommands_NearestSnap = 520
    swCommands_PointSnap = 521
    swCommands_HVPointSnap = 522
    swCommands_MidpointSnap = 523
    swCommands_IntersectionSnap = 524
    swCommands_HVSnap = 525
    swCommands_ParallelSnap = 526
    swCommands_PerpendicularSnap = 527
    swCommands_TangentSnap = 528
    swCommands_DynamicMirrorEntities = 529
    swCommands_CenterPointSnap = 530
    swCommands_Color = 531
    swCommands_Strikeout = 532
    swCommands_Bullet = 533
    swCommands_Stack = 534
    swCommands_SpellChecker = 535
    swCommands_AngleSnap = 536
    swCommands_QuadrantSnap = 537
    swCommands_InsertFeatureMoveFace = 538
    swCommands_Number = 539
    swCommands_LengthSnap = 540
    swCommands_CheckReadOnlyFiles = 541
    swCommands_SplineOnSurface = 542
    swCommands_DecreaseIndent = 543
    swCommands_IncreaseIndent = 544
    swCommands_PerimeterCircle = 545
    swCommands_InsertMoldFolders = 546
    swCommands_ViewPartingLines = 547
    swCommands_3DDrawingView = 548
    swCommands_SingleView = 549
    swCommands_TwoViewHorizontal = 550
    swCommands_TwoViewVertical = 551
    swCommands_FourView = 552
    swCommands_LinkViews = 553
    swCommands_Plane = 554
    swCommands_SketchGroupRebuild = 555
    swCommands_HoleSeries = 556
    swCommands_Blocks = 557
    swCommands_FillPattern = 558
    swCommands_CopyEntities = 559
    swCommands_FormingTool = 560
    swCommands_View3DSketchPlane = 561
    swCommands_View3DSketchDimensions = 562
    swCommands_MakeSmartComponent = 563
    swCommands_InvertSelection = 564
    swCommands_CosmosworksDesigner = 565
    swCommands_SolidworksRouting = 566
    swCommands_3DSketchOnPlane = 567
    swCommands_HorizontalBreak = 568
    swCommands_ResetComponents = 569
    swCommands_EndCap = 570
    swCommands_Indent = 571
    swCommands_DisplayControlPolygon = 572
    swCommands_NewMacro = 573
    swCommands_ReplaceMateEntities = 574
    swCommands_ReplaceComponents = 575
    swCommands_Print3D = 576
    swCommands_FilterWeldBeads = 577
    swCommands_NoExternalReferences = 578
    swCommands_AlignBetweenLines = 579
    swCommands_NewWindow = 580
    swCommands_TileHorizontally = 581
    swCommands_TileVertically = 582
    swCommands_Copy = 583
    swCommands_Cut = 584
    swCommands_Paste = 585
    swCommands_Undo = 586
    swCommands_Redo = 587
    swCommands_Close = 588
    swCommands_Print = 589
    swCommands_PrintPreview = 590
    swCommands_SwiftRecognizeFeatures = 591
    swCommands_SwiftInsertDimension = 592
    swCommands_SwiftInsertDatum = 593
    swCommands_SwiftInsertGtol = 594
    swCommands_SwiftShowConstraintStatus = 595
    swCommands_SwiftDeleteAll = 596
    swCommands_SwiftGtsOptions = 597
    swCommands_ToolsAddAssemblyToleranceDimension = 598
    swCommands_ToolsComputeStackAnalysis = 599
    swCommands_FullyDefineSketch = 600
    swCommands_ZoomToFitKey = 601
    swCommands_FilletManager = 602
    swCommands_DraftManager = 603
    swCommands_ScreenCapture = 604
    swCommands_Roll = 605
    swCommands_Turn = 606
    swCommands_ViewLights = 607
    swCommands_ViewCameras = 608
    swCommands_PushPull = 609
    swCommands_ColorScheme = 610
    swCommands_InsertSketchBelt = 611
    swCommands_TolXpert = 612
    swCommands_TolAnalyst = 613
    swCommands_TolXpertMultiSelect = 614
    swCommands_TolXpertEndMultiSelect = 615
    swCommands_InsertBelt = 616
    swCommands_SketchCreateChain = 617
    swCommands_InsertBoundarySurface = 618
    swCommands_FullScreenMode = 619
    swCommands_SaveAs = 620
    swCommands_CosmosMotion = 621
    swCommands_ScanTo3D = 622
    swCommands_EditFeature = 623
    swCommands_RapidPrototype = 624
    swCommands_SwiftInsertSizeDimension = 625
    swCommands_SwiftInsertMultiSelectFeature = 626
    swCommands_SwiftInsertPatternFeature = 627
    swCommands_FitText = 628
    swCommands_Conveyor = 629
    swCommands_RectangleTools = 630
    swCommands_ArcTools = 631
    swCommands_CircleTools = 632
    swCommands_Undo_Eq = 633
    swCommands_Select_All = 634
    swCommands_Reset = 635
    swCommands_Tools_Drw_Dimtext_Link = 636
    swCommands_Restore_Rotation = 637
    swCommands_Translate_Drawing = 638
    swCommands_Auto_Jog = 639
    swCommands_Create_Framepoint = 640
    swCommands_Change_Arrow_Style = 641
    swCommands_Lock_Framepoint = 642
    swCommands_Pattern_Copy = 643
    swCommands_Unlock_Framepoint = 644
    swCommands_Hide_Geometry = 645
    swCommands_Modify_Curv_Scale = 646
    swCommands_Delete_Light = 647
    swCommands_Body_Color = 648
    swCommands_Drview_Load_Model = 649
    swCommands_Body_Texture = 650
    swCommands_Feature_Color = 651
    swCommands_Feature_Texture = 652
    swCommands_Component_Color = 653
    swCommands_Component_Texture = 654
    swCommands_Edit_Def_Assy = 655
    swCommands_Mainbar_Undo = 656
    swCommands_Animation_Play_From_Start = 657
    swCommands_Api_Menu_String_File = 658
    swCommands_Animation_Wizard = 659
    swCommands_Start_Contour_Single_Select = 660
    swCommands_End_Contour_Single_Select = 661
    swCommands_Api_Menu_String_Edit = 662
    swCommands_Cancel_Sketch_Drag = 663
    swCommands_Activate_Selected_Contour = 664
    swCommands_Finish_Active_Contour = 665
    swCommands_Api_Menu_String_View = 666
    swCommands_Api_Menu_String_Insert = 667
    swCommands_Api_Menu_String_Tools = 668
    swCommands_Api_Menu_String_Window = 669
    swCommands_Api_Menu_String_Help = 670
    swCommands_Api_Menu_String_Developer_Tools = 671
    swCommands_Object_Popup_Menu = 672
    swCommands_Grid_Align = 673
    swCommands_Hatch_Properties = 674
    swCommands_Flip_180 = 675
    swCommands_Resume_Stacking_Balloons = 676
    swCommands_Stack_Dir_Up = 677
    swCommands_Stack_Dir_Down = 678
    swCommands_Delete_Relation = 679
    swCommands_Stack_Dir_Left = 680
    swCommands_Stack_Dir_Right = 681
    swCommands_Api_Menu_String_View_Toolbars = 682
    swCommands_View_Mates = 683
    swCommands_Hlink_History = 684
    swCommands_Add_Newrelation = 685
    swCommands_Show_Incontext_Feature_Holders = 686
    swCommands_Hide_Incontext_Feature_Holders = 687
    swCommands_Cd_Next = 688
    swCommands_Cd_Delete = 689
    swCommands_Cd_Previous = 690
    swCommands_Cd_Deleteall = 691
    swCommands_Cd_Refs = 692
    swCommands_Route_Properties = 693
    swCommands_Align_Vert_By_Center = 694
    swCommands_Align_Horz_By_Center = 695
    swCommands_Apply = 696
    swCommands_Close_ = 697
    swCommands_Mate_Cancel = 698
    swCommands_User_Job_Cancel = 699
    swCommands_Reset_Std_View = 700
    swCommands_Mate_Finish = 701
    swCommands_Mate_Preview = 702
    swCommands_Expl_Save = 703
    swCommands_Expl_Apply = 704
    swCommands_Expl_Cancel = 705
    swCommands_Cd_Undo = 706
    swCommands_Cd_Connum = 707
    swCommands_Defer = 708
    swCommands_Delete_Constraints = 709
    swCommands_Undo_ = 710
    swCommands_Static = 711
    swCommands_Options_Apply = 712
    swCommands_Watch_Start = 713
    swCommands_Watch_Stop = 714
    swCommands_Watch_Exit = 715
    swCommands_Cd_Edit = 716
    swCommands_Sm2_Inside = 717
    swCommands_Sm2_Outside = 718
    swCommands_Route_Properties_Popup = 719
    swCommands_Route_Options = 720
    swCommands_Route_Get_Property = 721
    swCommands_Leader_Delete_Branch = 722
    swCommands_Route_Remove_Pipe = 723
    swCommands_Rmb_Loft_Tangency = 724
    swCommands_Rmb_Loft_Smooth = 725
    swCommands_Rmb_Loft_Close = 726
    swCommands_Rmb_Sweep_Tangency = 727
    swCommands_Rmb_Sweep_Smooth = 728
    swCommands_Rmb_Sweep_Align = 729
    swCommands_Rmb_Collect_All_Bends = 730
    swCommands_Rmb_Iso_Ad_Mesh = 731
    swCommands_Rmb_Iso_Position = 732
    swCommands_Rmb_Iso_Constrain_Model = 733
    swCommands_Rmb_Iso_Ignore_Holes = 734
    swCommands_Rmb_Skcham_Dist = 735
    swCommands_Rmb_Skcham_Angle = 736
    swCommands_Rmb_Skcham_Equal = 737
    swCommands_Rmb_Sm_Reverse_Dir = 738
    swCommands_Rmb_Sm_Bend_Revdir = 739
    swCommands_Dve_Rmb_Pushpin = 740
    swCommands_Dve_Rmb_Mc_Drop_Base_Pt = 741
    swCommands_Dve_Rmb_Mc_Drop_Destination = 742
    swCommands_Dve_Rmb_Mc_Select_Entities = 743
    swCommands_Dve_Rmb_Mc_Define_Base_Pt = 744
    swCommands_Dve_Rmb_Mc_Define_Destination = 745
    swCommands_Rmb_Mvsrf_Copy = 746
    swCommands_View_Assy_Opaque = 747
    swCommands_View_Assy_Full = 748
    swCommands_View_Assy_Maintain = 749
    swCommands_Mate_Apply = 750
    swCommands_Deform_Rmb_Set_Transparent = 751
    swCommands_Deform_Rmb_Set_Zebra = 752
    swCommands_Rmb_Edit_Section = 753
    swCommands_Deform_Rmb_Add_Connector = 754
    swCommands_Deform_Rmb_Update_Display = 755
    swCommands_Deform_Rmb_Disp_Connectionlines = 756
    swCommands_Triad_Align_To_Prin = 757
    swCommands_Deform_Rmb_Reserved_3 = 758
    swCommands_Triad_Align = 759
    swCommands_Deform_Rmb_Reserved_4 = 760
    swCommands_Triad_Align2 = 761
    swCommands_Deform_Rmb_Reserved_5 = 762
    swCommands_Triad_Align_To_Comp = 763
    swCommands_Find_Next = 764
    swCommands_Remove_All = 765
    swCommands_Ok = 766
    swCommands_Cancel = 767
    swCommands_Add = 768
    swCommands_Show_Triad_Manipulator = 769
    swCommands_Route_Add_All = 770
    swCommands_Ref_Help = 771
    swCommands_Tx_Walkthrough_Goto_Start = 772
    swCommands_Tx_Walkthrough_Rewind = 773
    swCommands_Tx_Walkthrough_Play = 774
    swCommands_Tx_Walkthrough_Ff = 775
    swCommands_Tx_Walkthrough_Goto_End = 776
    swCommands_Tx_Walkthrough_Pause = 777
    swCommands_Tx_Walkthrough_Stop = 778
    swCommands_Tx_Walkthrough_Record = 779
    swCommands_Tx_Walkthrough_Play_Normal = 780
    swCommands_Tx_Walkthrough_Play_Loop = 781
    swCommands_Tx_Walkthrough_Play_Reciprocate = 782
    swCommands_Tx_Walkthrough_Play_Slow = 783
    swCommands_Tx_Walkthrough_Play_Fast = 784
    swCommands_Visual_State_Clear_Override = 785
    swCommands_Visual_State_Clear_Override_All = 786
    swCommands_Dim_Snap_Horizontal = 787
    swCommands_Dim_Snap_Vertical = 788
    swCommands_Dim_Snap_To_Edge = 789
    swCommands_Autofix_Resume = 790
    swCommands_Sign_Up = 791
    swCommands_Sign_In = 792
    swCommands_Accept = 793
    swCommands_Submit = 794
    swCommands_Browse = 795
    swCommands_Feature_Import = 796
    swCommands_Cancel_Inplace = 797
    swCommands_Object_Displaycontent = 798
    swCommands_Object_Displayasicon = 799
    swCommands_Object_Resetsize = 800
    swCommands_Edit_Dimval = 801
    swCommands_Select_Midpoint = 802
    swCommands_View_Options_Centerlines = 803
    swCommands_Finish_Section = 804
    swCommands_View_Options_Refplanes = 805
    swCommands_Parent_Child_Rel = 806
    swCommands_Entity_Properties = 807
    swCommands_Popup_Show_Hidden = 808
    swCommands_Whats_Wrong = 809
    swCommands_Popup_Hide_Hidden = 810
    swCommands_Popup_Show_Component = 811
    swCommands_Popup_Hide_Component = 812
    swCommands_Edit_Undolist = 813
    swCommands_Edit_Rollforward = 814
    swCommands_Edit_Rollback = 815
    swCommands_Edit_Drag = 816
    swCommands_Run = 817
    swCommands_Insert_Object = 818
    swCommands__Dumpfacets = 819
    swCommands_File_Saveall = 820
    swCommands_Edit_Pastespecial = 821
    swCommands_Show_Hidden = 822
    swCommands_View_Displayrelationships = 823
    swCommands_Create_Point = 824
    swCommands_View_Normalto = 825
    swCommands_View_Selectview = 826
    swCommands_View_Cutaway = 827
    swCommands_View_Exploded = 828
    swCommands_View_Displaylayout = 829
    swCommands_Add_Dragitem = 830
    swCommands_Edit_Dragitem = 831
    swCommands_Tools_Macro = 832
    swCommands_Api_Help_Contents = 833
    swCommands_Debug_Lights = 834
    swCommands__Dump_Dumpsketch = 835
    swCommands_Edit_Rebuild_Step = 836
    swCommands_Edit_Rebuild_To = 837
    swCommands_Tools_Orientcomponent = 838
    swCommands_Insert_Dimensions = 839
    swCommands_Insert_Symbols = 840
    swCommands_Tools_Blank = 841
    swCommands_Tools_Unblank = 842
    swCommands_Insert_Jog = 843
    swCommands_Insert_Drawingview_Broken = 844
    swCommands_Insert_Cthread_Callout = 845
    swCommands_Cth_Callout_Cmd = 846
    swCommands_Insert_Point = 847
    swCommands_Make_Section = 848
    swCommands_Cancel_Edit_Cntr = 849
    swCommands_Cancel_Edit_Srvr = 850
    swCommands_File_Checkout = 851
    swCommands_Insert_View_1st = 852
    swCommands__Dumpsolid = 853
    swCommands_Insert_Familytable_New = 854
    swCommands_Insert_Familytable_Open = 855
    swCommands_Insert_Page = 856
    swCommands_Insert_Sheet = 857
    swCommands_Inc_Update = 858
    swCommands_Edit_Sketch = 859
    swCommands_Sketch_Align = 860
    swCommands_Debug_Dump_Entity = 861
    swCommands_Exit_Sketch = 862
    swCommands_Edit_Sketchplane = 863
    swCommands_Component_Properties = 864
    swCommands_Feat_Edit = 865
    swCommands_Edit_Familytable = 866
    swCommands_Edit_Familytable_Open = 867
    swCommands_Edit_Incontext = 868
    swCommands_Sk_Constrain_Coincident = 869
    swCommands_Sk_Constrain_Parallel = 870
    swCommands_Sk_Constrain_Concentric = 871
    swCommands_Sketch_Section = 872
    swCommands_Sk_Constrain_Perp = 873
    swCommands_Sk_Constrain_Tangent = 874
    swCommands_View_Hide_Behind_Plane = 875
    swCommands_Insert_Group = 876
    swCommands_View_Constraint = 877
    swCommands_Edit_Force_Rebuild = 878
    swCommands__Force_Rebuild = 879
    swCommands__Showmultihidden = 880
    swCommands__Dynamichighlight = 881
    swCommands_Insert_Xhatch = 882
    swCommands_Sk_Use_Edge_Ctrline = 883
    swCommands_View_Orthographic_Named = 884
    swCommands_Update_Std_View = 885
    swCommands_Sketch_Midpoint = 886
    swCommands_Sketch_Xpoint = 887
    swCommands_Heal_Next = 888
    swCommands_Tools_Align_Horz = 889
    swCommands_Tools_Align_Vert = 890
    swCommands_View_Query_Select = 891
    swCommands_Display_Faceid = 892
    swCommands_Feat_Linear_Pattern = 893
    swCommands_Feat_Cir_Pattern = 894
    swCommands_Blank_Refgeom = 895
    swCommands_Unblank_Refgeom = 896
    swCommands_View_Sheet_Previous = 897
    swCommands_View_Sheet_Next = 898
    swCommands__Debug_Solvopt = 899
    swCommands_Heal_Back = 900
    swCommands_Blank_Part_Body = 901
    swCommands_View_Sheet = 902
    swCommands_View_Drawing_Scale = 903
    swCommands_Property_Menu_Item = 904
    swCommands_Sketch_Undo = 905
    swCommands_Heal_Close_Gaps = 906
    swCommands_Heal_Fix_Faces = 907
    swCommands_Tools_Units = 908
    swCommands_Insert_Refdim = 909
    swCommands__Dump_History = 910
    swCommands__Dump_Backup_Info = 911
    swCommands__Debug_Set_Backup = 912
    swCommands__Debug_Edit_Undo = 913
    swCommands_Unlock_Bom = 914
    swCommands_View_Change_Scale = 915
    swCommands_View_Orientation_Rmb = 916
    swCommands_Draw_Prefs = 917
    swCommands_Lock_Bom = 918
    swCommands__Display_Tuning = 919
    swCommands_Top_Right = 920
    swCommands_Save_Template = 921
    swCommands_Dims_Prefs = 922
    swCommands_Top_Left = 923
    swCommands_Insert_Sectionline = 924
    swCommands_Hide_Components = 925
    swCommands_Show_Components = 926
    swCommands_Show_Feature_Detail = 927
    swCommands_Dbg_Check_Body = 928
    swCommands_Debug_Check_Body = 929
    swCommands_Bottom_Right = 930
    swCommands_Hide_Feature_Detail = 931
    swCommands__Dump_Parasld_Ents = 932
    swCommands_Bottom_Left = 933
    swCommands__Debug_Autoconstrain = 934
    swCommands_View_Rotate_Center = 935
    swCommands_View_Rotate_Screen = 936
    swCommands_Debug_Check_Faces = 937
    swCommands_Heal_Remove_Faces = 938
    swCommands_View_Dynamic_High = 939
    swCommands_View_Pick_Invisible = 940
    swCommands_Comp_Config_Prop = 941
    swCommands_Heal_Gaps = 942
    swCommands_Heal_Gap_Edges = 943
    swCommands_Heal_Tolerant_Edges = 944
    swCommands_Tools_Dim_Pref = 945
    swCommands_Preferences_Menu_Item = 946
    swCommands_Sheet_Tab_Popup_Properties = 947
    swCommands_Sheet_Tab_Popup_Add = 948
    swCommands_Sheet_Tab_Popup_Delete = 949
    swCommands_Sheet_Tab_Popup_Activate = 950
    swCommands_Debug_Check_Iges_Geom = 951
    swCommands_View_Pick_Hidden_Wf = 952
    swCommands_View_Pick_Hidden_Hlr = 953
    swCommands_Blank_Sketch = 954
    swCommands_Unblank_Sketch = 955
    swCommands_Dump_Sketchdb = 956
    swCommands_Fix_Component = 957
    swCommands_Heal_Mistyped_Edges = 958
    swCommands_Unfix_Component = 959
    swCommands_Heal_Diagnosis_Faces = 960
    swCommands_Escape_Key_Down = 961
    swCommands_Heal_Diagnosis_Edges = 962
    swCommands_File_Summaryinfo = 963
    swCommands_Heal_Edges_Ok = 964
    swCommands_Edit_Part = 965
    swCommands_Heal_Plug_By_Extension = 966
    swCommands_Edit_Assembly = 967
    swCommands_Heal_Plug_By_Construction = 968
    swCommands_Heal_Gaps_Closed_Checking = 969
    swCommands_Open_Comp_File = 970
    swCommands_Heal_Gaps_Finishing = 971
    swCommands_Heal_Re_Sewing = 972
    swCommands_Tools_Configuration = 973
    swCommands_Heal_Upgrading = 974
    swCommands_Page_Setup = 975
    swCommands_Regen_At_Load = 976
    swCommands_File_Find = 977
    swCommands_Delete_Dtable = 978
    swCommands_Tools_Hide_Dv = 979
    swCommands_Edit_Current_Scope = 980
    swCommands_Heal_Checking_Faulty = 981
    swCommands_Heal_Failed_Check = 982
    swCommands_Heal_Constructing = 983
    swCommands_Tools_Sketch_Scale = 984
    swCommands_Tools_Sketch_Translate = 985
    swCommands_Attach_Dimensions = 986
    swCommands_Sktools_Autoconstr = 987
    swCommands_Insert_Mirrored_Part = 988
    swCommands_Split_Extrude = 989
    swCommands_Compress_Sketch = 990
    swCommands_Heal_Fallback_Choice = 991
    swCommands_File_Derive_Comp = 992
    swCommands_View_Explode_Assembly = 993
    swCommands_Heal_Fallback_Use = 994
    swCommands_View_Collapse_Assembly = 995
    swCommands_Heal_Fallback_Pass = 996
    swCommands_Autosolve_Toggle = 997
    swCommands_Refsurface_Thicken = 998
    swCommands_Insert_Mirror_Solid = 999
    swCommands_Debug_Force_Rebuild_Assem = 1000
    swCommands_Asm_Feat_Cut_Extr = 1001
    swCommands_Asm_Feat_Cut_Revolve = 1002
    swCommands_Asm_Feature_Hole = 1003
    swCommands_View_Confirm_Select = 1004
    swCommands_Insert_Extrude_Ref_Surf = 1005
    swCommands_Insert_Copy_Ref_Surface = 1006
    swCommands_Heal_Found_Faulty = 1007
    swCommands_Insert_Libfeat = 1008
    swCommands_Derive_Sketch = 1009
    swCommands_Underive_Sketch = 1010
    swCommands__Dump_Dumpheader = 1011
    swCommands__Dump_Header = 1012
    swCommands_Heal_Faces_Deleted = 1013
    swCommands_Debug_Check_Bad_Feature = 1014
    swCommands__Dump_Xmt3d_File = 1015
    swCommands_Component_Pattern = 1016
    swCommands_Heal_Checking = 1017
    swCommands_Surfid_Trace = 1018
    swCommands_Heal_Finishing = 1019
    swCommands_Debug_Set_Needs_Update = 1020
    swCommands_Debug_Set_Suppress_Affter = 1021
    swCommands_Debug_Add_Mategroup = 1022
    swCommands_Sk_Drag_Thru_Dims = 1023
    swCommands_Insert_Weld = 1024
    swCommands_Add_Spot = 1025
    swCommands_Blank_Atom_Body = 1026
    swCommands_Add_Direction = 1027
    swCommands_Unblank_Atom_Body = 1028
    swCommands_Import_Cthreads = 1029
    swCommands_View_Fm_By_Feat = 1030
    swCommands_View_Fm_By_Dep = 1031
    swCommands_Edit_Expl_Param = 1032
    swCommands_Window_Closeall = 1033
    swCommands_Assembly_Rotate_Axis = 1034
    swCommands_Debug_Dump_Journal3d = 1035
    swCommands_Dymparam_Dlg_Ok = 1036
    swCommands_Dymparam_Dlg_Cancel = 1037
    swCommands_Dymparam_Dlg_Reverse = 1038
    swCommands_Dymparam_Dlg_Regen = 1039
    swCommands_Dymparam_Dlg_Increment = 1040
    swCommands_Dymparam_Dlg_Designintent = 1041
    swCommands_File_Sync = 1042
    swCommands_View_Edit_Perspective = 1043
    swCommands_Insert_Target_Point = 1044
    swCommands_Debug_Force_Rebuild_Assem_Top_Only = 1045
    swCommands_Show_Dependents = 1046
    swCommands_Debug_Save_Entity = 1047
    swCommands_Sk_Close_Contour = 1048
    swCommands_File_Save_As_Vrml = 1049
    swCommands_Dump_All_Eqns = 1050
    swCommands_Debug_Dump_Entity_Id = 1051
    swCommands_Debug_Combine_Body = 1052
    swCommands_Debug_Check_Min_Radius = 1053
    swCommands_Debug_Dump_Kernel_Version = 1054
    swCommands_List_Extrefs = 1055
    swCommands_Debug_Match_Bool = 1056
    swCommands_Debug_Match_Bodies = 1057
    swCommands_Insert_Annotations = 1058
    swCommands_Rmb_Edit_Camera = 1059
    swCommands_View_This_Camera = 1060
    swCommands_View_Lock_Camera = 1061
    swCommands_Rmb_Lock_Camera = 1062
    swCommands_Web_Goback = 1063
    swCommands_Web_Goforward = 1064
    swCommands_Debug_Match_Regions = 1065
    swCommands_Window_Featurepalette = 1066
    swCommands_Expl_Step_New = 1067
    swCommands_Expl_Step_Prev = 1068
    swCommands_Expl_Step_Next = 1069
    swCommands_Expl_Step_Undo = 1070
    swCommands_Expl_Step_Delete = 1071
    swCommands_Expl_Step_Apply = 1072
    swCommands_Tools_Addins = 1073
    swCommands_Debug_Sketch_Tol = 1074
    swCommands_Debug_Set_Needs_Debug_Data = 1075
    swCommands_Tools_Show_Tangent = 1076
    swCommands_Tools_Show_Tan = 1077
    swCommands_Tools_Font_Tan = 1078
    swCommands_Tools_Remove_Tan = 1079
    swCommands_List_Exportents = 1080
    swCommands_Insert_Woodruff = 1081
    swCommands_Enable_Face_Blend = 1082
    swCommands_Debug_Enable_Face_Blend = 1083
    swCommands_Debug_Enable_Hole_Wizard = 1084
    swCommands__Display_List = 1085
    swCommands_Debug_Check_Ent_Id = 1086
    swCommands_App_Tipofday = 1087
    swCommands_Debug_Set_Suppress_Cms = 1088
    swCommands_Read_Section = 1089
    swCommands_Solidworks_Community = 1090
    swCommands_Debug_Dump_Surface_Mesh = 1091
    swCommands_Comp_Body = 1092
    swCommands_Comp_Display = 1093
    swCommands_Comp_Show_Detail = 1094
    swCommands_Sm_Start = 1095
    swCommands_Sm_Reorder_Bends = 1096
    swCommands_Sm_Insert_Form = 1097
    swCommands_Sm_End = 1098
    swCommands_Button33458 = 1099
    swCommands_Button33459 = 1100
    swCommands_Button33460 = 1101
    swCommands_Button33461 = 1102
    swCommands_Button33462 = 1103
    swCommands_Button33463 = 1104
    swCommands_Button33464 = 1105
    swCommands_Button33465 = 1106
    swCommands_Button33466 = 1107
    swCommands_Button33467 = 1108
    swCommands_Button33468 = 1109
    swCommands_Button33473 = 1110
    swCommands_Button33474 = 1111
    swCommands_Button33475 = 1112
    swCommands_Button33476 = 1113
    swCommands_Button33477 = 1114
    swCommands_Button33478 = 1115
    swCommands_Button33479 = 1116
    swCommands_Button33480 = 1117
    swCommands_Button33481 = 1118
    swCommands_Button33482 = 1119
    swCommands_Button33483 = 1120
    swCommands_Button33502 = 1121
    swCommands_Button33503 = 1122
    swCommands_Button33504 = 1123
    swCommands_Button33505 = 1124
    swCommands_Button33507 = 1125
    swCommands_Button33508 = 1126
    swCommands_Button33509 = 1127
    swCommands_Button33510 = 1128
    swCommands_Edit_Vsection = 1129
    swCommands_Debug_Fix_Sw97plus1_Draw = 1130
    swCommands_Insert_Picture = 1131
    swCommands_View_Display_Picture = 1132
    swCommands_View_Modify_Del_Picture = 1133
    swCommands_View_Modify_Repl_Picture = 1134
    swCommands_Move_Show_Delta_Xyz = 1135
    swCommands_Rotate_Show_Delta_Xyz = 1136
    swCommands_Tools_Customize = 1137
    swCommands_Check_Sketch_For_Feature = 1138
    swCommands_Insert_Zone = 1139
    swCommands_Query_Advanced = 1140
    swCommands_Face_Curvature = 1141
    swCommands_Move_Show_Xyz = 1142
    swCommands_Debug_Set_Tol = 1143
    swCommands_Disable_Move_Eval = 1144
    swCommands_Enable_Showdims = 1145
    swCommands_Remove_Watermark = 1146
    swCommands_Allow_Closed_Section_Lines = 1147
    swCommands_Font_Face = 1148
    swCommands_Font_Units = 1149
    swCommands_Font_Points = 1150
    swCommands_Layer_Select = 1151
    swCommands_Toolbar_First = 1152
    swCommands_Toolbar_Standard = 1153
    swCommands_Toolbar_View = 1154
    swCommands_Toolbar_Assembly = 1155
    swCommands_Toolbar_Drawing = 1156
    swCommands_Toolbar_Features = 1157
    swCommands_Toolbar_Dependency = 1158
    swCommands_Toolbar_Macro = 1159
    swCommands_Toolbar_Sel_Filter = 1160
    swCommands_Toolbar_Sketch = 1161
    swCommands_Toolbar_Sketch_Rels = 1162
    swCommands_Toolbar_Sketch_Tools = 1163
    swCommands_Toolbar_Web = 1164
    swCommands_Toolbar_Lineformat = 1165
    swCommands_Toolbar_Font = 1166
    swCommands_Toolbar_Annotation = 1167
    swCommands_Toolbar_Routing = 1168
    swCommands_Toolbar_Stdview = 1169
    swCommands_Toolbar_Selfilter = 1170
    swCommands_New_Toolbar_Selfilter = 1171
    swCommands_Toolbar_Mold = 1172
    swCommands_Toolbar_Sht_Mtl = 1173
    swCommands_Toolbar_Surface = 1174
    swCommands_Toolbar_Curve = 1175
    swCommands_Toolbar_Debug = 1176
    swCommands_New_Toolbar_Sel_Filter = 1177
    swCommands_Toolbar_Refgeom = 1178
    swCommands_Toolbar_Tools = 1179
    swCommands_Toolbar_Layer = 1180
    swCommands_Toolbar_Align = 1181
    swCommands_Toolbar_2dto3d = 1182
    swCommands_Toolbar_Exploderoute = 1183
    swCommands_Toolbar_Com_Feature = 1184
    swCommands_Toolbar_Spline_Tools = 1185
    swCommands_Toolbar_Simulation = 1186
    swCommands_Toolbar_Office = 1187
    swCommands_Toolbar_Nc_Parts = 1188
    swCommands_Toolbar_Weldment = 1189
    swCommands_Toolbar_Inference = 1190
    swCommands_Toolbar_Table = 1191
    swCommands_Toolbar_DimXpert = 1192
    swCommands_Fullscreen_Toolbar = 1193
    swCommands_Toolbar_Tolanalyst = 1194
    swCommands_Toolbar_Last = 1195
    swCommands_Insert_New_Zone = 1196
    swCommands_Debug_Set_No_Update = 1197
    swCommands_Insert_Ref_Point = 1198
    swCommands_View_Disp_Ref_Points = 1199
    swCommands_View_Disp_Ref_Points2 = 1200
    swCommands_Lightweight_Toggle = 1201
    swCommands_Make_Lightweight = 1202
    swCommands_Make_Resolved = 1203
    swCommands_Make_Suppressed = 1204
    swCommands_Toolbar_Context = 1205
    swCommands_Activate_Sheet = 1206
    swCommands_Tools_Custom_Symbol_New = 1207
    swCommands_Insert_Custom_Symbol_Save = 1208
    swCommands_Insert_Coord_Sys2 = 1209
    swCommands_View_Disp_Coordsys2 = 1210
    swCommands_Incr_Pick_Radius = 1211
    swCommands_Insert_Ref_Line = 1212
    swCommands_View_Disp_Ref_Lines = 1213
    swCommands_Enable_Mate_Inferencing = 1214
    swCommands_Assembly_Stats = 1215
    swCommands_Display_Curveid = 1216
    swCommands__Enable_Autoload = 1217
    swCommands_Explode_Custom_Symbol = 1218
    swCommands_Make_Custom_Symbol = 1219
    swCommands_Tools_Custom_Symbol_Edit = 1220
    swCommands_Debug_Monitor_Body_Tag = 1221
    swCommands_Insert_Route_Point = 1222
    swCommands_Insert_Connection_Point = 1223
    swCommands_Ref_Point_Offset = 1224
    swCommands_Ref_Point_Onset = 1225
    swCommands_Route_Set_Edit_Loc = 1226
    swCommands_Route_Add_Route_Point = 1227
    swCommands_Disable_Routing = 1228
    swCommands_Debug_Dump_Extra_Bodies = 1229
    swCommands_Dummy_Materef = 1230
    swCommands_New_View = 1231
    swCommands_Debug_Check_Two_Entities = 1232
    swCommands_App_Servicepacks = 1233
    swCommands_Resolve_All = 1234
    swCommands_Lightweight_All = 1235
    swCommands_Debug_Toggle_Dm_Journal = 1236
    swCommands_Debug_Import_Diagnosis = 1237
    swCommands_Route_Start_Con_Point = 1238
    swCommands_Hide_Bom = 1239
    swCommands_Show_Bom = 1240
    swCommands_Create_Infer_Points = 1241
    swCommands_Edit_Seed_Feature = 1242
    swCommands_Insert_Ff_Drawingview_Named = 1243
    swCommands_Insert_Ff_View_3rd = 1244
    swCommands_Tools_Addview_Ff = 1245
    swCommands_Route_Fab_Update = 1246
    swCommands_Insert_Section_Feature = 1247
    swCommands_Sk3d_Selectx = 1248
    swCommands_Sk3d_Selecty = 1249
    swCommands_Sk3d_Selectz = 1250
    swCommands_Sk3d_Selectxy = 1251
    swCommands_Sk3d_Selectyz = 1252
    swCommands_Sk3d_Selectzx = 1253
    swCommands_Tools_Arrange_Components = 1254
    swCommands__Debug_Dve = 1255
    swCommands_Documentprefs = 1256
    swCommands_Add_Ref_Point = 1257
    swCommands_New_Subassembly = 1258
    swCommands_Form_Newassembly = 1259
    swCommands_Dissolve_Subassembly = 1260
    swCommands_Line_Usecurrprops = 1261
    swCommands_Edit_Dynamic = 1262
    swCommands_Conn_Point_Flip = 1263
    swCommands_User_Macro_First = 1264
    swCommands_Parasolid_Rollback = 1265
    swCommands_Debug_Nominal_Geometry = 1266
    swCommands_Debug_Curve_Fitting = 1267
    swCommands__Useswapcopy = 1268
    swCommands_Fltr_Onoff = 1269
    swCommands_Fltr_Clearall = 1270
    swCommands_Fltr_Setall = 1271
    swCommands_Fltr_Vertex = 1272
    swCommands_Fltr_Edge = 1273
    swCommands_Fltr_Face = 1274
    swCommands_Fltr_Axis = 1275
    swCommands_Fltr_Plane = 1276
    swCommands_Fltr_Skpoint = 1277
    swCommands_Fltr_Sksegment = 1278
    swCommands_Fltr_Midpoint = 1279
    swCommands_Fltr_Centermark = 1280
    swCommands_Fltr_Dimension = 1281
    swCommands_Fltr_Surffin = 1282
    swCommands_Fltr_Gtol = 1283
    swCommands_Fltr_Note = 1284
    swCommands_Fltr_Datumfeat = 1285
    swCommands_Fltr_Weld = 1286
    swCommands_Fltr_Datumtarg = 1287
    swCommands_Fltr_Cthread = 1288
    swCommands_Pin_Drawing_Views_On = 1289
    swCommands_Detachable_Drawings = 1290
    swCommands_Dump_Ghost_Sketch = 1291
    swCommands__Enablescissor = 1292
    swCommands_Insert_Light_Pointlight = 1293
    swCommands_Insert_Light_Spotlight = 1294
    swCommands_Insert_Light_Distantlight = 1295
    swCommands_Light_Properties = 1296
    swCommands_Tools_Options = 1297
    swCommands_Disable_Route_Types = 1298
    swCommands__Debug_Sketch_Inferencing = 1299
    swCommands__Debug_Sketch_Point_Inferencing = 1300
    swCommands_Autoinfer_Toggle = 1301
    swCommands_Bom_Viewtable = 1302
    swCommands_View_Ruler = 1303
    swCommands_Debug_Time_Section_View = 1304
    swCommands_Debug_Use_Old_Section_View_Code = 1305
    swCommands__Drawalledges = 1306
    swCommands_Line_Stylebylayer = 1307
    swCommands_Line_Solid = 1308
    swCommands_Line_Dashed = 1309
    swCommands_Line_Phantom = 1310
    swCommands_Line_Chain = 1311
    swCommands_Line_Center = 1312
    swCommands_Line_Stitch = 1313
    swCommands_Line_Thickthin = 1314
    swCommands_Line_Weightbylayer = 1315
    swCommands_Line_Thin = 1316
    swCommands_Line_Normal = 1317
    swCommands_Line_Thick = 1318
    swCommands_Line_Thick2 = 1319
    swCommands_Line_Thick3 = 1320
    swCommands_Line_Thick4 = 1321
    swCommands_Line_Thick5 = 1322
    swCommands_Line_Thick6 = 1323
    swCommands_Edit_Dissolve_Assembly = 1324
    swCommands_Insert_Form_Assembly = 1325
    swCommands_Route_Realign_Fitting = 1326
    swCommands_Debug_Set_Command_Line_Debug_Code = 1327
    swCommands_Route_Add_To_Fab = 1328
    swCommands__Dump_Ecdcxmit = 1329
    swCommands__Dump_Ecdcjou = 1330
    swCommands__Ecdc_Performance = 1331
    swCommands__Ecdc_Highlight = 1332
    swCommands__Dump_Ecdcloops = 1333
    swCommands__Dump_Ecdc_Mini = 1334
    swCommands__Ecdc_Minsets = 1335
    swCommands__Ecdc_Boxsets = 1336
    swCommands__Ecdc_Boxfaces = 1337
    swCommands__Ecdc_Boxedges = 1338
    swCommands__Ecdc_Boxcache = 1339
    swCommands__Ecdcswitches = 1340
    swCommands_Tools_Clashselection = 1341
    swCommands_Dim_Inspection = 1342
    swCommands_Smart_Mate = 1343
    swCommands__Enable_Full_Restructure = 1344
    swCommands_Debug_Enable_3dfilletpoints = 1345
    swCommands__Enablecommanddeletion = 1346
    swCommands_Unfrag_File = 1347
    swCommands__Ecdcstatic = 1348
    swCommands_Auto_Sm_Drawing = 1349
    swCommands_Piping_Help = 1350
    swCommands_Piping_Help_Hint = 1351
    swCommands_Display_Face_Normal = 1352
    swCommands_Piping_Custom_Pipe_Config = 1353
    swCommands_Piping_Standard_Pipe_Config = 1354
    swCommands_Piping_Make_Flange_Driving = 1355
    swCommands_Piping_Make_Flange_Driven = 1356
    swCommands_View_Decimation_Onoff = 1357
    swCommands_Arrow_Open = 1358
    swCommands_Arrow_Closed = 1359
    swCommands_Arrow_Slash = 1360
    swCommands_Arrow_Dot = 1361
    swCommands_Arrow_Origin = 1362
    swCommands_Arrow_Wide = 1363
    swCommands_Arrow_Isowide = 1364
    swCommands_Arrow_Rus = 1365
    swCommands_Arrow_Closetop = 1366
    swCommands_Arrow_Closebot = 1367
    swCommands_Arrow_None = 1368
    swCommands_Use_New_Get_Enties_Using_Point = 1369
    swCommands_View_Toolbars = 1370
    swCommands_Debug_Enable_3duse_Edge = 1371
    swCommands_Insert_Tangency_Ref_Surface = 1372
    swCommands_Use_Assert_For_Parasolid_Mem_Leak = 1373
    swCommands_Dump_Parasolid_Memory_Leaks = 1374
    swCommands_Asm_Lin_Feat_Pattern = 1375
    swCommands_Asm_Cir_Feat_Pattern = 1376
    swCommands_Open_Comp_Assem_File = 1377
    swCommands__Displaymemoryallocation2 = 1378
    swCommands_Debug_Parasolid_Stack_Trace = 1379
    swCommands_Asm_Table_Feat_Pattern = 1380
    swCommands_Debug_P1857_Feat_Edit = 1381
    swCommands_Asm_Sketch_Feat_Pattern = 1382
    swCommands_Debug_Tsg_Transparency = 1383
    swCommands_Edit_Dcircle = 1384
    swCommands_Debug_Use_New_Surf_Extension_Ui = 1385
    swCommands_Share_Surfid_Dtd = 1386
    swCommands_Share_Surfid_All = 1387
    swCommands_Tools_Crop_Edit = 1388
    swCommands_Tools_Crop_Delete = 1389
    swCommands_View_Hideshow = 1390
    swCommands_Edit_Lsk_Pattern = 1391
    swCommands_Edit_Csk_Pattern = 1392
    swCommands_Solid_Data_Manager = 1393
    swCommands_Debug_Display_Curvature = 1394
    swCommands_View_Model_Edges = 1395
    swCommands_Debug_Dump_Config_Mgr = 1396
    swCommands_Debug_Dump_Config_Objs = 1397
    swCommands_Edit_Polygon = 1398
    swCommands_Weld_2ndray_Fillet = 1399
    swCommands_Dtd_Convert_Back = 1400
    swCommands_Goto_Section_View = 1401
    swCommands_Goto_Detail_View = 1402
    swCommands_Goto_Parent_View = 1403
    swCommands_Goto_Auxiliary_View = 1404
    swCommands_Goto_Projected_View = 1405
    swCommands_Developertools_Menu = 1406
    swCommands_Resolve_Out_Of_Date_Lwcomps = 1407
    swCommands_Insert_Sketch_Import = 1408
    swCommands_Getting_Started = 1409
    swCommands_Whats_New = 1410
    swCommands_Sw_Release_Notes = 1411
    swCommands_Sw_Beta_Report = 1412
    swCommands_Unblank_Part_Body = 1413
    swCommands_Sel_Filter_Msg_Timer = 1414
    swCommands_Save_Cgr = 1415
    swCommands_Debug_Save_Cgr = 1416
    swCommands_Edit_Suppress_All_Configs = 1417
    swCommands_Debug_Dtd_Ii = 1418
    swCommands_Edit_Suppress_Select_Configs = 1419
    swCommands_Select_Loop = 1420
    swCommands_Edit_Unsuppress_All_Configs = 1421
    swCommands_Edit_Unsuppress_Select_Configs = 1422
    swCommands_Help_Onlinetutorial = 1423
    swCommands_Edit_Unsuppress_Dependent_All_Configs = 1424
    swCommands_Edit_Unsuppress_Dependent_Select_Configs = 1425
    swCommands_Double_Click_Timer = 1426
    swCommands_Flash_Cursor_Timer = 1427
    swCommands_Select_Tangency = 1428
    swCommands_Save_As_A_Part = 1429
    swCommands_Alternate_Line_Creation = 1430
    swCommands_Help_Welcometosolidworksscreen = 1431
    swCommands_Help_Welcometosolidworks = 1432
    swCommands_Trans_In_Steps = 1433
    swCommands_Sm_Insert_Unbend = 1434
    swCommands_Assem_Hlr_Compcol = 1435
    swCommands_File_Lock = 1436
    swCommands_File_Lock_Menu = 1437
    swCommands_File_Lock_Unlock = 1438
    swCommands_File_Lockchildren = 1439
    swCommands_File_Unlockchildren = 1440
    swCommands_File_Unlock = 1441
    swCommands_Insert_Bendtable_Open = 1442
    swCommands_Insert_Bendtable_New = 1443
    swCommands_Edit_Bendtable = 1444
    swCommands_Delete_Bendtable = 1445
    swCommands_Dve_Mid_Plane = 1446
    swCommands_Dve_Blind = 1447
    swCommands_Dve_Uptovertex = 1448
    swCommands_Dve_Uptosurface = 1449
    swCommands_Dve_Offsetfromsurface = 1450
    swCommands_Dve_Throughall = 1451
    swCommands_Dve_Throughnext = 1452
    swCommands_Dve_Debug_Extr_Em = 1453
    swCommands_Dve_Debug_Extr_Ei = 1454
    swCommands_Group_Remove_Item = 1455
    swCommands_Edit_Redolist = 1456
    swCommands_Debug_Open_Cgr = 1457
    swCommands__Drawingtopart = 1458
    swCommands_Drawingtopart_Refreshdialog = 1459
    swCommands_Debug_Dump_All_Component_Config_Objects = 1460
    swCommands_Debug_Dump_Comp_Instance_Tree = 1461
    swCommands_Enable_Break_Out_Section = 1462
    swCommands_Dve_Rmb_Ok = 1463
    swCommands_Move_Dve_Resume_Drag = 1464
    swCommands_Dve_Rmb_Cancel = 1465
    swCommands_Debug_Customise_Pm = 1466
    swCommands_Enable_Proj_Drag_And_Mated_Tumble = 1467
    swCommands_View_Rotateplusy = 1468
    swCommands_View_Rotateminusy = 1469
    swCommands_View_Rotateplusz = 1470
    swCommands_View_Rotateminusz = 1471
    swCommands_View_Rotateminusx = 1472
    swCommands_View_Rotateplusx = 1473
    swCommands_View_Rotx_Minusninety = 1474
    swCommands_View_Rotx_Plusninety = 1475
    swCommands_View_Roty_Minusninety = 1476
    swCommands_View_Roty_Plusninety = 1477
    swCommands_View_Transplusx = 1478
    swCommands_View_Transminusx = 1479
    swCommands_View_Transplusy = 1480
    swCommands_View_Transminusy = 1481
    swCommands_View_Zoomin = 1482
    swCommands_View_Zoomout = 1483
    swCommands_View_Display_Faceted = 1484
    swCommands_View_Rw_Shading = 1485
    swCommands_View_Ogl_Shading = 1486
    swCommands_View_Options_Colors_Highlight = 1487
    swCommands_View_Options_Colors_Part = 1488
    swCommands_View_Options_Colors_Sketch = 1489
    swCommands_View_Options_Colors_Dimension = 1490
    swCommands_View_Options_Colors_Bg = 1491
    swCommands_View_Disp_Refdims = 1492
    swCommands_View_Fullpage = 1493
    swCommands_Window_Redraw = 1494
    swCommands_Window_Ambrowser = 1495
    swCommands_Basepart_Regen_Msg = 1496
    swCommands_Tools_Toolbars = 1497
    swCommands_Macro_Playback_Over = 1498
    swCommands_Edit_Drop = 1499
    swCommands_Ole_Property_Sheet = 1500
    swCommands_Edit_Template = 1501
    swCommands_Edit_Sheet = 1502
    swCommands_Dv_Suppress = 1503
    swCommands_Dv_Unsuppress = 1504
    swCommands_Align_Ordinate = 1505
    swCommands_Change_Ordinate_Dir = 1506
    swCommands_Edit_Ordinate = 1507
    swCommands_Select_Silhouette = 1508
    swCommands_Toggle_Grid = 1509
    swCommands_Break_Alignment = 1510
    swCommands_Align_Horz = 1511
    swCommands_Align_Vert = 1512
    swCommands_Restore_Align = 1513
    swCommands_Align_View = 1514
    swCommands_Tools_Remove_Tangent_Edges = 1515
    swCommands_Insert_Dim = 1516
    swCommands_Activate_Configuration = 1517
    swCommands_Jog_Ordinate = 1518
    swCommands_Break_View = 1519
    swCommands_Unbreak_View = 1520
    swCommands_Draw_Bl_Straight = 1521
    swCommands_Draw_Bl_Spline = 1522
    swCommands_Draw_Bl_Zigzag = 1523
    swCommands_Sel_Filter = 1524
    swCommands_Remove_From_Library = 1525
    swCommands_Add_To_Library = 1526
    swCommands_Component_Reload = 1527
    swCommands_Hide_Cthread = 1528
    swCommands_Show_Cthread = 1529
    swCommands_Edit_Drawview_Sketch = 1530
    swCommands_Align_Grid = 1531
    swCommands_Face_Xhatch_Properties = 1532
    swCommands_Unslant_Dim = 1533
    swCommands_Add_Configuration = 1534
    swCommands_Show_Configuration = 1535
    swCommands_Reset_Configuration = 1536
    swCommands_Show_Cabinet = 1537
    swCommands_Hide_Cabinet = 1538
    swCommands_Hide_Dim = 1539
    swCommands_Show_Dim = 1540
    swCommands_View_Clear_Select = 1541
    swCommands_Drview_Prop = 1542
    swCommands_Link_Dims = 1543
    swCommands_Unlink_Dim = 1544
    swCommands_Tools_Show_Tangent_Edges = 1545
    swCommands_Tools_Font_Tangent_Edges = 1546
    swCommands_Sketch_Detach = 1547
    swCommands_Flip_Ref_Dim = 1548
    swCommands_Ann_Show = 1549
    swCommands_Ann_Feat_Dim = 1550
    swCommands_Ann_Ref_Dim = 1551
    swCommands_Add_Feature_Dims = 1552
    swCommands_Remove_Feature_Dims = 1553
    swCommands_Remove_Snap = 1554
    swCommands_Toggle_Ole_Owner = 1555
    swCommands_Show_Explode_Steps = 1556
    swCommands_Create_Silhouettes = 1557
    swCommands_Show_Configuration_Adv = 1558
    swCommands_Load_Model_Thread_Finished = 1559
    swCommands_Show_Zone = 1560
    swCommands_Hide_Zone = 1561
    swCommands_Break_Dim_Align = 1562
    swCommands_Autosave = 1563
    swCommands_Show_Dim_Align = 1564
    swCommands_File_Reload_Vodoc = 1565
    swCommands_Load_Model_Thread_Failed = 1566
    swCommands_View_Display_No_Display_State = 1567
    swCommands_Rad_Dim_Radial = 1568
    swCommands_Toolbar_Routing_Str = 1569
    swCommands_Rad_Dim_Diametric = 1570
    swCommands_Rad_Dim_Lindiamtric = 1571
    swCommands_Dim_Showpara = 1572
    swCommands_Tools_Drw_Autoregen = 1573
    swCommands_Dim_Center_Text = 1574
    swCommands_Reset_Line_Font = 1575
    swCommands_Dissolve_Lib_Feature = 1576
    swCommands_More_Lines = 1577
    swCommands_Edit_Equation = 1578
    swCommands_Add_Equation = 1579
    swCommands_Del_Equation = 1580
    swCommands_Print_Selection = 1581
    swCommands_Draw_Bl_Isozag = 1582
    swCommands_Edit_Importfolder = 1583
    swCommands_View_Undo_Last = 1584
    swCommands_Convert_To_Bom98 = 1585
    swCommands_Goto_Feature = 1586
    swCommands_Goto_Component = 1587
    swCommands_Edit_Findinfm = 1588
    swCommands_Edit_User_Dims = 1589
    swCommands_Filter2 = 1590
    swCommands_Lock_Filter2 = 1591
    swCommands_Filt_Pushpin = 1592
    swCommands_Toggle_Viewing_Dir = 1593
    swCommands_Filt_Plane = 1594
    swCommands_Filt_Centermark = 1595
    swCommands_Filt_Dimn = 1596
    swCommands_Filt_Note = 1597
    swCommands_Filt_Cthread = 1598
    swCommands_Filt_Sfsymbol = 1599
    swCommands_Filt_Gtol = 1600
    swCommands_Filt_Datumfeat = 1601
    swCommands_Filt_Datumtag = 1602
    swCommands_Filt_Weldsymb = 1603
    swCommands_Filt_Skitem = 1604
    swCommands_Filt_Skpoint = 1605
    swCommands_Filt_Midpoint = 1606
    swCommands_Offset_Dim_Text = 1607
    swCommands_Lock_Filter = 1608
    swCommands_Filter_Toolbar = 1609
    swCommands_Filt_Clear = 1610
    swCommands_Filt_Face = 1611
    swCommands_Filt_Edge = 1612
    swCommands_Filt_Vertice = 1613
    swCommands_Filt_Axis = 1614
    swCommands_Forward = 1615
    swCommands_Backward = 1616
    swCommands_Home = 1617
    swCommands_Reload = 1618
    swCommands_Filter_Onoff = 1619
    swCommands_Filter_Onoff2 = 1620
    swCommands_Small_Icon = 1621
    swCommands_Large_Icon = 1622
    swCommands_Filt_All = 1623
    swCommands_Set_As_Anchor = 1624
    swCommands_User_Menu_Min = 1625
    swCommands_User_Menu_Max = 1626
    swCommands_User_Toolbar_Min = 1627
    swCommands_User_Toolbar_Max = 1628
    swCommands_Macro_Menu_Min = 1629
    swCommands_Macro_Menu_Max = 1630
    swCommands_Enable_Overlay_View = 1631
    swCommands_Insert_Schematic = 1632
    swCommands_Feat_Import_Rebuild = 1633
    swCommands_Debug_Enable_Fillet_Dve = 1634
    swCommands_Command_Option_Toggle = 1635
    swCommands_Enable_Sweepbodypattern = 1636
    swCommands_Rotate_Routing_Clip = 1637
    swCommands_Insert_Mirror_Subassembly = 1638
    swCommands_Toggle_Enhanced_Routing = 1639
    swCommands_View_Normal_To = 1640
    swCommands_Bring_Move_Comp = 1641
    swCommands_Goback_To_Drawing = 1642
    swCommands_Dve_Rmb_Multi_Radius = 1643
    swCommands_Dve_Rmb_Propagate = 1644
    swCommands_Debug_Helical_Sweep = 1645
    swCommands_Debug_Api_Attribs = 1646
    swCommands_Show_Dependents_All_Configs = 1647
    swCommands_Show_Dependents_Select_Configs = 1648
    swCommands_Hide_Components_All_Configs = 1649
    swCommands_Hide_Components_Select_Configs = 1650
    swCommands_Show_Components_All_Configs = 1651
    swCommands_Show_Components_Select_Configs = 1652
    swCommands_Dve_Rmb_Close_Spline_Curve = 1653
    swCommands_Dve_Rmb_Linear_Surface = 1654
    swCommands_Dve_Rmb_Lpat_Varysketch = 1655
    swCommands_Dve_Rmb_Lpat_Geometry_Pattern = 1656
    swCommands_Dve_Rmb_Lpat_Flip_Direction1 = 1657
    swCommands_Dve_Rmb_Lpat_Flip_Direction2 = 1658
    swCommands_Gdi_Doublebuffer_Anim = 1659
    swCommands_Rmb_Cpat_Equal_Space = 1660
    swCommands_Rmb_Cpat_Geometry_Pattern = 1661
    swCommands_Rmb_Spat_Centroid = 1662
    swCommands_Rmb_Spat_Geometry_Pattern = 1663
    swCommands_Rmb_Extend_Distance = 1664
    swCommands_Rmb_Extend_Upto_Point = 1665
    swCommands_Rmb_Extend_Upto_Surface = 1666
    swCommands_Rmb_Cpat_Flip_Direction = 1667
    swCommands_Dve_Skin0 = 1668
    swCommands_Dve_Skin1 = 1669
    swCommands_Dve_Skin2 = 1670
    swCommands_Dve_Skin3 = 1671
    swCommands_Dve_Skin4 = 1672
    swCommands_Debug_Draw_Sketch_Ogl = 1673
    swCommands_Sk_Endchain = 1674
    swCommands_Ole_Edit = 1675
    swCommands__3d_Dcm_Switches = 1676
    swCommands_Enable_Cam_Mate = 1677
    swCommands_Edit_Broken_Out_Section = 1678
    swCommands_Open_From_Webfolder = 1679
    swCommands_Save_To_Webfolder = 1680
    swCommands_Dve_No_Manipulator = 1681
    swCommands_Enable_Group_Annotations = 1682
    swCommands_Mirrcmd_Mirror_All_Children = 1683
    swCommands_Mirrcmd_Mirror_All_Instances = 1684
    swCommands_Debug_Xmit_Now = 1685
    swCommands_Mirrcmd_Copy_All_Instances = 1686
    swCommands_Mirrcmd_Browse = 1687
    swCommands_Mirrcmd_Preview_Show = 1688
    swCommands_Mirrcmd_Preview_Hide = 1689
    swCommands_Mirrcmd_Preview_Mirror_Show = 1690
    swCommands_Mirrcmd_Preview_Mirror_Hide = 1691
    swCommands_Mirrcmd_Preview_Instance_Show = 1692
    swCommands_Mirrcmd_Preview_Instance_Hide = 1693
    swCommands_App_Killtipofday = 1694
    swCommands_Debug_Enable_Hole_Series_Tab = 1695
    swCommands_Select_Tangency_Laminar = 1696
    swCommands_Select_Open_Edge_Loop = 1697
    swCommands_Debug_Offset_Thicken_Shell = 1698
    swCommands_Transparent_Edit = 1699
    swCommands_Dcubed_Debug = 1700
    swCommands_Transparentcontext_Edit = 1701
    swCommands_Auto_Size = 1702
    swCommands_Enable_Auto_Simplify = 1703
    swCommands_Tweak_Surface = 1704
    swCommands_Enable_Prc_Proj = 1705
    swCommands_Debug_Keyhole = 1706
    swCommands_Rip_Both_Directions = 1707
    swCommands_Rip_Single_Direction = 1708
    swCommands__Debug_Persistent_Dcms = 1709
    swCommands_Add_Constraint_Horiz = 1710
    swCommands_Add_Constraint_Vert = 1711
    swCommands_Add_Constraint_Colinear = 1712
    swCommands_Add_Constraint_Coradial = 1713
    swCommands_Add_Constraint_Perp = 1714
    swCommands_Add_Constraint_Parallel = 1715
    swCommands_Add_Constraint_Tang = 1716
    swCommands_Add_Constraint_Concent = 1717
    swCommands_Add_Constraint_Atmid = 1718
    swCommands_Add_Constraint_Atinter = 1719
    swCommands_Add_Constraint_Coinc = 1720
    swCommands_Add_Constraint_Samelen = 1721
    swCommands_Add_Constraint_Sym = 1722
    swCommands_Add_Constraint_Fix = 1723
    swCommands_Add_Constraint_Atpierce = 1724
    swCommands_Add_Constraint_Merge = 1725
    swCommands_Add_Constraint_Normal = 1726
    swCommands_Add_Constraint_Parallelyz = 1727
    swCommands_Add_Constraint_Parallelzx = 1728
    swCommands_Add_Constraint_Equalcurvature = 1729
    swCommands_Add_Constraint_Equaltangent = 1730
    swCommands_Add_Constraint_Tanface = 1731
    swCommands_Add_Constraint_Traction = 1732
    swCommands_Persistent_Ass_Solver = 1733
    swCommands_Clear_List_Box = 1734
    swCommands_Delete_List_Box_Item = 1735
    swCommands_Quick_Create_Plane = 1736
    swCommands_Fillet_Preview = 1737
    swCommands_Bufferswapnotify_Reduction = 1738
    swCommands_Allow_Constraints_To_Circs_In_Assem = 1739
    swCommands_Tools_New_Addins = 1740
    swCommands_Edit_Cavity_Part = 1741
    swCommands_Not_Satisfied = 1742
    swCommands_Build_Doctor = 1743
    swCommands_Solidworks_Central = 1744
    swCommands_Auto_Simplify_On_Save = 1745
    swCommands_Auto_Simplify_On_Open = 1746
    swCommands_Auto_Simplify_Now = 1747
    swCommands_Auto_Unsimplify_Now = 1748
    swCommands_Auto_Simplify_Cull_Faces = 1749
    swCommands_Auto_Simplify_Cull_Components = 1750
    swCommands_Auto_Simplify_Static_Render = 1751
    swCommands_Auto_Simplify_Dyn_Render = 1752
    swCommands_Auto_Simplify_Hlr = 1753
    swCommands_Auto_Simplify_Photoworks = 1754
    swCommands_Auto_Simplify_Shadows = 1755
    swCommands_Auto_Simplify_Save_As_Xt = 1756
    swCommands_Auto_Simplify_Move_Component = 1757
    swCommands_Auto_Simplify_Rotate_Component = 1758
    swCommands_Auto_Simplify_Collision = 1759
    swCommands_Auto_Simplify_Clearance = 1760
    swCommands_Rmb_Zebra_Properties = 1761
    swCommands_Debug_Use_Display_Data = 1762
    swCommands_Delete_All_Constraints = 1763
    swCommands_Rmb_Createplane_Linepoint = 1764
    swCommands_Rmb_Createplane_Parallel = 1765
    swCommands_Rmb_Createplane_Angle = 1766
    swCommands_Rmb_Createplane_Offset = 1767
    swCommands_Rmb_Createplane_Curve = 1768
    swCommands_Rmb_Createplane_Csys = 1769
    swCommands_Rmb_Createplane_Onsurface = 1770
    swCommands_Soft_Shadows = 1771
    swCommands_Import_To_Drawing = 1772
    swCommands_Rmb_Spat_Selpoint = 1773
    swCommands__2dto3d = 1774
    swCommands__2dto3d_Copy = 1775
    swCommands__2dto3d_Paste = 1776
    swCommands__2dto3d_Reset = 1777
    swCommands_Leader_Add_Branch = 1778
    swCommands_Leader_Delete_Bent = 1779
    swCommands_Leader_Add_Bent = 1780
    swCommands_Leader_Delete_All = 1781
    swCommands_Debug_Test_Plane_Manip = 1782
    swCommands_Aem = 1783
    swCommands_Insert_Macro_Feature = 1784
    swCommands_Debug_Force_Feat_Current_Time = 1785
    swCommands_Break_Dim_Lines = 1786
    swCommands_Edit_Exit_No_Save = 1787
    swCommands__Display_Mup = 1788
    swCommands_Rmb_Rib_First_Side = 1789
    swCommands_Rmb_Rib_Second_Side = 1790
    swCommands_Rmb_Rib_Both_Sides = 1791
    swCommands_Rmb_Rib_Normal_To_Sketch = 1792
    swCommands_Rmb_Rib_Parallel_To_Sketch = 1793
    swCommands__Dump_Selection_Manager = 1794
    swCommands_Insert_Model_Items = 1795
    swCommands_Drw_Rebuild_All = 1796
    swCommands_Cull_Dynamic_Switch = 1797
    swCommands_Cull_Static_Switch = 1798
    swCommands_Cull_Dynamic_Update = 1799
    swCommands_Auto_Simplify_Drawing_View_Creation = 1800
    swCommands_Insert_Surface_Move = 1801
    swCommands_Select_Seed_Feature = 1802
    swCommands_View_Zoom_About_Center = 1803
    swCommands_Sk_Endspline = 1804
    swCommands_Zebra_Properties = 1805
    swCommands_Flip_Dowel_Sym = 1806
    swCommands_Rmb_Face_Zebra_Stripes = 1807
    swCommands_Rmb_Ann_Use_Jog_Leader = 1808
    swCommands_Delete_Selected_Constraint = 1809
    swCommands_View_Disp_Hideall = 1810
    swCommands_Edit_Text = 1811
    swCommands__Aemswitches = 1812
    swCommands_Assy_Edit_Opaque = 1813
    swCommands_Assy_Edit_Maintain = 1814
    swCommands_Assy_Edit_Full = 1815
    swCommands_Edit_Sk_Pattern = 1816
    swCommands_Sketch_Jog_Flip = 1817
    swCommands_Add_Split_Feat_To_Asm = 1818
    swCommands_Dve_Rmb_Show_Preview = 1819
    swCommands_WPF_StyleManager = 1820
    swCommands_Start_Dialog_Reg_Test = 1821
    swCommands_Debug_Set_Feature_Auto_Name = 1822
    swCommands_Sm_Insert_Relief_Feat = 1823
    swCommands_Auto_Simplify_Auto_Recull = 1824
    swCommands_Enable_Save_Assembly_As_Part = 1825
    swCommands_Enable_Pdm = 1826
    swCommands_Enable_Lightweight_Drawings = 1827
    swCommands_Enable_Superlightweight = 1828
    swCommands_Insert_Folder = 1829
    swCommands_Sm_Measure_Bend_Deviation = 1830
    swCommands_Debug_Pk_Lofted_Body = 1831
    swCommands_Debug_Dump_Sectioned_Bodies = 1832
    swCommands_Insert_Sketch_Dxfdwg = 1833
    swCommands_Dotmenu_Scenegraph_Dump_Memory = 1834
    swCommands_Dotmenu_Scenegraph_Dump_Structure = 1835
    swCommands_Back_Office_Precreate_Drview = 1836
    swCommands_Insert_Macro_Feature_Drawing = 1837
    swCommands_Geometric_Callout = 1838
    swCommands_Holewizard_Callout = 1839
    swCommands__Dcubedoptions_Sketchdebugswitches = 1840
    swCommands__Debug_Sketch_Switches = 1841
    swCommands__Debug_Assembly_Switches = 1842
    swCommands_Back_Office_Precreate_Drview_Enable = 1843
    swCommands_Smp_Assm_Hlr_Drawing = 1844
    swCommands_Spline_Switch = 1845
    swCommands_Unlock_Configuration = 1846
    swCommands_Lock_Configuration = 1847
    swCommands_Insert_Designtable = 1848
    swCommands_Insert_Drw_Dxfdwg = 1849
    swCommands_Debug_Preview_Assm_Hlr = 1850
    swCommands_Debug_Skoffset_Line_Preview = 1851
    swCommands_Debug_Skoffset_Popup_Text = 1852
    swCommands_Save_Config_Preview = 1853
    swCommands_Bgproc_Block = 1854
    swCommands_Insert_Com_Feature_Min = 1855
    swCommands_Edit_Smart_Insert = 1856
    swCommands_Mark_Smart_Insert_Uptodate = 1857
    swCommands_Split_Open_Segm_Ar = 1858
    swCommands_Rmb_Ar_Autoroute = 1859
    swCommands_Insert_Com_Feature_Max = 1860
    swCommands__Mirrormates = 1861
    swCommands_Enablenewnote = 1862
    swCommands_Blockdef_Properties = 1863
    swCommands_Blockdef_Select_All_Insts = 1864
    swCommands_Blockdef_Delete_All_Insts = 1865
    swCommands_Blockdef_Edit = 1866
    swCommands_Draw_View_Start_Hlr = 1867
    swCommands_Draw_All_View_Start_Hlr = 1868
    swCommands_Aem_Sim_Startstop = 1869
    swCommands_Aem_Sim_Addeditspring = 1870
    swCommands_Aem_Sim_Slow = 1871
    swCommands_Aem_Sim_Ffwd = 1872
    swCommands_Cmark_Setbase = 1873
    swCommands__Dump_Refchain_Manager = 1874
    swCommands_Show_Ogl_Stats = 1875
    swCommands_Sheet_Draft_Mode = 1876
    swCommands_Enable_Dynamic_Load_Body = 1877
    swCommands_Insert_Geometry_Import = 1878
    swCommands_View_Incr_Tessellation = 1879
    swCommands_Spline_Tool_Region_Drag = 1880
    swCommands_Aem_Sim_Addeditmotor = 1881
    swCommands_Help_Autocad_Users = 1882
    swCommands_Reset_Solvers = 1883
    swCommands_Display_Property_Dve = 1884
    swCommands_Block_Insert = 1885
    swCommands_Block_Make = 1886
    swCommands_Block_Edit = 1887
    swCommands_Block_Explode = 1888
    swCommands_Block_Delete = 1889
    swCommands_Block_Select_Instances = 1890
    swCommands_Block_Edit_Instance = 1891
    swCommands_Auto_Dim_Drawing = 1892
    swCommands_Cmark_Merge = 1893
    swCommands_Sketch_Show_Constraints = 1894
    swCommands_View_Showantn_Linkerrors = 1895
    swCommands_Block_Edit_From_File = 1896
    swCommands__Debug_Auto_Dim_Sketch = 1897
    swCommands_Cmark_Select = 1898
    swCommands_Edit_Bendtable_Open = 1899
    swCommands_Toggle_Pic_Texture = 1900
    swCommands_Aem_Sim_Savereplay = 1901
    swCommands_Aem_Sim_Pause = 1902
    swCommands_Aem_Sim_Reverse = 1903
    swCommands_Add_To_Favorite = 1904
    swCommands_Read_Only_Pref = 1905
    swCommands_Create_Empty_Folder = 1906
    swCommands_Edit_Delete_Replay = 1907
    swCommands_Driven_Dim = 1908
    swCommands_Block_New = 1909
    swCommands_Sketch_Hide_Constraints = 1910
    swCommands_Button38171 = 1911
    swCommands_Button38172 = 1912
    swCommands_Button38173 = 1913
    swCommands_Button38174 = 1914
    swCommands_Aem_Sim_Ping_Ping = 1915
    swCommands_Aem_Sim_Ping_Pong = 1916
    swCommands_Dotmenu_Disable_Edge_Cache = 1917
    swCommands_Button38181 = 1918
    swCommands_Button38183 = 1919
    swCommands_Manufacturing_Network = 1920
    swCommands_Aem_Sim_Addedittorsional_Spring = 1921
    swCommands_Insert_Gearmate = 1922
    swCommands_Chamfer_Preview = 1923
    swCommands_Sketch_Hide_All_Constraints = 1924
    swCommands_Debug_Enable_Many_Curv_Surf = 1925
    swCommands_Aem_Sim_Addedit_Conveyor = 1926
    swCommands_Force_Convert_Explode = 1927
    swCommands_Debug_Enable_Helical_Sweep_Performance = 1928
    swCommands_Switch_To_Toolbar_First = 1929
    swCommands_Switch_To_Sketch_Toolbar = 1930
    swCommands_Switch_To_Feature_Toolbar = 1931
    swCommands_Switch_To_Sht_Mtl_Toolbar = 1932
    swCommands_Switch_To_Surface_Toolbar = 1933
    swCommands_Switch_To_Assembly_Toolbar = 1934
    swCommands_Switch_To_Drawing_Toolbar = 1935
    swCommands_Sketch_Suppress_Constraints = 1936
    swCommands_Switch_To_Toolbar_Last = 1937
    swCommands_Customization_And_More = 1938
    swCommands_Drawing_Assembly_Stats = 1939
    swCommands_Tools_Move_Copy = 1940
    swCommands_Component_Pattern_Linear = 1941
    swCommands_Component_Pattern_Circular = 1942
    swCommands_Component_Pattern_Feature = 1943
    swCommands_Rmb_Mate_Apply = 1944
    swCommands_Dve_Rmb_Undo = 1945
    swCommands_Quick_Help = 1946
    swCommands_Dve_Rmb_Redo = 1947
    swCommands_Pe_Newsgroup = 1948
    swCommands_Debug_Enable_Improvedrawingviewcreation = 1949
    swCommands_Lic_Agreement = 1950
    swCommands_Debug_Material_Editor = 1951
    swCommands_Enable_Shared_Tessellation = 1952
    swCommands_Insert_End_Cap = 1953
    swCommands_Silhouette_Offsets = 1954
    swCommands_Layer_Toolbar = 1955
    swCommands_Sketch_Tools_Toolbar = 1956
    swCommands_UseWpfCommands = 1957
    swCommands_WpfTestCommand = 1958
    swCommands_Animation_Goto_Start = 1959
    swCommands_Animation_Rewind = 1960
    swCommands_Animation_Play = 1961
    swCommands_Animation_Ff = 1962
    swCommands_Animation_Goto_End = 1963
    swCommands_Animation_Pause = 1964
    swCommands_Animation_Stop = 1965
    swCommands_Animation_Record = 1966
    swCommands_Animation_Play_Normal = 1967
    swCommands_Animation_Play_Loop = 1968
    swCommands_Animation_Play_Reciprocate = 1969
    swCommands_Animation_Play_Slow = 1970
    swCommands_Animation_Play_Fast = 1971
    swCommands_Recorddrag = 1972
    swCommands_Insert_Create_Assy = 1973
    swCommands_Insert_Create_Assy_Feat = 1974
    swCommands_Table_Cell_Sub_Total = 1975
    swCommands_Table_Cell_Total = 1976
    swCommands_Collapse_Tree = 1977
    swCommands_Enable_Light_Manipulators = 1978
    swCommands_Edit_Color_Scheme = 1979
    swCommands_View_Cg = 1980
    swCommands_Customization_Context_Tbar = 1981
    swCommands_View_Animate_Explode_Assembly = 1982
    swCommands_View_Animate_Collapse_Assembly = 1983
    swCommands_Quick_Help_Part = 1984
    swCommands_Quick_Help_Drawing = 1985
    swCommands_Quick_Help_Assembly = 1986
    swCommands_Whats_New_Interactive = 1987
    swCommands_Quick_Help_Assembly2 = 1988
    swCommands_Display_Face = 1989
    swCommands_Toggle_Context_Switch = 1990
    swCommands_Move_Alignment_Part = 1991
    swCommands_Move_Alignment_Assembly = 1992
    swCommands_View_Move_Manipulator = 1993
    swCommands_Help_Partnersolutions = 1994
    swCommands_Conc_Dim_Show_Extn_Lines = 1995
    swCommands_Debug_Enable_Previewwithmodelviewslist = 1996
    swCommands_Edit_Table_Row_Property = 1997
    swCommands_Search_Detail_Items = 1998
    swCommands_Recognize_Features = 1999
    swCommands_Move_Up_Using_Arrow_Key = 2000
    swCommands_Move_Down_Using_Arrow_Key = 2001
    swCommands_Move_Left_Using_Arrow_Key = 2002
    swCommands_Move_Right_Using_Arrow_Key = 2003
    swCommands__Debug_Pgm = 2004
    swCommands_Front_Top_Side_Viewports = 2005
    swCommands_First_Angle_Projection = 2006
    swCommands_Favorite_Material_1 = 2007
    swCommands_Favorite_Material_2 = 2008
    swCommands_Favorite_Material_3 = 2009
    swCommands_Favorite_Material_4 = 2010
    swCommands_Favorite_Material_5 = 2011
    swCommands_Favorite_Material_6 = 2012
    swCommands_Favorite_Material_7 = 2013
    swCommands_Favorite_Material_8 = 2014
    swCommands_Favorite_Material_9 = 2015
    swCommands_Favorite_Material_10 = 2016
    swCommands_Copy_Swift_Schema = 2017
    swCommands_Edit_Swift_Schema = 2018
    swCommands_Debug_Anim_Capture = 2019
    swCommands_Insert_Swift_Symbol = 2020
    swCommands_Debug_Hsds_Dialog = 2021
    swCommands_Create_New_Configuration = 2022
    swCommands_Skg_Remove = 2023
    swCommands_Skg_Insertionpoint = 2024
    swCommands_Skg_Save = 2025
    swCommands_Skg_Ok = 2026
    swCommands_Skg_Cancel = 2027
    swCommands_Toolbar_Sketch_Group = 2028
    swCommands_Debug_Visual_Overlay = 2029
    swCommands_Content_Filter_All = 2030
    swCommands_Content_Filter_Parts = 2031
    swCommands_Content_Filter_Asm = 2032
    swCommands_Content_Filter_Features = 2033
    swCommands_Content_Filter_Notes = 2034
    swCommands_Content_Filter_Gtol = 2035
    swCommands_Content_Filter_Sfin = 2036
    swCommands_Content_Filter_Weld = 2037
    swCommands_Content_Filter_Formtools = 2038
    swCommands_Content_Back = 2039
    swCommands_Content_Forward = 2040
    swCommands_Content_Search = 2041
    swCommands_Content_Reload = 2042
    swCommands_Asm_Configure_All_Children = 2043
    swCommands_Asm_Configure_All_Parents = 2044
    swCommands_Asm_Unconfigure_All = 2045
    swCommands_Infer_Tb_Enabled = 2046
    swCommands_Infer_Tb_Grid_Quick = 2047
    swCommands_Infer_Tb_Nearest_Quick = 2048
    swCommands_Hide_Swift_Dims = 2049
    swCommands_Infer_Tb_Points_Quick = 2050
    swCommands_Infer_Tb_Hv_Points_Quick = 2051
    swCommands_Infer_Tb_Midpoints_Quick = 2052
    swCommands_Infer_Tb_Intersection_Quick = 2053
    swCommands_Infer_Tb_Hv_Quick = 2054
    swCommands_Infer_Tb_Parallel_Quick = 2055
    swCommands_Infer_Tb_Perpendicular_Quick = 2056
    swCommands_Infer_Tb_Tangent_Quick = 2057
    swCommands_Insert_Cos = 2058
    swCommands_Activate_Doc_Or_Journal = 2059
    swCommands_Save_Journal_As_Word = 2060
    swCommands_Add_File_To_Docs = 2061
    swCommands_Add_Comment = 2062
    swCommands_Remove_All_Comments = 2063
    swCommands_Small_List_Icon = 2064
    swCommands_Large_List_Icon = 2065
    swCommands_Dotmenu_New_Broken_Enabled = 2066
    swCommands_Content_Filter_Block = 2067
    swCommands_Edit_Paragraph = 2068
    swCommands_Edit_Bullet = 2069
    swCommands_Delete_Comment = 2070
    swCommands_Edit_Comment = 2071
    swCommands_Add_Voice_Comment = 2072
    swCommands_Manual_Viewlabel = 2073
    swCommands_Electrical_Open_Cable_Wire_Library = 2074
    swCommands_Electrical_Open_Component_Library = 2075
    swCommands_Electrical_Read_Segment_Data = 2076
    swCommands_Electrical_Write_Segment_Data = 2077
    swCommands_Electrical_Load_From_To_Data = 2078
    swCommands_Electrical_Autoroute = 2079
    swCommands_Infer_Tb_Centerpoints_Quick = 2080
    swCommands_Hide_Swift_Ann = 2081
    swCommands_Import_Electrical_Data = 2082
    swCommands_Infer_Tb_Quadrants_Quick = 2083
    swCommands_Infer_Tb_Angle_Quick = 2084
    swCommands_Show_Feat_Based_Swift_Tree = 2085
    swCommands_Show_Ann_Based_Swift_Tree = 2086
    swCommands_Show_Flat_Swift_Tree = 2087
    swCommands_Hide_Swift_All_Datum_Tags = 2088
    swCommands_Edit_Voice_Comment = 2089
    swCommands_Delete_Voice_Comment = 2090
    swCommands_Debug_Prj8329_Tolerance = 2091
    swCommands_Html_Go_Back = 2092
    swCommands_Html_Go_Forward = 2093
    swCommands_Html_Go_Search_The_Web = 2094
    swCommands_Html_Go_Start_Page = 2095
    swCommands_Html_View_Stop = 2096
    swCommands_Html_View_Refresh = 2097
    swCommands_Font_Restart_Number = 2098
    swCommands_Font_Continue_Number = 2099
    swCommands_Measure_Proj = 2100
    swCommands_Measure_Minmax = 2101
    swCommands_Measure_Units = 2102
    swCommands_Measure_Xyz = 2103
    swCommands_Measure_Csys = 2104
    swCommands_Dist_Min = 2105
    swCommands_Dist_Max = 2106
    swCommands_Dist_Cc = 2107
    swCommands_Measure_Proj_None = 2108
    swCommands_Measure_Proj_Screen = 2109
    swCommands_Measure_Proj_Plane = 2110
    swCommands_Measure_Proj_Recent = 2111
    swCommands_Measure_Defaultcsys = 2112
    swCommands_Debug_Anim_Dimension = 2113
    swCommands_Repeat_Command = 2114
    swCommands_Content_Mgr_Search_Local_Cmd = 2115
    swCommands_Content_Mgr_Search_3dcc_Cmd = 2116
    swCommands_Swift_Ann_Disp_Angle = 2117
    swCommands_Save_Comp = 2118
    swCommands_Change_Write_Access_Comp = 2119
    swCommands_Change_Write_Access = 2120
    swCommands_View_Display_States = 2121
    swCommands_Display_State_Rmb = 2122
    swCommands_Debug_Enable_Smartfilterforfilletchamfer = 2123
    swCommands_Incremental_Sg_Update = 2124
    swCommands_Dotmenu_Use_Manipulator_In_3dsketch = 2125
    swCommands_Sk_Endcos = 2126
    swCommands_Sw_Taskpane = 2127
    swCommands_Import_Electrical_Cab_Data = 2128
    swCommands_New_Display_State = 2129
    swCommands_Swift_Layout_Top = 2130
    swCommands_Swift_Layout_Front = 2131
    swCommands_Swift_Layout_Right = 2132
    swCommands_Show_Flexible_Name = 2133
    swCommands_Animkey_Cut = 2134
    swCommands_Animkey_Copy = 2135
    swCommands_Animkey_Paste = 2136
    swCommands_Animkey_Clear = 2137
    swCommands_Animkey_Select_All = 2138
    swCommands_Animkey_Properties = 2139
    swCommands_Animkey_Place = 2140
    swCommands_Animkey_Replace = 2141
    swCommands_Animation_New = 2142
    swCommands_Animation_Rename = 2143
    swCommands_Animation_Delete = 2144
    swCommands_View_Showantn_Linkvar = 2145
    swCommands_Gantt_Zoomin = 2146
    swCommands_Gantt_Zoomout = 2147
    swCommands_Import_Cable_Library = 2148
    swCommands_Import_Component_Library = 2149
    swCommands_Animkey_Reverse_Path = 2150
    swCommands_Display_State_Undo = 2151
    swCommands_Display_State_Redo = 2152
    swCommands_Debug_Enable_Pdm_Sync = 2153
    swCommands_Debug_Enable_Ctrl_Measure = 2154
    swCommands_Animkey_Suppress = 2155
    swCommands_Animkey_Interp_Step_End = 2156
    swCommands_Animkey_Interp_Linear = 2157
    swCommands_Animkey_Interp_Easein_Quad = 2158
    swCommands_Animkey_Interp_Easeout_Quad = 2159
    swCommands_Animkey_Interp_Easeinout_Quad = 2160
    swCommands_Animkey_Interp_Easein_Sin = 2161
    swCommands_Animkey_Interp_Easeout_Sin = 2162
    swCommands_Animkey_Interp_Easeinout_Sin = 2163
    swCommands_Dve_Rmb_Back = 2164
    swCommands_Dve_Rmb_Next = 2165
    swCommands_Edit_Rtl_Mode = 2166
    swCommands_Content_Add_Existing_Folder = 2167
    swCommands_Content_Create_New_Folder = 2168
    swCommands_Option_Relations_Snaps = 2169
    swCommands_Content_Add_File_Location = 2170
    swCommands_Add_To_Palette = 2171
    swCommands_Drawing_Stats = 2172
    swCommands_Dcubed_Versions = 2173
    swCommands_Billboards = 2174
    swCommands_Insert_Cut_Net = 2175
    swCommands_Insert_Stock_Net = 2176
    swCommands_Insert_Protrusion_Volswept = 2177
    swCommands_Insert_Volsweep_Ref_Surface = 2178
    swCommands_Insert_Cut_Volsweep = 2179
    swCommands_Swift_Adv_Tol_Ann = 2180
    swCommands_Save_Smart = 2181
    swCommands_Viewport_3d_Cursor = 2182
    swCommands_Debug_Enable_Prc_Project = 2183
    swCommands_Debug_Enable_3d_Project = 2184
    swCommands_Viewport_Unsplit_Camera = 2185
    swCommands_Show_Ogl_Framecount = 2186
    swCommands_Insert_Annotation_Plane = 2187
    swCommands_Swift_Other_Recognition_Engine = 2188
    swCommands_Layout_To_Doc = 2189
    swCommands_Sketch_Group_Flip = 2190
    swCommands_Insert_Camera = 2191
    swCommands_Resolve_Conflict = 2192
    swCommands_Convert_Spline_To_Circlines = 2193
    swCommands_Debug_Enable_Contour_Editing = 2194
    swCommands_Addedit_Mate_Supplement = 2195
    swCommands_Glassbox_Done = 2196
    swCommands_Glassbox_Zoomtofit = 2197
    swCommands_Glassbox_Zoomto = 2198
    swCommands_Glassbox_Zoom = 2199
    swCommands_Glassbox_Rotate = 2200
    swCommands_Glassbox_Pan = 2201
    swCommands_Copy_Drw_To_Dwgeditor = 2202
    swCommands_Whats_Wrong_Tolx_Dim = 2203
    swCommands_Add_Constraint_Alongx = 2204
    swCommands_Add_Constraint_Alongy = 2205
    swCommands_Add_Constraint_Alongz = 2206
    swCommands_Edit_Decal = 2207
    swCommands_Ann_Per_Annotation_View = 2208
    swCommands_Annotation_Visibility = 2209
    swCommands_Annotation_View_Create = 2210
    swCommands_Switch_Annotation_View = 2211
    swCommands_Autotrace_Sketchpic = 2212
    swCommands_Activate_Annotation_View = 2213
    swCommands_Deactivate_Annotation_View = 2214
    swCommands_Delete_Annotation_View = 2215
    swCommands_Orient_Annotation_By_Selection = 2216
    swCommands_Add_Constraint_Onsurface = 2217
    swCommands_Smart_Feature_Preview = 2218
    swCommands_Smc_Help = 2219
    swCommands_Insert_Smart_Features = 2220
    swCommands_Edit_Smart_Comp_Inst = 2221
    swCommands_Auto_Ann_View_Creation = 2222
    swCommands_Auto_Ann_View_Generate = 2223
    swCommands_Change_Ann_View = 2224
    swCommands_Swift_Use_Callout_Template = 2225
    swCommands_Light_Prop_Item_Min = 2226
    swCommands_Light_Prop_Item_Max = 2227
    swCommands_Light_Del_Item_Min = 2228
    swCommands_Light_Del_Item_Max = 2229
    swCommands_Activate_And_Orient_Annotation_View = 2230
    swCommands_Tab_Reorient = 2231
    swCommands_Annotation_View_Show = 2232
    swCommands_Annotation_View_Hide = 2233
    swCommands_Edit_Annotation_View = 2234
    swCommands_Insert_Smartfeature = 2235
    swCommands_Debug_Set_Res_Point = 2236
    swCommands_Debug_Check_Res_Leak = 2237
    swCommands_Custom_Msg_Display_Vw_By_Name = 2238
    swCommands_Custom_Msg_Display_Camera_By_Name = 2239
    swCommands_Debug_Enable_New_Cthread_Creation = 2240
    swCommands_Autofix_Model = 2241
    swCommands_Debug_Enable_Open_Multiple_Files = 2242
    swCommands_Show_View_Palette = 2243
    swCommands_Debug_Enable_Convert_Sheetmetal = 2244
    swCommands_Sm_Convert_To_Sheetmetal = 2245
    swCommands_Isolate1 = 2246
    swCommands_Isolate2 = 2247
    swCommands_Crt_Rut_Using_Connector = 2248
    swCommands_Crt_Rt_Using_From_To_Lst = 2249
    swCommands_Crt_Adhoc_Rt = 2250
    swCommands_Edt_Elec_Route = 2251
    swCommands_Edt_Elec_Wires = 2252
    swCommands_Elec_Rt_Properties = 2253
    swCommands_Crt_Pipe_Rt_Using_Connector = 2254
    swCommands_Crt_Pipe_Rt_Adhoc = 2255
    swCommands_Edit_Pipe_Rt = 2256
    swCommands_Pipe_Rt_Properties = 2257
    swCommands_Crt_Flex_Tube_Rt_Using_Connector = 2258
    swCommands_Crt_Flex_Tube_Rt_Adhoc = 2259
    swCommands_Edit_Flex_Tube_Rt = 2260
    swCommands_Flex_Tube_Rt_Properties = 2261
    swCommands_Flex_Tube_Rt_Guide = 2262
    swCommands_Piping_Rt_Guide = 2263
    swCommands_Electrical_Rt_Guide = 2264
    swCommands_Auto_Route = 2265
    swCommands_Route_Rotate_Clip = 2266
    swCommands_Route_Through = 2267
    swCommands_Route_Unhook_From = 2268
    swCommands_Split_Route = 2269
    swCommands_Pipe_Route = 2270
    swCommands_Electrical_Route = 2271
    swCommands_Flexible_Tube_Route = 2272
    swCommands_Align_With_Comp_Origin = 2273
    swCommands_Align_With_Assy_Origin = 2274
    swCommands_Snap_To_Selection = 2275
    swCommands_Snap_While_Dragging = 2276
    swCommands_Rotate_90_Degrees = 2277
    swCommands_Rotate_180_Degrees = 2278
    swCommands_Align_With_Selection = 2279
    swCommands_Enable_Conics = 2280
    swCommands_Swift_Fpo_Constr_Point = 2281
    swCommands_Swift_Fpo_Constr_Line = 2282
    swCommands_Swift_Fpo_Constr_Circle = 2283
    swCommands_Swift_Fpo_Constr_Plane = 2284
    swCommands_Add_Fitting = 2285
    swCommands_Add_Coverings = 2286
    swCommands_Content_Wizard = 2287
    swCommands_Change_Route_Dia = 2288
    swCommands_Repair_Route = 2289
    swCommands_Add_Bends = 2290
    swCommands_Move_Spherical_Manipulator = 2291
    swCommands_Resize_Spherical_Manipulator = 2292
    swCommands__Debug_Memory_Leaks = 2293
    swCommands_Flextube_Dummy_Button_2 = 2294
    swCommands_File_Copy_Design = 2295
    swCommands_Flextube_Dummy_Button_Big_1 = 2296
    swCommands_Flextube_Dummy_Button_Big_2 = 2297
    swCommands_Piping_Dummy_Button_1 = 2298
    swCommands_Piping_Dummy_Button_Big_1 = 2299
    swCommands_Electrical_Dummy_Button_1 = 2300
    swCommands_Electrical_Dummy_Button_2 = 2301
    swCommands_Electrical_Dummy_Button_3 = 2302
    swCommands_Electrical_Dummy_Button_4 = 2303
    swCommands_Electrical_Dummy_Button_5 = 2304
    swCommands_Electrical_Dummy_Button_6 = 2305
    swCommands_Electrical_Dummy_Button_7 = 2306
    swCommands_Electrical_Dummy_Button_8 = 2307
    swCommands_Electrical_Dummy_Button_9 = 2308
    swCommands_Electrical_Dummy_Button_10 = 2309
    swCommands_Electrical_Dummy_Button_Big_1 = 2310
    swCommands_Electrical_Dummy_Button_Big_2 = 2311
    swCommands_Electrical_Dummy_Button_Big_3 = 2312
    swCommands_Electrical_Dummy_Button_Big_4 = 2313
    swCommands_Electrical_Dummy_Button_Big_5 = 2314
    swCommands_Electrical_Dummy_Button_Big_6 = 2315
    swCommands_Electrical_Dummy_Button_Big_7 = 2316
    swCommands_Electrical_Dummy_Button_Big_8 = 2317
    swCommands_Electrical_Dummy_Button_Big_9 = 2318
    swCommands_Electrical_Dummy_Button_Big_10 = 2319
    swCommands_Common_Tool_Dummy_Button_1 = 2320
    swCommands_Common_Tool_Dummy_Button_2 = 2321
    swCommands_Common_Tool_Dummy_Button_3 = 2322
    swCommands_Common_Tool_Dummy_Button_4 = 2323
    swCommands_Common_Tool_Dummy_Button_5 = 2324
    swCommands_Common_Tool_Dummy_Button_6 = 2325
    swCommands_Common_Tool_Dummy_Button_7 = 2326
    swCommands_Common_Tool_Dummy_Button_8 = 2327
    swCommands_Common_Tool_Dummy_Button_9 = 2328
    swCommands_Common_Tool_Dummy_Button_10 = 2329
    swCommands_Common_Tool_Dummy_Button_Big_1 = 2330
    swCommands_Common_Tool_Dummy_Button_Big_2 = 2331
    swCommands_Common_Tool_Dummy_Button_Big_3 = 2332
    swCommands_Common_Tool_Dummy_Button_Big_4 = 2333
    swCommands_Common_Tool_Dummy_Button_Big_5 = 2334
    swCommands_Common_Tool_Dummy_Button_Big_6 = 2335
    swCommands_Common_Tool_Dummy_Button_Big_7 = 2336
    swCommands_Common_Tool_Dummy_Button_Big_8 = 2337
    swCommands_Common_Tool_Dummy_Button_Big_9 = 2338
    swCommands_Common_Tool_Dummy_Button_Big_10 = 2339
    swCommands_Common_Tool_Dummy_Button_11 = 2340
    swCommands_Publish_Content = 2341
    swCommands_Split_Open_Route = 2342
    swCommands_Anim_View_Front = 2343
    swCommands_Anim_View_Back = 2344
    swCommands_Anim_View_Left = 2345
    swCommands_Anim_View_Right = 2346
    swCommands_Anim_View_Top = 2347
    swCommands_Anim_View_Bottom = 2348
    swCommands_Anim_View_Isometric = 2349
    swCommands_Anim_View_Trimetric = 2350
    swCommands_Anim_View_Dimetric = 2351
    swCommands_Anim_Custom_Msg_Display_Vw_By_Name = 2352
    swCommands_Anim_Custom_Msg_Display_Camera_By_Name = 2353
    swCommands_Anim_View_Camera = 2354
    swCommands_View_Scale_Has_Changed = 2355
    swCommands_Zebra_Stripe_Preview = 2356
    swCommands_Savenotification = 2357
    swCommands_Change_Shader = 2358
    swCommands_Bold_Menu_Title = 2359
    swCommands_Edit_Weldment_Props = 2360
    swCommands_Delete_Weldment = 2361
    swCommands_Hole_Table_Hide_Origin = 2362
    swCommands_Hole_Table_Show_Origin = 2363
    swCommands_Hole_Table_Goto_Tag = 2364
    swCommands_Spline_Tool_Delete_Tangency = 2365
    swCommands_Spline_Tool_Delete_Curvature = 2366
    swCommands_Create_Sub_Weldment = 2367
    swCommands_Hole_Table_Expand_Same_Size = 2368
    swCommands_Hole_Table_Show_Centers = 2369
    swCommands_Hole_Table_Hide_Centers = 2370
    swCommands_View_Precise_Mode = 2371
    swCommands_View_Fast_Mode = 2372
    swCommands_Insert_Weldment = 2373
    swCommands_Edit_Sub_Weld_Props = 2374
    swCommands_Saveto_Separate_File = 2375
    swCommands_Tools_Macro_Mru_1 = 2376
    swCommands_Tools_Macro_Mru_2 = 2377
    swCommands_Tools_Macro_Mru_3 = 2378
    swCommands_Tools_Macro_Mru_4 = 2379
    swCommands_Tools_Macro_Mru_5 = 2380
    swCommands_Tools_Macro_Mru_6 = 2381
    swCommands_Tools_Macro_Mru_7 = 2382
    swCommands_Tools_Macro_Mru_8 = 2383
    swCommands_Tools_Macro_Mru_9 = 2384
    swCommands_Api_Menu_String_Macro = 2385
    swCommands_Helixdve_Revdir = 2386
    swCommands_Helix_Cw = 2387
    swCommands_Helix_Taperhelix = 2388
    swCommands_Helix_Ccw = 2389
    swCommands_Edit_Folder_Feat = 2390
    swCommands_Feature_Pop_Make_Weld_Bead = 2391
    swCommands_Feature_Pop_Suppress_Weld_Beads = 2392
    swCommands_Feature_Pop_Remove_Weld_Bead = 2393
    swCommands_Feature_Pop_Unsuppress_Weld_Beads = 2394
    swCommands_View_Fm_By_Dep_And_Feat = 2395
    swCommands_Insert_Advance_Helix_Creation = 2396
    swCommands_Route_Io_Output = 2397
    swCommands_Measure_Showcallouts = 2398
    swCommands_Activex_First = 2399
    swCommands_Debug_Api_Activex_Controls = 2400
    swCommands_Activex_1 = 2401
    swCommands_Activex_2 = 2402
    swCommands_Activex_3 = 2403
    swCommands_Activex_4 = 2404
    swCommands_Activex_10 = 2405
    swCommands_Activex_Last = 2406
    swCommands_Activex_5 = 2407
    swCommands_Activex_6 = 2408
    swCommands_Activex_7 = 2409
    swCommands_Activex_8 = 2410
    swCommands_Activex_9 = 2411
    swCommands_Ann_View_Item1 = 2412
    swCommands_Ann_View_Item2 = 2413
    swCommands_Ann_View_Item3 = 2414
    swCommands_Ann_View_Item4 = 2415
    swCommands_Ann_View_Item5 = 2416
    swCommands_Ann_View_Item6 = 2417
    swCommands_Ann_View_Item7 = 2418
    swCommands_Ann_View_Item8 = 2419
    swCommands_Ann_View_Item9 = 2420
    swCommands_Ann_View_Item10 = 2421
    swCommands_Ann_View_Item11 = 2422
    swCommands_Ann_View_Item12 = 2423
    swCommands_Ann_View_Item13 = 2424
    swCommands_Ann_View_Item14 = 2425
    swCommands_Ann_View_Item15 = 2426
    swCommands_Ann_View_Item16 = 2427
    swCommands_Ann_View_Item17 = 2428
    swCommands_Ann_View_Item18 = 2429
    swCommands_Ann_View_Item19 = 2430
    swCommands_Ann_View_Item20 = 2431
    swCommands_Show_Pgm_Untrimmed = 2432
    swCommands_Hide_Pgm_Untrimmed = 2433
    swCommands_Delete_Pgm_Sketch_Offset = 2434
    swCommands_Select_Open_Half_Loop = 2435
    swCommands_Debug_Enable_Dragdrop_Insert = 2436
    swCommands_Hole_Table_Show_Tags = 2437
    swCommands_Hole_Table_Hide_Tags = 2438
    swCommands_Dve_Rmb_Exit_Preview = 2439
    swCommands_Show_3d_Sketch_Triad = 2440
    swCommands_Move_Annotation_To_View = 2441
    swCommands_Orient_Annotation_View = 2442
    swCommands_Enable_Ann_View_Mode = 2443
    swCommands_Toggle_Smart_Dim_Mode = 2444
    swCommands_Toggle_Power_Dim_Mode = 2445
    swCommands_Toogle_Bwrtree = 2446
    swCommands_Route_Guide = 2447
    swCommands_Routing_Tools = 2448
    swCommands_Triad_Blob_Align_To = 2449
    swCommands_Content_Uponelevel = 2450
    swCommands_Mate_Graph_Debug_View = 2451
    swCommands_Assign_Smart_Fastener = 2452
    swCommands_Flip_Smart_Fastener = 2453
    swCommands_Near_Stack_Smart_Fastener = 2454
    swCommands_Far_Stack_Smart_Fastener = 2455
    swCommands_Properties_Smart_Fastener = 2456
    swCommands_Delete_Smart_Fastener = 2457
    swCommands_Open_Associated_Drw = 2458
    swCommands_Dve_Rmb_Select_Feature = 2459
    swCommands_Debug_Enable_2ptspline = 2460
    swCommands_Add_Derived_Configuration = 2461
    swCommands_Add_Smartfastener_String = 2462
    swCommands_Edit_Smart_Fastener = 2463
    swCommands_Mark_Smart_Fastener_Uptodate = 2464
    swCommands_Switch_To_Novice_Mode = 2465
    swCommands_Switch_To_Novice_Mode_List = 2466
    swCommands_Switch_To_Expert_Mode = 2467
    swCommands_Blank_Origin_Sketch = 2468
    swCommands_Unblank_Origin_Sketch = 2469
    swCommands_Dissolve_Sktext = 2470
    swCommands_Select_Chain = 2471
    swCommands_Rmb_Onto_Sketch = 2472
    swCommands_Rmb_Onto_Face = 2473
    swCommands_Rmb_Reverse = 2474
    swCommands_Rmb_Leader_Done = 2475
    swCommands_Mjl_Add_Horizontal_Bent = 2476
    swCommands_Debug_Test_Sizable_Plane_Manip = 2477
    swCommands_Hide_Sketch_Dim_In_Drawing = 2478
    swCommands_Show_Sketch_Dim_In_Drawing = 2479
    swCommands_Fit_Clearance = 2480
    swCommands_Fit_Transitional = 2481
    swCommands_Fit_Press = 2482
    swCommands_Fit_None = 2483
    swCommands_Fit_User = 2484
    swCommands_Blank_Pic_Feat = 2485
    swCommands_Unblank_Pic_Feat = 2486
    swCommands_Show_Feature_Name = 2487
    swCommands_Show_Feature_Des = 2488
    swCommands_Show_Comp_Filename = 2489
    swCommands_Show_Comp_Des = 2490
    swCommands_Show_Config_Name = 2491
    swCommands_Show_Configname_In_Configtree = 2492
    swCommands_Show_Configdes_In_Configtree = 2493
    swCommands_Show_Config_Previews = 2494
    swCommands_Start_Select_Contour = 2495
    swCommands_End_Select_Contour = 2496
    swCommands_Drawing_Feat_Edit_Def = 2497
    swCommands_Edit_Suppress_Feature = 2498
    swCommands_Edit_Unsuppress_Feature = 2499
    swCommands_Rmb_Delete_Manipulator = 2500
    swCommands_Fm_Flat_View = 2501
    swCommands_Edit_Rolltoprevious = 2502
    swCommands_Edit_Rolltoend = 2503
    swCommands_Insert_Detail_Centerline_From_Comp = 2504
    swCommands_Feature_Properties = 2505
    swCommands_Edit_Rolltoforward = 2506
    swCommands_Predefined_Add_Model = 2507
    swCommands_Dt_Save_Table = 2508
    swCommands_Dve_Uptobody = 2509
    swCommands_Generate_Region = 2510
    swCommands_Show_Config_Description = 2511
    swCommands_Create_Cut_List_Folder = 2512
    swCommands_Edit_Cut_List_Folder_Props = 2513
    swCommands_Start_Select_Contour_2 = 2514
    swCommands_Bom_Feat_Properties = 2515
    swCommands_Join_Contours = 2516
    swCommands_Mate_Delete = 2517
    swCommands_Mate_Remove = 2518
    swCommands_Body_Properties = 2519
    swCommands_Dve_Sketch_Message_Dlg = 2520
    swCommands_Addedit_Mate = 2521
    swCommands_Rmb_Loft_Synch_Hide = 2522
    swCommands_Rmb_Loft_Synch_Undo = 2523
    swCommands_Rmb_Loft_Synch_Hide_All = 2524
    swCommands_Rmb_Loft_Show_All = 2525
    swCommands_Hide_Dim_Witness = 2526
    swCommands_Show_Dim_Witness = 2527
    swCommands_Go_To_Mate_Component_1 = 2528
    swCommands_Hide_Mate_Component_1 = 2529
    swCommands_Show_Mate_Component_1 = 2530
    swCommands_Suppress_Mate_Component_1 = 2531
    swCommands_Resolve_Mate_Component_1 = 2532
    swCommands_Go_To_Mate_Component_2 = 2533
    swCommands_Hide_Mate_Component_2 = 2534
    swCommands_Show_Mate_Component_2 = 2535
    swCommands_Suppress_Mate_Component_2 = 2536
    swCommands_Resolve_Mate_Component_2 = 2537
    swCommands_Hide_Dim_Leader = 2538
    swCommands_Show_Dim_Leader = 2539
    swCommands_Explode_Delete = 2540
    swCommands_Explode_Dissolve_Group = 2541
    swCommands_Explode_Add_Sel_Comps_To_All = 2542
    swCommands_Explode_Add_Sel_Comps = 2543
    swCommands_Explode_Add_To_Group = 2544
    swCommands_Explode_Delete_Last_Step = 2545
    swCommands_Explode_Move_Before_Group_T = 2546
    swCommands_Explode_Reuse_Sub = 2547
    swCommands_Explode_Update_Sub = 2548
    swCommands_Explode_Reuse_Tree_Sub = 2549
    swCommands_Explode_Move_After_Group_T = 2550
    swCommands_Explode_Move_Before_Group_G = 2551
    swCommands_Explode_Move_After_Group_G = 2552
    swCommands_Explode_Tree_Edit = 2553
    swCommands_Explode_Manip_Edit = 2554
    swCommands_Collapseallitems_Tree = 2555
    swCommands_Hideshow_Brwser_Tree = 2556
    swCommands_Bom_Open_Comp_File = 2557
    swCommands_Router_Change_Mode = 2558
    swCommands_Router_Newloc = 2559
    swCommands_Flip_Direction = 2560
    swCommands_Component_Display = 2561
    swCommands_Comp_Display_Wireframe = 2562
    swCommands_Comp_Display_Hiddengreyed = 2563
    swCommands_Comp_Display_Hiddenremoved = 2564
    swCommands_Comp_Display_Shaded_With_Edges = 2565
    swCommands_Comp_Display_Shaded = 2566
    swCommands_Comp_Display_View_Default = 2567
    swCommands_Comp_Display_Hlr_Quality = 2568
    swCommands_Comp_Display_Reset = 2569
    swCommands_Create_Sub_Bodyfolder = 2570
    swCommands_Quick_Help_App_First = 2571
    swCommands_Quick_Help_App1 = 2572
    swCommands_Quick_Help_App2 = 2573
    swCommands_Quick_Help_App3 = 2574
    swCommands_Quick_Help_App4 = 2575
    swCommands_Quick_Help_App5 = 2576
    swCommands_Quick_Help_App6 = 2577
    swCommands_Quick_Help_App7 = 2578
    swCommands_Quick_Help_App8 = 2579
    swCommands_Quick_Help_App9 = 2580
    swCommands_Quick_Help_App10 = 2581
    swCommands_Quick_Help_App_Last = 2582
    swCommands_Block_Save_To_File = 2583
    swCommands__Docm_Preview = 2584
    swCommands__Fileexplorer_Open = 2585
    swCommands__Fileexplorer_Save = 2586
    swCommands__Fileexplorer_Save_All = 2587
    swCommands__Fileexplorer_Find_In_Vault_Pdmw = 2588
    swCommands__Fileexplorer_Checkin_This_Document_Pdmw = 2589
    swCommands__Fileexplorer_Checkin_From_Disk_Pdmw = 2590
    swCommands__Updatereload_From_Vault_Pdmw = 2591
    swCommands__Fileexplorer_Updatereload_All_From_Vault_Pdmw = 2592
    swCommands__Fileexplorer_Refresh = 2593
    swCommands_Internal_Dimension = 2594
    swCommands__File_Explorer_View = 2595
    swCommands__Fileexplorer_Docinfo_Pdmw = 2596
    swCommands_Toolbar_Electrical_Routing = 2597
    swCommands_View_Journal = 2598
    swCommands_Show_Feature_History = 2599
    swCommands_Suppress_Spline_Constraint_Error = 2600
    swCommands_Automatic_Cutlist = 2601
    swCommands_Update_Cutlist = 2602
    swCommands_Command_History = 2603
    swCommands_Shared_Tessellation_Method_0 = 2604
    swCommands_Shared_Tessellation_Method_1 = 2605
    swCommands_Shared_Tessellation_Method_2 = 2606
    swCommands_Shared_Tessellation_Method_3 = 2607
    swCommands_Deform_Rmb_Show_Connector = 2608
    swCommands_Deform_Rmb_Delete_Connector = 2609
    swCommands_Deform_Rmb_Delete_All_Connector = 2610
    swCommands_Rmb_Loft_Synch_Undo_Last_Oper = 2611
    swCommands_Content_Mgr_Open = 2612
    swCommands_Int_Tree_Ignore = 2613
    swCommands_Int_Tree_Open = 2614
    swCommands_Int_Tree_Unignore = 2615
    swCommands_Int_Tree_Zoom = 2616
    swCommands_Lock_Unlock_Focus = 2617
    swCommands_Lock_Unlock_Focus_Double_Click = 2618
    swCommands_Fe_Search = 2619
    swCommands_Fe_Reporting = 2620
    swCommands_Fe_Labels = 2621
    swCommands_Show_Table = 2622
    swCommands_Hide_Table = 2623
    swCommands_Fe_Docinfo = 2624
    swCommands__Savestreamscompressed = 2625
    swCommands_Fe_Refresh = 2626
    swCommands_Comp_Parent_Child_Rel = 2627
    swCommands_Start_Smart_Selection = 2628
    swCommands_End_Smart_Selection = 2629
    swCommands_Rmb_Loft_Mesh_Allfaces1 = 2630
    swCommands_Rmb_Loft_Mesh_Oneface1 = 2631
    swCommands_Rmb_Loft_Mesh_Clear_Allfaces1 = 2632
    swCommands_Rmb_Loft_Mesh_Clear_Oneface1 = 2633
    swCommands_Int_Tree_Coi_Int = 2634
    swCommands_Toolbar_Flexibletube_Routing = 2635
    swCommands_Toolbar_Piping_Routing = 2636
    swCommands_Routing_Main_Toolbar = 2637
    swCommands_Routing_Common_Toolbar = 2638
    swCommands_Toolbar_Electrical_Routing_New = 2639
    swCommands_Delete_Cut_List = 2640
    swCommands_Tolxpr_Show_Interference = 2641
    swCommands_Tolxpr_Hide_Interference = 2642
    swCommands_Anim_Suppress_Viewpoint = 2643
    swCommands_Anim_Lock_Viewpoint = 2644
    swCommands_Dim_Foreshort = 2645
    swCommands_Rmb_Appearance_Co = 2646
    swCommands_Rmb_Appearance_Pm = 2647
    swCommands_View_Appearance_Callout = 2648
    swCommands_Rmb_Appear_Callout_Edit_Color = 2649
    swCommands_Rmb_Appear_Callout_Edit_Texture = 2650
    swCommands_Rmb_Appear_Callout_Edit_Opt_Props = 2651
    swCommands_Rmb_Appear_Callout_Copy = 2652
    swCommands_Rmb_Appear_Callout_Cut = 2653
    swCommands_Rmb_Appear_Callout_Detach = 2654
    swCommands_Tx_Delete_Assy_Seq = 2655
    swCommands_Tx_Reset_Assy_Seq = 2656
    swCommands_Tx_Create_Assy_Seq = 2657
    swCommands_Pm_Holewiz_Close_Ok = 2658
    swCommands_Pm_Holewiz_Close_Undo = 2659
    swCommands_Rmb_Create_Hole_Series = 2660
    swCommands_Debug_Disable_Full_Mate_Solve = 2661
    swCommands_Swift_Fpo_Surf = 2662
    swCommands_Swift_Fpo_Plane = 2663
    swCommands_Swift_Fpo_Hole = 2664
    swCommands_Swift_Fpo_Compound = 2665
    swCommands_Swift_Fpo_Counterbore = 2666
    swCommands_Swift_Fpo_Contersink = 2667
    swCommands_Swift_Fpo_Blank = 2668
    swCommands_Swift_Fpo_Cone = 2669
    swCommands_Swift_Fpo_Cylinder = 2670
    swCommands_Swift_Fpo_Sphere = 2671
    swCommands_Swift_Fpo_Slot = 2672
    swCommands_Swift_Fpo_Width = 2673
    swCommands_Swift_Fpo_Pocket = 2674
    swCommands_Swift_Fpo_Pattern = 2675
    swCommands_Swift_Fpo_Ok = 2676
    swCommands_Remove_Smc_Reference = 2677
    swCommands_Rmb_Featappearance_Co = 2678
    swCommands_Rmb_Bodyappearance_Co = 2679
    swCommands_Rmb_Compappearance_Co = 2680
    swCommands_Sketchplane_Delete = 2681
    swCommands_Sketchplane_Deleteall = 2682
    swCommands_Sketchplane_Rename = 2683
    swCommands_Disable_Appearance_Co = 2684
    swCommands_Rmb_Appear_Callout_Delete_Face_Color = 2685
    swCommands_Rmb_Appear_Callout_Delete_Face_Texture = 2686
    swCommands_Rmb_Appear_Callout_Edit_Feat_Color = 2687
    swCommands_Rmb_Appear_Callout_Edit_Body_Color = 2688
    swCommands_Rmb_Appear_Callout_Edit_Part_Color = 2689
    swCommands_Rmb_Appear_Callout_Edit_Feat_Texture = 2690
    swCommands_Rmb_Appear_Callout_Edit_Body_Texture = 2691
    swCommands_Rmb_Appear_Callout_Edit_Part_Texture = 2692
    swCommands_Drawing_Feat_Edit = 2693
    swCommands_Rmb_Appear_Callout_Delete_Feat_Color = 2694
    swCommands_Rmb_Appear_Callout_Delete_Feat_Texture = 2695
    swCommands_Rmb_Appear_Callout_Delete_Body_Color = 2696
    swCommands_Rmb_Appear_Callout_Delete_Body_Texture = 2697
    swCommands_Rmb_Appear_Callout_Delete_Comp_Color = 2698
    swCommands_Rmb_Appear_Callout_Delete_Comp_Texture = 2699
    swCommands_Rmb_Appear_Callout_Delete_Part_Color = 2700
    swCommands_Rmb_Appear_Callout_Delete_Part_Texture = 2701
    swCommands_Rmb_Appear_Callout_Edit_Comp_Color = 2702
    swCommands_Rmb_Appear_Callout_Edit_Comp_Texture = 2703
    swCommands_Rmb_Enable_Appear_Callouts = 2704
    swCommands_Comp_Display_Wireframe_All = 2705
    swCommands_Comp_Display_Hiddengreyed_All = 2706
    swCommands_Comp_Display_Hiddenremoved_All = 2707
    swCommands_Comp_Display_Shaded_With_Edges_All = 2708
    swCommands_Comp_Display_Shaded_All = 2709
    swCommands_Comp_Display_View_Default_All = 2710
    swCommands_Comp_Display_Wireframe_Specify = 2711
    swCommands_Comp_Display_Hiddengreyed_Specify = 2712
    swCommands_Comp_Display_Hiddenremoved_Specify = 2713
    swCommands_Comp_Display_Shaded_With_Edges_Specify = 2714
    swCommands_Comp_Display_Shaded_Specify = 2715
    swCommands_Comp_Display_View_Default_Specify = 2716
    swCommands_Sheet_Tab_Popup_Rename = 2717
    swCommands_Nx_Select_Manager = 2718
    swCommands_Nx_Select_Manager_End = 2719
    swCommands_Nx_Sel_Loop = 2720
    swCommands_Nx_Sel_Group = 2721
    swCommands_Nx_Sel_Clear_All = 2722
    swCommands_Nx_Sel_Open_Loop = 2723
    swCommands_Nx_Sel_Region = 2724
    swCommands_Nx_Sel_Regular = 2725
    swCommands_Comp_Isolate = 2726
    swCommands_Sketch_Align_Grid_Origin = 2727
    swCommands_Drawing_Reload = 2728
    swCommands_Split_Cable = 2729
    swCommands_Blank_Atom_Body2 = 2730
    swCommands_Unblank_Atom_Body2 = 2731
    swCommands_Comp_Isolate_Exit = 2732
    swCommands__Debug_Pgm_Gtrim = 2733
    swCommands_Debug_Sos_Keep_Dcubed_Spline = 2734
    swCommands_Nx_Rmb_Ok = 2735
    swCommands_Nx_Rmb_Cancel = 2736
    swCommands_Nx_Rmb_Clear_All = 2737
    swCommands_Nx_Rmb_Sel_Regular = 2738
    swCommands_Nx_Rmb_Sel_Group = 2739
    swCommands_Nx_Rmb_Sel_Open_Loop = 2740
    swCommands_Nx_Rmb_Sel_Closed_Loop = 2741
    swCommands_Nx_Rmb_Sel_Region = 2742
    swCommands_Nx_Rmb_Push_Pin = 2743
    swCommands_Nx_Rmb_Auto_Ok = 2744
    swCommands_Swift_Multi_Select = 2745
    swCommands_Swift_Multi_Select_End = 2746
    swCommands_Debug_Enable_Horz_Nec = 2747
    swCommands_Debug_Enable_Nec_Modifydlg = 2748
    swCommands__Debug_Dont_Undo_Drag = 2749
    swCommands_Edit_Sketch_Belt = 2750
    swCommands_View_Mates_Transparency = 2751
    swCommands_Swift_Fpo_Notch = 2752
    swCommands_Swift_Fpo_Fillet = 2753
    swCommands_Swift_Fpo_Chamfer = 2754
    swCommands_Swift_Fpo_Boss = 2755
    swCommands_View_Showhide_Tb = 2756
    swCommands_Debug_Enable_Netfeat_Centerline = 2757
    swCommands_Publish_Dl_Content = 2758
    swCommands_Debug_Display_Tolerances = 2759
    swCommands_Debug_Allow_Sketch_Constraint_Tolerance = 2760
    swCommands_Quick_Reference_Guide = 2761
    swCommands_Pw_Material_Whatsnew_Help_Id = 2762
    swCommands_Pw_Options_Whatsnew_Help_Id = 2763
    swCommands_Pw_Scene_Whatsnew_Help_Id = 2764
    swCommands_Design_Checker_Learn_Checks_Whatsnew_Help_Id = 2765
    swCommands_Shader_Enableshadergenerator = 2766
    swCommands_See_What_Dcm_Sees = 2767
    swCommands_Shader_Enable_Scene_Env = 2768
    swCommands_Shader_Enable_True_Env = 2769
    swCommands_Shader_Enable_Rotating_Env = 2770
    swCommands_Debug_Acis_Kernel_Lofting = 2771
    swCommands_Debug_Noregen_Atload = 2772
    swCommands_Debug_Acis_Matched_Boolean = 2773
    swCommands_Debug_Mp_For_Surface = 2774
    swCommands_Debug_Acis_Sgnewspline_Periodic_Knots = 2775
    swCommands_Debug_Acis_Procedural_Curves = 2776
    swCommands_Debug_Acis_Timing_System = 2777
    swCommands_Insert_2dsketch_On_Plane = 2778
    swCommands_Shader_Enablerendermanager = 2779
    swCommands_Swift_Create_Basic_Dim = 2780
    swCommands_Debug_Vsta = 2781
    swCommands_Debug_Vsta_Show_Ide = 2782
    swCommands_Debug_Vsta_Load_Addins = 2783
    swCommands_Dummy = 2784
    swCommands_Dim_Stop_Break = 2785
    swCommands_Update_Msg = 2786
    swCommands_Heal_Faces_Ok = 2787
    swCommands_Keep_Constraints = 2788
    swCommands_FileClose = 2789
    swCommands_ToolsGrid = 2791
    swCommands_TrimCornerCorner = 2792
    swCommands_RectangleAtAngle = 2793
    swCommands_CentreRectangle = 2794
    swCommands_CentreRectangleAtAngle = 2795
    swCommands_WeldBead = 2796
    swCommands_Shader_Enable_Material_Editor_Realview_Shader_Page = 2797
    swCommands_Anim_Edit_Dim = 2798
    swCommands_Scene = 2799
    swCommands_ICE = 2800
    swCommands_SwiftAddTaStudy = 2801
    swCommands_List_Comp_References = 2802
    swCommands_List_Body_References = 2803
    swCommands_List_Feat_References = 2804
    swCommands_List_Face_References = 2805
    swCommands_List_Edge_References = 2806
    swCommands_List_Vert_References = 2807
    swCommands_Select_Display_State = 2808
    swCommands_Toolbar_Display_States = 2809
    swCommands_Show_Hidden_comps = 2810
    swCommands_Sw_Animatorpane = 2811
    swCommands_Toolbar_ScreenCapture = 2812
    swCommands_ScreenCaptureToolbar = 2813
    swCommands_ScreenCaptureAvi_Begin = 2814
    swCommands_ScreenCaptureAvi_End = 2815
    swCommands_Toolbar_Layout_Tools = 2816
    swCommands_Layout = 2817
    swCommands_Edit_Layout = 2818
    swCommands_Repeat_Mate = 2819
    swCommands_Edit_3DCC_Model = 2820
    swCommands_Edit_RV_Appearance = 2821
    swCommands_HoleAlignment = 2822
    swCommands_Add_Part_Block = 2823
    swCommands_Select_SubAssembly_In_GraphicsView = 2824
    swCommands_App_Exit = 2825
    swCommands_Insert_Cosmetic_Pattern = 2826
    swCommands_Animation_Duplicate = 2827
    swCommands_SimElementOn = 2828
    swCommands_SimElementOff = 2829
    swCommands_SimElementSuppress = 2830
    swCommands_SimElementUnsuppress = 2831
    swCommands_DriveWorkXxpress = 2832
    swCommands_DFMXpress = 2833
    swCommands_COSMOSFloXpress = 2834
    swCommands_RapidSketch = 2835
    swCommands_PlasticsFolder = 2836
    swCommands_DraftNsplit = 2837
    swCommands_Pin_Orientation_Dialog = 2838
    swCommands_Dim_Jog = 2839
    swCommands_Rmb_Display_Camera_FOV_Box = 2840
    swCommands_Fmt_Painter = 2841
    swCommands_PlasticsRegion = 2842
    swCommands_InsertLiveSection = 2843
    swCommands_LiveSectionFitToPart = 2844
    swCommands_LiveSectionReset = 2845
    swCommands_LiveSectionTriadShow = 2846
    swCommands_LiveSectionTriadHide = 2847
    swCommands_ClearanceVerification = 2848
    swCommands_MarkConvertedDocumentsDirty = 2849
    swCommands_HandSketch = 2850
    swCommands_StretchEntities = 2851
    swCommands_TitleBlockDefine = 2852
    swCommands_TitleBlockEdit = 2853
    swCommands_TitleBlockEnterData = 2854
    swCommands_Dotmenu_FacetContainer_Replace_Test = 2855
    swCommands_Fmt_Painter_Apply_All = 2856
    swCommands_FilterSketches = 2857
    swCommands_End_Adhoc_Rt = 2858
    swCommands_End_Pipe_Rt_Adhoc = 2859
    swCommands_End_Flex_Tube_Rt_Adhoc = 2860
    swCommands_Reimport_From_To_Lst = 2861
    swCommands_Insert_Connector = 2862
    swCommands_Dump_Signature = 2863
    swCommands_SketchSlot_Line = 2864
    swCommands_SketchSlot_Line_Center = 2865
    swCommands_SketchSlot_Arc3P = 2866
    swCommands_SketchSlot_Arc_Center = 2867
    swCommands_Unload_Hidden_Comps = 2868
    swCommands_ViewLiveSections = 2875
    swCommands_Debug_Beam_Analysis = 2876
    swCommands_PlasticsShelled = 2877
    swCommands_PlasticsUnShelled = 2878
    swCommands_PlasticsOpenShelled = 2879
    swCommands_Rotate_45_Degrees = 2880
    swCommands_InsertSketchEQCurve = 2881
    swCommands_SolidToSheetMetal = 2882
    swCommands_VisualizationTool = 2883
    swCommands_Create_Sub_LiveSectionFolder = 2884
    swCommands_AnalysistoolsDraftAnalysis = 2885
    swCommands_AnalysistoolsUndercutAnalysis = 2886
    swCommands_AnalysistoolsPartingLineAnalysis = 2887
    swCommands_LayoutDefault = 2888
    swCommands_LayoutWidescreen = 2889
    swCommands_LayoutDualMonitor = 2890
    swCommands_LayoutCustom = 2891
    swCommands_ToolsSensor = 2892
    swCommands_CircuitWorks = 2893
    swCommands_OfficeButtonTolAnalyst = 2894
    swCommands_Whats_New_Highlights = 2895
    swCommands_Body_RV_Appearance = 2896
    swCommands_Feature_RV_Appearance = 2897
    swCommands_Component_RV_Appearance = 2898
    swCommands_Part_RV_Appearance = 2899
    swCommands_Gantt_Zoomtofit = 2916
    swCommands_Animkey_EditTime = 2917
    swCommands_Animation_MoveCurTime = 2918
    swCommands_AnimEditTime_Dlg_Ok = 2919
    swCommands_AnimEditTime_Dlg_Cancel = 2920
    swCommands_AnimEditTime_Dlg_SetTime = 2921
    swCommands_AnimEditTime_Dlg_SetOffset = 2922
    swCommands_AnimEditTime_Dlg_Increment = 2923
    swCommands_Sm_Toggle_Flat_Display = 2924
    swCommands_ViewDecals = 2925
    swCommands_ChangeDisplayState = 2926
    swCommands_RigidGroups = 2927
    swCommands_InsertFeatureNudge = 2928
    swCommands_Animation_CancelSolver = 2929
    swCommands_Animation_SolverStatus = 2930
    swCommands_Publish_To_Edrawing = 2931
    swCommands_AnimMateSuppress = 2932
    swCommands_AnimMateUnsuppress = 2933
    swCommands_Remove_Feature_Appearance = 2934
    swCommands_Remove_Body_Appearance = 2935
    swCommands_Remove_Component_Appearance = 2936
    swCommands_Remove_Part_Appearance = 2937
    swCommands_HideShowEdges = 2938
    swCommands_Swift_Fpo_DimType_Linear = 2939
    swCommands_Swift_Fpo_DimType_Angular = 2940
    swCommands_Show_Graphics_Stats = 2941
    swCommands_Show_Graphics_Framecount = 2942
    swCommands_Debug_Draw_Sketch_Graphics_Hardware = 2943
    swCommands_Sm_Show_Problem_Areas = 2944
    swCommands_Sm_Clear_Problem_Areas = 2945
    swCommands_LayoutPresentation = 2946
    swCommands_Dotmenu_Render_In_PhotoView360 = 2947
    swCommands_Iso_draw_pipe_rt = 2948
    swCommands_TitleBlockTable = 2949
    swCommands_Whats_New_Pdf = 2950
    swCommands_Whats_New_Html = 2951
    swCommands_SageExpress = 2952
    swCommands_Design_Study = 2953
    swCommands_ViewDimNames = 2954
    swCommands_DesignStudy_Add_Parameters = 2955
    swCommands_Asm_Feat_Fillet = 2956
    swCommands_Asm_Feat_Chamfer = 2957
    swCommands_Asm_Feat_Cut_Sweep = 2958
    swCommands_Insert_Feature_Lock = 2959
    swCommands_Insert_Walkthrough = 2960
    swCommands_Exit_Measure = 2961
    swCommands_RenderToolbar = 2962
    swCommands_Toolbar_Render = 2963
    swCommands_Renumber_Hole_Table = 2964
    swCommands_Renumber_Series_Table = 2965
    swCommands_Invoke_PhotoviewRender = 2966
    swCommands_Edit_Scene = 2967
    swCommands_Render_Options = 2968
    swCommands_Final_Render = 2969
    swCommands_Schedule_Render = 2970
    swCommands_Recall_Last_Render = 2971
    swCommands_Debug_Dump_Virtual_Comps = 2972
    swCommands_DimensionSpaceEvenly = 2973
    swCommands_DimensionAlignCollinear = 2974
    swCommands_DimensionStagger = 2975
    swCommands_AutoArrangeDimension = 2976
    swCommands_DimensionTextAlignTop = 2977
    swCommands_DimensionTextAlignBottom = 2978
    swCommands_DimensionTextAlignLeft = 2979
    swCommands_DimensionTextAlignRight = 2980
    swCommands_Weld_Gap = 2981
    swCommands_GridFeature = 2982
    swCommands_ShowGuidelines = 2983
    swCommands_Simple_Route = 2984
    swCommands_Toolbar_Simple_Routing = 2985
    swCommands_Glassbox_Exit = 2986
    swCommands_Glassbox_Save = 2987
    swCommands_Glassbox_ViewOrient = 2988
    swCommands_Review_Pending_Updates = 2989
    swCommands_ViewPlaneSections = 2990
    swCommands_CosmeticWeld = 2991
    swCommands_ViewSimulationSymbol = 2992
    swCommands_NoteLPat = 2993
    swCommands_NoteCPat = 2994
    swCommands_Display_Simplified_Cosmetic_Weld_Curves = 2995
    swCommands_Display_Simplified_Cosmetic_Weld_Geometries = 2996
    swCommands_On_Show_Cosmetic_Welds = 2997
    swCommands_On_Hide_Cosmetic_Welds = 2998
    swCommands_Grid_View = 2999
    swCommands_Blank_Grid_Comp = 3000
    swCommands_Unblank_Grid_Comp = 3001
    swCommands_WeldTable = 3002
    swCommands_Add_Constraint_Planar_Offset = 3003
    swCommands_ViewCosmeticWeldSymbol = 3004
    swCommands_Invoke_Integrated_PhotoviewRender = 3005
    swCommands_SheetmetalCosting = 3006
    swCommands_MagnetLine = 3007
    swCommands_Open_Part = 3008
    swCommands_Open_Assembly = 3009
    swCommands_BendTable = 3010
    swCommands_Open_Sub_Assembly = 3011
    swCommands_Tube_Properties = 3012
    swCommands_Spool_Command = 3013
    swCommands_Unfreeze_All = 3014
    swCommands_Freeze_All = 3015
    swCommands_SearchHelp = 3016
    swCommands_SearchKB = 3017
    swCommands_SearchComunityForum = 3018
    swCommands_SearchCommands = 3019
    swCommands_SearchFilesAndModels = 3020
    swCommands_Show_Hidden_comps_Undo = 3021
    swCommands_Show_Hidden_comps_Exit = 3022
    swCommands_Isolate_Changed_Dims = 3023
    swCommands_ReplaceFormTool = 3024
    swCommands_Dimension_Driven_Toggle = 3025
    swCommands_Auto_Dimension_Toggle = 3026
    swCommands_Edit_Select_All = 3027
    swCommands_Machined_Parts_Costing = 3028
    swCommands_Numeric_Input_Toggle = 3029
    swCommands_Ambient_Occlusion = 3030
    swCommands_Select_Snapshot = 3031
    swCommands_Set_QuickView_Transparency = 3032
    swCommands_Selective_Open = 3033
    swCommands_Resolve_Top = 3034
    swCommands_Resolve_Top_LightWeight = 3035
    swCommands_PunchTable = 3036
    swCommands_RemoveAllDisplayStates = 3037
    swCommands_Selective_Open_LightWeight = 3038
    swCommands_Open_LightWeight = 3039
    swCommands_Manage_Equations = 3040
    swCommands_SweptFlange = 3041
    swCommands_Ok_Command = 3042
    swCommands_Cancel_Command = 3043
    swCommands_Spool_Tube_Command = 3044
    swCommands_SendTo = 3045
    swCommands_NextCmdMgrTab = 3046
    swCommands_PrevCmdMgrTab = 3047
    swCommands_Insert_Baseline_Dimension = 3048
    swCommands_Conic = 3049
    swCommands_Defeature = 3050
    swCommands_Insert_Sculpt = 3051
    swCommands_RevisionCloud = 3052
    swCommands_Copy_Appearance = 3053
    swCommands_Paste_Appearance = 3054
    swCommands_SaveWithPreBuiltConfigs = 3055
    swCommands_ChangeLayer = 3056
    swCommands_InsertCenterOfMass = 3057
    swCommands_PartReviewer = 3058
    swCommands_OnViewCenterOfMassSymbol = 3059
    swCommands_RebuildAndSaveConfig = 3060
    swCommands_RebuildAndSaveConfigOff = 3061
    swCommands_RebuildAndSaveConfigActive = 3062
    swCommands_RebuildAndSaveConfigAll = 3063
    swCommands_RebuildAndSaveConfigSpecific = 3064
    swCommands_Measure_PtoP = 3065
    swCommands_Measure_History = 3066
    swCommands_Dist_Custom = 3067
    swCommands_AngularOrdinateDimension = 3068
    swCommands_InsertCenterOfMassRefPoint = 3069
    swCommands_UpdateAllSpeedpakConfig = 3070
    swCommands_View_Rotate_About_Vertical = 3071
    swCommands_RMB_Blind_Direction_2 = 3072
    swCommands_RMB_UptoVertex_Direction_2 = 3073
    swCommands_RMB_UptoSurface_Direction_2 = 3074
    swCommands_RMB_OffsetFromSurface_Direction_2 = 3075
    swCommands_RMB_Throughall_Direction_2 = 3076
    swCommands_RMB_ThroughNext_Direction_2 = 3077
    swCommands_RMB_UptoBody_Direction_2 = 3078
    swCommands_RMB_Direction_2_OnOff = 3079
    swCommands_RMB_Reverse_Direction = 3080
    swCommands_View_Orientation_ViewBox = 3081
    swCommands_Edit_Ang_Ordinate = 3082
    swCommands_Re_Jog = 3083
    swCommands_Set_Current_View_As_Front = 3084
    swCommands_Set_Current_View_As_Back = 3085
    swCommands_Set_Current_View_As_Top = 3086
    swCommands_Set_Current_View_As_Bottom = 3087
    swCommands_Set_Current_View_As_Right = 3088
    swCommands_Set_Current_View_As_Left = 3089
    swCommands_LDR_Update_Model_Graphics = 3090
    swCommands_RemoveMarkAndPurgeDataForAllConfig = 3091
    swCommands_Dve_ThroughAll_Both = 3092
    swCommands_Insert_Light_Sunlight = 3093
    swCommands_Change_DrView_Reference = 3094
    swCommands_SolveAsFlexibleOrRigid = 3095
    swCommands_PathLengthDimension = 3096
    swCommands_Edit_Path_Length_Dim = 3097
    swCommands_LoopDve = 3098
    swCommands_CVSpline = 3099
    swCommands_InsertCV = 3100
    swCommands_DimensionPattern = 3101
    swCommands_SketchCreatePathLength = 3102
    swCommands_Add_Slope = 3103
    swCommands_ReplaceEntity = 3104
    swCommands_Toggle_Notes_UpperCase = 3105
    swCommands_Set_Dim_Extension_Centerline = 3106
    swCommands_Reset_Dim_Extension_Centerline = 3107
    swCommands_Component_Pattern_Sketch = 3108
    swCommands_Component_Pattern_Curve = 3109
    swCommands_Rmb_Find_Intersection = 3110
    swCommands_SMGusset = 3111
    swCommands_Corner_Relief = 3112
    swCommands_RefPlane_Flip_Normal = 3113
    swCommands_Restore_Settings = 3114
    swCommands_Render_Region = 3115
    swCommands_SelectConfigurations = 3116
    swCommands_ConfigurationsToolbar = 3117
    swCommands_Midpointline = 3118
    swCommands_ViewCompAnnotations = 3119
    swCommands_ViewAssemAnnotations = 3120
    swCommands_ZoomtoSheet = 3121
    swCommands_AutomaticUpdateCutlists = 3122
    swCommands_ConvertToStyle = 3123
    swCommands_ConvertToModif = 3124
    swCommands_Toggle_Magnified_Selection = 3125
    swCommands_Component_Pattern_Chain = 3126
    swCommands_On_Hold_Cosmetic_Welds_Rebuild = 3127
    swCommands_On_Rebuild_Cosmetic_Welds = 3128
    swCommands_Segment = 3129
    swCommands_CurvatureHedgehog = 3130
    swCommands_Add_to_CMarkSet = 3131
    swCommands_Rotate_Xaxis_By90 = 3132
    swCommands_Rotate_Yaxis_By90 = 3133
    swCommands_Rotate_Zaxis_By90 = 3134
    swCommands_Select_Annotation_View = 3135
    swCommands_Rename_Annotation_View = 3136
    swCommands_Reattach_to_CMarkSet = 3137
    swCommands_Reference_arrow = 3138
    swCommands_Surface_Flatten = 3139
    swCommands_MBD = 3140
    swCommands_Capture_3dView = 3141
    swCommands_MBD_Template_Editor = 3142
    swCommands_Electrical_EditConnector = 3143
    swCommands_Zone_Editor = 3144
    swCommands_Dynamic_Annotation_Views = 3145
    swCommands_OfficeButtonFlowSimulation = 3146
    swCommands_OfficeButtonPlastics = 3147
    swCommands_OfficeButtonInspection = 3148
    swCommands_Fixed_Length_Route = 3149
    swCommands_Show_Hide_Fixed_Length_Route_Manipulators = 3150
    swCommand_ReferenceArrow_PopUp = 3151
    swCommand_ChildReferenceArrow = 3152
    swCommands_Add_Constraint_SameCurvelen = 3153
    swCommands_UnUsed = 3154
    swCommand_Sheet_Format = 3155
    swCommand_Border_Editor = 3156
    swCommands_PhotoView_ProofSheet = 3157
    swCommand_Delete_Selected_BE = 3158
    swCommand_Restore_Selected_BE = 3159
    swCommand_Deselect_All_Selected_BE = 3160
    swCommands_Sort_Stacked_Balloons = 3161
    swCommand_TemporaryFixGroup = 3162
    swCommands_Create_Userdefined_Rt_By_Drag_Drop = 3163
    swCommands_Create_Userdefined_Rt_On_Fly = 3164
    swCommands_Userdefined_Add_Fitting = 3165
    swCommands_Userdefined_Rt_On_Fly = 3166
    swCommands_Edit_Userdefined_Start_At_Point = 3167
    swCommands_Userdefined_Rt_Properties = 3168
    swCommand_Hide_Show_Primary_Planes = 3169
    swCommand_Cartoon_Shading = 3170
    swCommand_Component_Preview_Window = 3171
    swCommands_AdvancedHoleWizard = 3172
    swCommands_InsertBoundingBox = 3173
    swCommands_SearchMySolidworks = 3174
    swCommands_SearchBlogs = 3175
    swCommands_SearchCadModels = 3176
    swCommands_SearchTraining = 3177
    swCommands_SearchTwitter = 3178
    swCommands_SearchYoutube = 3179
    swCommands_SearchManufacturers = 3180
    swCommands_InsertThreadWiz = 3181
    swCommands_SwiftInsertBasicDimension = 3182
    swCommands_AddFlagNoteToStack = 3183
    swCommands_ViewDatumReferenceFrame = 3184
    swCommands_MBD_Load_Unload = 3185
    swCommands_Pick_Identicalcomponents = 3186
    swCommands_Exit_Component_Preview = 3187
    swCommands_ToggleInstant2D = 3188
    swCommands_ShadedSketchContours = 3189
    swCommands_OffsetOnSurface = 3190
    swCommands_3dPrintValidation = 3191
    swCommands_Rmb_Cpat_Symmetric = 3192
    swCommands_User_Defined_Route = 3193
    swCommands_Routing_Reuse_Route = 3194
    swCommands_Display_States_Target = 3195
    swCommands_SMNormalCut = 3196
    swCommands_SwiftInsertBasicSizeDimension = 3197
    swCommands_PublishSTEP242File = 3198
    swCommands_Show_Config_Or_DisplayState_Name = 3199
    swCommands_RebuildAll = 3200
    swCommands_ViewSimResults = 3201
    swCommands_Rmb_Edit_SimResults = 3202
    swCommands_Show_LDR_Configuration = 3203
    swCommands_Mark_LDR_Config = 3204
    swCommands_Mark_LDR_ConfigOff = 3205
    swCommands_Mark_LDR_ConfigActive = 3206
    swCommands_Mark_LDR_ConfigAll = 3207
    swCommands_Mark_LDR_ConfigSpecific = 3208
    swCommands_Remove_Mark_LDR_AndPurgeDataForAllConfig = 3209
    swCommands_Show_Mesh_Feat = 3210
    swCommands_Hide_Mesh_Feat = 3211
    swCommands_3dpmi = 3212
    swCommands_Rmb_Cpat_Equal_Spacing1 = 3213
    swCommands_Rmb_Cpat_Equal_Spacing2 = 3214
    swCommands_Asset_Publish = 3215
    swCommands_Toggle_MagMate = 3216
    swCommands_Ground_Plane = 3217
    swCommands_SurfFromMesh = 3218
    swCommands_changeSubDTransparency = 3219
    swCommands_toggleSubDCage = 3220
    swCommands_toggleSelectedVisibleSubdElements = 3221
    swCommands_filterAnySubDEntities = 3222
    swCommands_filterSubdVerts = 3223
    swCommands_filterSubdEdges = 3224
    swCommands_filterSubdFaces = 3225
    swCommands_filterSubdEdgeRings = 3226
    swCommands_filterSubdEdgeLoops = 3227
    swCommands_filterSubdFaceLoops = 3228
    swCommands_Start_Screen = 3229
    swCommands_FilterMeshFacet = 3230
    swCommands_FilterMeshFin = 3231
    swCommands_FilterMeshVertex = 3232
    swCommands_GeneralToleranceTable = 3233
    swCommands_TabAndSlot = 3234
    swCommands_HandsketchPen = 3235
    swCommands_HandsketchEraser = 3236
    swCommands_HandsketchSelect = 3237
    swCommands_HandsketchColor = 3238
    swCommands_HandsketchThickness = 3239
    swCommands_HandsketchConvertShape = 3240
    swCommands_HandsketchConvertEntity = 3241
    swCommands_Toolbar_Handsketch = 3242
    swCommands_InsertHandSketch = 3243
    swCommands_InsertAutoDim = 3244
    swCommands_ConvertMeshSolidSurface = 3245
    swCommands_ToggleGraphicsDisplay = 3246
    swCommands_AlignRobotToSelection = 3247
    swCommands_AlignRobotToUCS = 3248
    swCommands_AlignRobotToScreen = 3249
    swCommands_Publish_3DByMe = 3250
    swCommands_InsertSubdQuadBall = 3251
    swCommands_PreInsertSubdQuadBall = 3252
    swCommands_InsertSubdBox = 3253
    swCommands_PreInsertSubdBox = 3254
    swCommands_InsertSubdCylinder = 3255
    swCommands_PreInsertSubdCylinder = 3256
    swCommands_InsertSubdGlobe = 3257
    swCommands_PreInsertSubdGlobe = 3258
    swCommands_InsertSubdTorus = 3259
    swCommands_PreInsertSubdTorus = 3260
    swCommands_InsertSubdCone = 3261
    swCommands_PreInsertSubdCone = 3262
    swCommands_InsertSubdRectangle = 3263
    swCommands_PreInsertSubdRectangle = 3264
    swCommands_InsertSubdDisk = 3265
    swCommands_PreInsertSubdDisk = 3266
    swCommands_InsertSubdRing = 3267
    swCommands_PreInsertSubdRing = 3268
    swCommands_InsertSubdMerge = 3269
    swCommands_PreInsertSubdMerge = 3270
    swCommands_InsertSubdSymmetry = 3271
    swCommands_PreInsertSubdSymmetry = 3272
    swCommands_InsertSubdExtrudeFace = 3273
    swCommands_PreInsertSubdExtrudeFace = 3274
    swCommands_InsertSubdSubDDivideFace = 3275
    swCommands_PreInsertSubdSubDDivideFace = 3276
    swCommands_InsertSubdSubDCrease = 3277
    swCommands_PreInsertSubdSubDCrease = 3278
    swCommands_InsertSubdInsertLoop = 3279
    swCommands_PreInsertSubdInsertLoop = 3280
    swCommands_InsertSubdDeleteLoop = 3281
    swCommands_PreInsertSubdDeleteLoop = 3282
    swCommands_InsertSubdSubDAlign = 3283
    swCommands_PreInsertSubdSubDAlign = 3284
    swCommands_InsertSubdSubDScale = 3285
    swCommands_PreInsertSubdSubDScale = 3286
    swCommands_Toolbar_Freeform = 3287
    swCommands_3dExperienceDesignEngineer = 3288
    swCommands_Toolbar_OneClick = 3289
    swCommands_HandsketchTouch = 3290
    swCommands_HandsketchRuler = 3291
    swCommands_Subd_CreateBridgeHole = 3292
    swCommands_Subd_MergeFacesSubdivide = 3293
    swCommands_Subd_BtnReverseDir = 3294
    swCommands_HandsketchPenProps = 3295
    swCommands_AutoExplodeLine = 3296
    swCommands_InsertSubdSubDQuickCrease = 3298
    swCommands_InsertSubdSubDQuickInsertLoop = 3299
    swCommands_InsertSubdSubDQuickAlign = 3300
    swCommands_InsertSubdSubDQuickExtrudeFace = 3301
    swCommands_InsertSubdSubDQuickSubdivide = 3302
    swCommands_Import_Swift_Schema = 3303
    swCommands_Reverse_Endpoint_Tangency = 3304
    swCommands_Mating_Component = 3305
    swCommands_DissolveEntities = 3306
    swCommands_DissolveAutoExplodeLine = 3307
    swCommands_HandsketchUpdateToShape = 3308
    swCommands_HandsketchUpdateToEntity = 3309
    swCommands_SelectOverGeometry = 3310
    swCommands__Force_Rebuild_All = 3311
    swCommands_InsertSubdFillHole = 3312
    swCommands_InvertSubDSelection = 3313
    swCommands_ClearSubDSelection = 3314
    swCommands_EditSubDMerge = 3315
    swCommands_InsertSubdSubDQuickDelete = 3316
    swCommands_XRayToggleAssem = 3317
    swCommands_XRayTogglePart = 3318
    swCommands_RMBFreeshapeOK = 3319
    swCommands_RMBFreeshapeCancel = 3320
    swCommands_MixModel_Resolve = 3321
    swCommands_MixModel_LightWeight = 3322
    swCommands_ViewGlobalBBox = 3323
    swCommands_SubdConvertMesh = 3324
    swCommands_SwiftInsertGeneralProfileTolerance = 3325
    swCommands_ForceMateMisalignment = 3326
    swCommands_RemoveMateMisalignment = 3327
    swCommands_InsertSubdExtrude = 3328
    swCommands_InsertSubdRevolve = 3329
    swCommands_InsertSubdSweep = 3330
    swCommands_Make_Trim_As_Construction = 3331
    swCommands_Ignore_Construction_Geom = 3332
    swCommands_3dTexturizeSolidSurface = 3333
    swCommands_Toolbar_Adv_Struct_System = 3334
    swCommands_AdvancedStructuralMember = 3335
    swCommands_PrimaryAdvStructMember = 3336
    swCommands_SecondaryAdvStructMember = 3337
    swCommands_CornerMgmtAdvStructMember = 3338
    swCommands_Explode_Roll_Back = 3339
    swCommands_Explode_Roll_Forward = 3340
    swCommands_Explode_Roll_To_Previous = 3341
    swCommands_Explode_Roll_To_End = 3342
    swCommands_UpdateImportedModel = 3343
    swCommands_HandsketchReplaceSpline = 3344
    swCommands_HandsketchReplaceComposite = 3345
    swCommands_HandsketchReplaceSlot = 3346
    swCommands_HandsketchReplaceEllipse = 3347
    swCommands_Explode_Suppress = 3348
    swCommands_Explode_Unsuppress = 3349
    swCommands_PostInsertSubdExtrude = 3350
    swCommands_PostInsertSubdRevolve = 3351
    swCommands_RemovedSection = 3352
    swCommands_Iso_Draw_Electrical_Rt = 3353
    swCommands_InsertFreeShapeConvertMesh = 3354
    swCommands_PostInsertSubdSweep = 3355
    swCommands_SolidWorks_backoffice = 3356
    swCommands_SegmentImportedMeshBody = 3357
    swCommands_Enable_RenderSystem_Profiling = 3358
    swCommands_Capture_RenderSystem_ProfilingData = 3359
    swCommands_DeleteHoleSurface = 3360
    swCommands_Dotmenu_Test_Graphics_Performance = 3361
    swCommands_TrimAsGroupWithPreAdvStructMember = 3362
    swCommands_TrimAsIndAdvStructMember = 3363
    swCommands_ConvertToGeneric = 3364
    swCommands_MostRecentlyUsed_File1 = 3365
    swCommands_MostRecentlyUsed_File2 = 3366
    swCommands_MostRecentlyUsed_File3 = 3367
    swCommands_MostRecentlyUsed_File4 = 3368
    swCommands_MostRecentlyUsed_File5 = 3369
    swCommands_MostRecentlyUsed_File6 = 3370
    swCommands_MostRecentlyUsed_File7 = 3371
    swCommands_MostRecentlyUsed_File8 = 3372
    swCommands_MostRecentlyUsed_File9 = 3373
    swCommands_MostRecentlyUsed_File10 = 3374
    swCommands_MostRecentlyUsed_File11 = 3375
    swCommands_MostRecentlyUsed_File12 = 3376
    swCommands_MostRecentlyUsed_File13 = 3377
    swCommands_MostRecentlyUsed_File14 = 3378
    swCommands_MostRecentlyUsed_File15 = 3379
    swCommands_MostRecentlyUsed_File16 = 3380
    swCommands_HandsketchProtractor = 3381
    swCommands_Fixed_Length_Covering = 3382
    swCommands_Rmb_BiDir = 3383
    swCommands_OfficeAddin3dExperienceMarketPlace = 3384
    swCommands_Explode_Done_With_Step = 3385
    swCommands_ProfileProperties = 3386
    swCommands_HandsketchSplineMode = 3387
    swCommands_AlternativeHandwrittenDim_0 = 3388
    swCommands_AlternativeHandwrittenDim_1 = 3389
    swCommands_AlternativeHandwrittenDim_2 = 3390
    swCommands_AlternativeHandwrittenDim_3 = 3391
    swCommands_AlternativeHandwrittenDim_4 = 3392
    swCommands_AlternativeHandwrittenDim_5 = 3393
    swCommands_AlternativeHandwrittenDim_6 = 3394
    swCommands_AlternativeHandwrittenDim_7 = 3395
    swCommands_AlternativeHandwrittenDim_8 = 3396
    swCommands_AlternativeHandwrittenDim_9 = 3397
    swCommands_InkMarkupView = 3398
    swCommands_SketchSlicing = 3399
    swCommands_3DPDF_ADD_ALL_3DVIEWS = 3401
    swCommands_AssemblyAdd = 3402
    swCommands_AssemblyAddRoute = 3403
    swCommands_Exit_Structural_Member = 3404
    swCommands_Insert_Chain_Dimension = 3405
    swCommands_AddTo_Chain_Dimension = 3406
    swCommands_ConvertTo_Chain_Dimension = 3407
    swCommands_ConvertTo_Base_Dimension = 3408
    swCommands_HandsketchModify = 3409
    swCommands_StackFasteners = 3410
    swCommands_BodyComparison = 3411
    swCommands_Remove_From_ChainDim = 3412
    swCommands_HandsketchEditModify = 3413
    swCommands_SkSilhouetteEnts = 3414
    swCommands_DefineStructConnection = 3415
    swCommands_Envelope_Publisher = 3416
    swCommands_Online_Familytable_Closed = 3417
    swCommands_ActivateFlexiblePartComp = 3418
    swCommands_Make_Edit_Sketch = 3419
    swCommands_Make_Reference_Sketch = 3420
    swCommands_EditFlexiblePartComp = 3421
    swCommands_ViewCompEnvelopes = 3422
    swCommands_ViewAssemEnvelopes = 3423
    swCommands_Add_OverallDim_To_ChainDim = 3424
    swCommands_Add_Constraint_G3Touch = 3425
    swCommands_HandsketchReplaceChamfer = 3426
    swCommands_HandsketchReplaceFillet = 3427
    swCommands_HandsketchReplaceExtend = 3428
    swCommands_DecimateMesh = 3429
    swCommands_Flexible_Part_Remove_Ref = 3430
    swCommands_CutListSortingOptions = 3431
    swCommands_SWPremium = 3432
    swCommands_SimulationStd = 3433
    swCommands_SimulationPro = 3434
    swCommands_SimulationPremium = 3435
    swCommands_LockViewPlane = 3436
    swCommands_Toolbar_Inkmarkup = 3437
    swCommands_InkMarkupPenProps = 3438
    swCommands_InkMarkupPen = 3439
    swCommands_InkMarkupMouse = 3440
    swCommands_InkMarkupEraser = 3441
    swCommands_InkMarkupSelect = 3442
    swCommands_InkMarkupTouch = 3443
    swCommands_InkMarkupText = 3444
    swCommands_InsertStructConnection = 3445
    swCommands_GetSupport = 3446
    swCommands_Resolve_Drawing = 3447
    swCommands_YUpViewOrientation = 3448
    swCommands_ZUpViewOrientation = 3449
    swCommands_SwiftInsertDatumTarget = 3450
    swCommands_Publish3DPDF = 3451
    swCommands_InsertNewFamilyMember = 3452
    swCommands_InsertNewRepresentation = 3453
    swCommands_InsertNewPrivateFamilyMember = 3454
    swCommands_HandsketchDraw = 3455
    swCommands_SaveWithOptions = 3456
    swCommands_SaveLocally = 3457
    swCommands_Show_ComponentInstance_Name = 3458
    swCommands_Show_ComponentReference_Name = 3459
    swCommands_Show_Representation_Name = 3460
    swCommands_Show_CADFamily_Name = 3461
    swCommands_Show_Revision_And_Maturity = 3462
    swCommands_User_Communities = 3463
    swCommands_Save_Virtual_Comp = 3464
    swCommands_Sw_Educator_Resources = 3465
    swCommands_InsertAbbrView = 3466
    swCommands_SwiftInsertAngleDimension = 3467
    swCommands_ViewBendLines = 3468
    swCommands_SmoothMesh = 3469
    swCommands_Dim_RadialDiametric_Toggle = 3470
    swCommands_Skey_SearchBox = 3471
    swCommands_PLM_Reserve = 3472
    swCommands_PLM_Unreserve = 3473
    swCommands_PLM_Reload_fromServer = 3474
    swCommands_PLM_Replace_By_Revision = 3475
    swCommands_PLM_Maturity = 3476
    swCommands_PLM_New_Revision = 3477
    swCommands_PLM_Move_to = 3478
    swCommands_PLM_Properties = 3479
    swCommands_PLM_Relations = 3480
    swCommands_PLM_Replace_Content = 3481
    swCommands_PLM_Set_Ent_Item_Number = 3482
    swCommands_PLM_Gen_Derived_Output_Number = 3483
    swCommands_Toolbar_Lifecycle_And_Collaboration = 3484
    swCommands_Disp_Dim_As_Radius = 3485
    swCommands_Disp_Dim_As_Diameter = 3486
    swCommands_Disp_Dim_As_Linear = 3487
    swCommands_On_Screen_Dim_Dialog = 3488
    swCommands_InsertStudWiz = 3489
    swCommands_InsertSymmDiaDim = 3490
    swCommands_PlasticsStd = 3491
    swCommands_PlasticsPro = 3492
    swCommands_PlasticsPremium = 3493
    swCommands_MakeVirtualCompIndependent = 3494
    swCommands_OpenFromPC = 3495
    swCommands_Publish_HomeByMe = 3496
    swCommands_Open_Detailing_Drw = 3497
    swCommands_Insert_From_PartSupply = 3498
    swCommands_On_Demand_Maufacturing = 3499
    swCommands_SwConnected_Release_Notes = 3500
    swCommands_Work_Offline = 3501
    swCommands_Publish_3DSwym_Picture = 3502
    swCommands_Publish_3DSwym_3D = 3503
    swCommands_Force_Regen_Bucket = 3504
    swCommands_Bom_Open_Draw_File = 3505
    swCommands_Open_Partdrawg_For_Drawing = 3506
    swCommands_FlowSimulation = 3507
    swCommands_FlowSimulation_HVAC = 3508
    swCommands_FlowSimulation_ElCooling = 3509
    swCommands_FlowSimulation_HVAC_ElCooling = 3510
    swCommands_PatternStructConnection = 3511
    swCommands_AutoRepair_Mates = 3512
    swCommands_LaunchFilePrep_Asst = 3513
    swCommands_Add_To_Bookmark = 3514
    swCommands_Open_Bookmark_Editor = 3515
    swCommands_Share_A_File = 3516
    swCommands_Propagate_Slots = 3517
    swCommands_SMStamp = 3518
    swCommands_Preview_Sketch_Dimension_Toggle = 3519
    swCommands_AutoRepair_Pattern = 3520
    swCommands_Reattach_Dim = 3521
    swCommands_Dim_Restore_Original_Value = 3522
    swCommands_PreviousVersionCheck = 3523
    swCommands_Share = 3524
    swCommands_Add_To_Recent_Bookmark = 3525
    swCommands_Copy_Bookmark_Link = 3526
    swCommands_SimulationDesigner = 3527
    swCommands_Hide_3d_Sketch_Triad = 3528
    swCommands_FlatPatternBendNotch = 3529
    swCommands_GrooveWeld = 3530
    swCommands_ConvertMeshBody2Classic = 3531
    swCommands_SWUltimate = 3532
    swCommands_CPQ_CreateVariabilityFeatures = 3533
    swCommands_OpenCollaborativeTask = 3534
    swCommands_Flip_Endpoint_Tangency = 3535
    swCommands_AutoGenerateDrawing = 3536
    swCommands_InsertFamilyTable_Drw = 3537
    swCommands_View_ShowAnnotationTextExpression = 3538
    swCommands_Dim_UpdateBreak = 3539
    swCommands_Dim_AddBreak = 3540
    swCommands_CmdPrediction_Search_Cmd = 3541
    swCommands_SWVisualize = 3542
    swCommands_Invoke_SWVisualize_Render_PM = 3543
    swCommands_OpenIn_SWVisualize = 3544
    swCommands_SWVisualize_GroupByAppearance = 3545
    swCommands_SWVisualize_GroupByPart = 3546
    swCommands_SWVisualize_ImportWithOptions = 3547
    swCommands_CreateNewTask = 3548
    swCommands_SwiftInsertOrdinateDimension = 3549
    swCommands_Highlight = 3550
    swCommands_AutoUpdateDrawing = 3551

class swCompatibilityDialogOptions_e(IntEnum):
    """swCompatibilityDialogOptions_e (3 constants, from SwConst)."""
    swCompatibilityDialogOptions_AlwaysShow = 0
    swCompatibilityDialogOptions_ShowOnIncompatible = 1
    swCompatibilityDialogOptions_NeverShow = 2

class swComponentCrossSectionType_e(IntEnum):
    """swComponentCrossSectionType_e (3 constants, from SWRoutingLib)."""
    swRectangularCrossSection = 1000
    swCircularCrossSection = 1010
    swNotHVAC = 1020

class swComponentIdentifier_e(IntEnum):
    """swComponentIdentifier_e (11 constants, from SwConst)."""
    swComponentIdentifier_None = 0
    swComponentIdentifier_PhysicalProductTitle = 1
    swComponentIdentifier_ComponentName = 2
    swComponentIdentifier_ComponentDescription = 4
    swComponentIdentifier_EnterpriseItemNumber = 8
    swComponentIdentifier_PhysicalProductDescription = 16
    swComponentIdentifier_ConfigurationName = 32
    swComponentIdentifier_ConfigurationDescription = 64
    swComponentIdentifier_DisplayStateName = 128
    swComponentIdentifier_FileTitle = 256
    swComponentIdentifier_PLMRevision = 512

class swComponentLoadStatus_e(IntEnum):
    """swComponentLoadStatus_e (3 constants, from SwConst)."""
    swComponentLoadStatus_Unknown = 0
    swComponentLoadStatus_Hidden = 1
    swComponentLoadStatus_Suppressed = 2

class swComponentReloadError_e(IntEnum):
    """swComponentReloadError_e (17 constants, from SwConst)."""
    swReloadOkay = 0
    swWriteAccessError = 1
    swFutureVersionError = 2
    swModifiedNotReloadedError = 3
    swInvalidOption = 4
    swFileNotSavedError = 5
    swInvalidComponentError = 6
    swUnexpectedError = 7
    swComponentLightWeightError = 8
    swFileDoesntExistError = 9
    swFileInvalidOrSameNameError = 10
    swDocumentHasNoView = 11
    swDocumentAlreadyOpenedError = 12
    swDocumentEventError = 13
    swDocumentNotChanged = 14
    swReloadCancel = 15
    swReadOnlyChanged = 16

class swComponentReloadOption_e(IntEnum):
    """swComponentReloadOption_e (2 constants, from SwConst)."""
    swAlwaysReload = 0
    swDontReloadOldComponents = 1

class swComponentResolveStatus_e(IntEnum):
    """swComponentResolveStatus_e (4 constants, from SwConst)."""
    swResolveOk = 0
    swResolveAbortedByUser = 1
    swResolveNotPerformed = 2
    swResolveError = 3

class swComponentRouteType_e(IntEnum):
    """swComponentRouteType_e (6 constants, from SWRoutingLib)."""
    swFabricatedPipe = 1
    swTube = 2
    swElectrical = 3
    swMixedRouteType = 4
    swUnknownType = 5
    swUserDefinedType = 6

class swComponentSolvingOption_e(IntEnum):
    """swComponentSolvingOption_e (2 constants, from SwConst)."""
    swComponentRigidSolving = 0
    swComponentFlexibleSolving = 1

class swComponentSuppressionState_e(IntEnum):
    """swComponentSuppressionState_e (6 constants, from SwConst)."""
    swComponentSuppressed = 0
    swComponentLightweight = 1
    swComponentFullyResolved = 2
    swComponentResolved = 3
    swComponentFullyLightweight = 4
    swComponentInternalIdMismatch = 5

class swComponentVisibilityState_e(IntEnum):
    """swComponentVisibilityState_e (3 constants, from SwConst)."""
    swComponentHidden = 0
    swComponentVisible = 1
    swComponentUnknown = -1

class swConcentricAlignmentType_e(IntEnum):
    """swConcentricAlignmentType_e (4 constants, from SwConst)."""
    swConcentricAlignConcentric = 0
    swConcentricAlignThisMate = 1
    swConcentricAlignLinkedMate = 2
    swConcentricAlignSymmetric = 3

class swConcentricPositionType(IntEnum):
    """swConcentricPositionType (3 constants, from SwConst)."""
    swConcentricPositionType_Default = -1
    swConcentricPositionType_Aligned = 0
    swConcentricPositionType_Symmetric = 1

class swConfigTreeSortType_e(IntEnum):
    """swConfigTreeSortType_e (4 constants, from SwConst)."""
    swSortType_History = 0
    swSortType_Numeric = 1
    swSortType_Literal = 2
    swSortType_DesignTable = 3

class swConfigurationChangeTypes_e(IntEnum):
    """swConfigurationChangeTypes_e (16 constants, from SwConst)."""
    swConfigurationChangeTypes_Undefined = -1
    swConfigurationChangeTypes_DimensionValue = 0
    swConfigurationChangeTypes_SuppressionState = 1
    swConfigurationChangeTypes_AddChildConfiguration = 2
    swConfigurationChangeTypes_RemoveChildConfiguration = 3
    swConfigurationChangeTypes_ComponentVisibilityState = 4
    swConfigurationChangeTypes_CustomProperty = 5
    swConfigurationChangeTypes_AddDisplayState = 6
    swConfigurationChangeTypes_RemoveDisplayState = 7
    swConfigurationChangeTypes_RenameDisplayState = 8
    swConfigurationChangeTypes_Feature = 9
    swConfigurationChangeTypes_Unused1 = 10
    swConfigurationChangeTypes_Unused2 = 11
    swConfigurationChangeTypes_ConvertToRepresentation = 12
    swConfigurationChangeTypes_ConvertToPhysicalProduct = 13
    swConfigurationChangeTypes_ChangeRepresentationParent = 14

class swConfigurationOptions2_e(IntEnum):
    """swConfigurationOptions2_e (10 constants, from SwConst)."""
    swConfigOption_UseAlternateName = 1
    swConfigOption_DontShowPartsInBOM = 2
    swConfigOption_SuppressByDefault = 4
    swConfigOption_HideByDefault = 8
    swConfigOption_MinFeatureManager = 16
    swConfigOption_InheritProperties = 32
    swConfigOption_LinkToParent = 64
    swConfigOption_DontActivate = 128
    swConfigOption_DoDisolveInBOM = 256
    swConfigOption_UseDescriptionInBOM = 512

class swConfigurationOptions_e(IntEnum):
    """swConfigurationOptions_e (2 constants, from SwConst)."""
    swUseAlternateName = 1
    swDontShowPartsInBOM = 2

class swConfigurationType_e(IntEnum):
    """swConfigurationType_e (6 constants, from SwConst)."""
    swConfiguration_Standard = 0
    swConfiguration_AsMachined = 1
    swConfiguration_AsWelded = 2
    swConfiguration_SheetMetal = 3
    swConfiguration_SpeedPak = 4
    swConfiguration_Defeature = 5

class swConnectedSegmentsOption_e(IntEnum):
    """swConnectedSegmentsOption_e (2 constants, from SwConst)."""
    swConnectedSegments_SimpleCut = 1
    swConnectedSegments_CopedCut = 2

class swConnectedSyncSettingsErrors_e(IntEnum):
    """swConnectedSyncSettingsErrors_e (4 constants, from SwConst)."""
    swConnectedSyncSettings_Success = 0
    swConnectedSyncSettings_ConnectedDisabled = 1
    swConnectedSyncSettings_ConnectedNotLoggedIn = 2
    swConnectedSyncSettings_UploadDownloadError = 3

class swConnectionPointType_e(IntEnum):
    """swConnectionPointType_e (4 constants, from SwConst)."""
    swConnectionPoint_Tube = 1
    swConnectionPoint_FabricatedPipe = 2
    swConnectionPoint_Electrical = 3
    swConnectionPoint_UserDefined = 4

class swConstrainedCornerAction_e(IntEnum):
    """swConstrainedCornerAction_e (4 constants, from SwConst)."""
    swConstrainedCornerInteract = 0
    swConstrainedCornerKeepGeometry = 1
    swConstrainedCornerDeleteGeometry = 2
    swConstrainedCornerStopProcessing = 3

class swConstrainedStatus_e(IntEnum):
    """swConstrainedStatus_e (7 constants, from SwConst)."""
    swUnknownConstraint = 1
    swUnderConstrained = 2
    swFullyConstrained = 3
    swOverConstrained = 4
    swNoSolution = 5
    swInvalidSolution = 6
    swAutosolveOff = 7

class swConstraintType_e(IntEnum):
    """swConstraintType_e (86 constants, from SwConst)."""
    swConstraintType_INVALIDCTYPE = 0
    swConstraintType_DISTANCE = 1
    swConstraintType_ANGLE = 2
    swConstraintType_RADIUS = 3
    swConstraintType_HORIZONTAL = 4
    swConstraintType_VERTICAL = 5
    swConstraintType_TANGENT = 6
    swConstraintType_PARALLEL = 7
    swConstraintType_PERPENDICULAR = 8
    swConstraintType_COINCIDENT = 9
    swConstraintType_CONCENTRIC = 10
    swConstraintType_SYMMETRIC = 11
    swConstraintType_ATMIDDLE = 12
    swConstraintType_ATINTERSECT = 13
    swConstraintType_SAMELENGTH = 14
    swConstraintType_DIAMETER = 15
    swConstraintType_OFFSETEDGE = 16
    swConstraintType_FIXED = 17
    swConstraintType_ARCANG90 = 18
    swConstraintType_ARCANG180 = 19
    swConstraintType_ARCANG270 = 20
    swConstraintType_ARCANGTOP = 21
    swConstraintType_ARCANGBOTTOM = 22
    swConstraintType_ARCANGLEFT = 23
    swConstraintType_ARCANGRIGHT = 24
    swConstraintType_HORIZPOINTS = 25
    swConstraintType_VERTPOINTS = 26
    swConstraintType_COLINEAR = 27
    swConstraintType_CORADIAL = 28
    swConstraintType_SNAPGRID = 29
    swConstraintType_SNAPLENGTH = 30
    swConstraintType_SNAPANGLE = 31
    swConstraintType_USEEDGE = 32
    swConstraintType_ELLIPSEANG90 = 33
    swConstraintType_ELLIPSEANG180 = 34
    swConstraintType_ELLIPSEANG270 = 35
    swConstraintType_ELLIPSEANGTOP = 36
    swConstraintType_ELLIPSEANGBOTTOM = 37
    swConstraintType_ELLIPSEANGLEFT = 38
    swConstraintType_ELLIPSEANGRIGHT = 39
    swConstraintType_ATPIERCE = 40
    swConstraintType_DOUBLEDISTANCE = 41
    swConstraintType_MERGEPOINTS = 42
    swConstraintType_ANGLE3P = 43
    swConstraintType_ARCLENGTH = 44
    swConstraintType_NORMAL = 45
    swConstraintType_NORMALPOINTS = 46
    swConstraintType_SKETCHOFFSET = 47
    swConstraintType_ALONGX = 48
    swConstraintType_ALONGY = 49
    swConstraintType_ALONGZ = 50
    swConstraintType_ALONGXPOINTS = 51
    swConstraintType_ALONGYPOINTS = 52
    swConstraintType_ALONGZPOINTS = 53
    swConstraintType_PARALLELYZ = 54
    swConstraintType_PARALLELZX = 55
    swConstraintType_INTERSECTION = 56
    swConstraintType_PATTERNED = 57
    swConstraintType_ISOBYPOINT = 58
    swConstraintType_SAMEISOPARAM = 59
    swConstraintType_FITSPLINE = 60
    swConstraintType_EQUALCURVATURE = 61
    swConstraintType_EQUALTANGENT = 62
    swConstraintType_TANGENTFACE = 63
    swConstraintType_ALONGX3D = 64
    swConstraintType_ALONGY3D = 65
    swConstraintType_ALONGXPOINTS3D = 66
    swConstraintType_ALONGYPOINTS3D = 67
    swConstraintType_TRACTION = 68
    swConstraintType_BELTTRACTION = 69
    swConstraintType_BLOCKFIXEDLOCK = 70
    swConstraintType_BLOCKNORMALLOCK = 71
    swConstraintType_BLOCKROTATELOCK = 72
    swConstraintType_FAKESLOTCONSTRAINT = 73
    swConstraintType_FIXEDSLOT = 74
    swConstraintType_SAMESLOTS = 75
    swConstraintType_LINEARPATTCNT = 76
    swConstraintType_CIRCULARPATTCNT = 77
    swConstraintType_RADIALOFFSET = 78
    swConstraintType_PLANAROFFSET = 79
    swConstraintType_EQUALCURV3DALIGN = 80
    swConstraintType_FLANGEFACEDIST = 81
    swConstraintType_CONICRHO = 82
    swConstraintType_C3TOUCH = 83
    swConstraintType_DOUBLEANGLE = 84
    swConstraintType_SAMECURVELENGTH = 85

class swContactType_e(IntEnum):
    """swContactType_e (3 constants, from SwConst)."""
    swContact = 0
    swTangent = 1
    swCurvature = 2

class swControlBitmapLabelType_e(IntEnum):
    """swControlBitmapLabelType_e (25 constants, from SwConst)."""
    swBitmapLabel_LinearDistance = 1
    swBitmapLabel_AngularDistance = 2
    swBitmapLabel_SelectEdgeFaceVertex = 3
    swBitmapLabel_SelectFaceSurface = 4
    swBitmapLabel_SelectVertex = 5
    swBitmapLabel_SelectFace = 6
    swBitmapLabel_SelectEdge = 7
    swBitmapLabel_SelectFaceEdge = 8
    swBitmapLabel_SelectComponent = 9
    swBitmapLabel_Diameter = 10
    swBitmapLabel_Radius = 11
    swBitmapLabel_LinearDistance1 = 12
    swBitmapLabel_LinearDistance2 = 13
    swBitmapLabel_Thickness1 = 14
    swBitmapLabel_Thickness2 = 15
    swBitmapLabel_LinearPattern = 16
    swBitmapLabel_CircularPattern = 17
    swBitmapLabel_Width = 18
    swBitmapLabel_Depth = 19
    swBitmapLabel_KFactor = 20
    swBitmapLabel_BendAllowance = 21
    swBitmapLabel_BendDeduction = 22
    swBitmapLabel_RipGap = 23
    swBitmapLabel_SelectProfile = 24
    swBitmapLabel_SelectBoundary = 25

class swCoordSysElementType_e(IntEnum):
    """swCoordSysElementType_e (7 constants, from SwConst)."""
    swCoordSysElement_XYPlane = 0
    swCoordSysElement_XZPlane = 1
    swCoordSysElement_YZPlane = 2
    swCoordSysElement_XAxis = 3
    swCoordSysElement_YAxis = 4
    swCoordSysElement_ZAxis = 5
    swCoordSysElement_Point = 6

class swCoreFeatureDirection_e(IntEnum):
    """swCoreFeatureDirection_e (2 constants, from SwConst)."""
    swCoreAlongExtractionDirection = 0
    swCoreAwayFromExtractionDirection = 1

class swCornerReliefBendType_e(IntEnum):
    """swCornerReliefBendType_e (2 constants, from SwConst)."""
    swCornerReliefBendType_TwoBend = 0
    swCornerReliefBendType_ThreeBend = 1

class swCornerReliefError_e(IntEnum):
    """swCornerReliefError_e (7 constants, from SwConst)."""
    swCornerReliefError_None = 0
    swCornerReliefError_InvalidFaces = 1
    swCornerReliefError_InvalidBody = 2
    swCornerReliefError_InvalidCornerType = 3
    swCornerReliefError_InvalidReliefType = 4
    swCornerReliefError_IndexNotAvailable = 5
    swCornerReliefError_GenericFailure = 6

class swCornerReliefSuitCaseType_e(IntEnum):
    """swCornerReliefSuitCaseType_e (3 constants, from SwConst)."""
    swCornerReliefSuitCase_Default = 0
    swCornerReliefSuitCase_ExtendGapInBendArea = 1
    swCornerReliefSuitCase_FillInSomeGap = 2

class swCornerReliefType_e(IntEnum):
    """swCornerReliefType_e (10 constants, from SwConst)."""
    swCornerCircularRelief = 0
    swCornerSquareRelief = 1
    swCornerBendWaistRelief = 2
    swCornerTearRelief = 3
    swCornerConstantWidthRelief = 4
    swCornerObroundRelief = 5
    swCornerMixed = 6
    swCornerFullRoundRelief = 7
    swCornerSuitCaseRelief = 8
    swCornerRectangularRelief = 9

class swCornerTreatmentPlanarTrimOptions_e(IntEnum):
    """swCornerTreatmentPlanarTrimOptions_e (2 constants, from SwConst)."""
    swCornerTreatmentPlanarTrim_FirstContact = 0
    swCornerTreatmentPlanarTrim_FullContact = 1

class swCornerTreatmentPlanarTrimToolType_e(IntEnum):
    """swCornerTreatmentPlanarTrimToolType_e (2 constants, from SwConst)."""
    swCornerTreatmentPlanarTrimTool_Automatic = 0
    swCornerTreatmentPlanarTrimTool_UserDefined = 1

class swCornerTreatmentTrimType_e(IntEnum):
    """swCornerTreatmentTrimType_e (3 constants, from SwConst)."""
    swCornerTreatmentTrim_PlanarTrim = 0
    swCornerTreatmentTrim_BodyTrim = 1
    swCornerTreatmentTrim_MiterTrim = 2

class swCornerType_e(IntEnum):
    """swCornerType_e (3 constants, from SwConst)."""
    swCorner_Simple = 0
    swCorner_TwoMember = 1
    swCorner_Complex = 2

class swCosmeticConfigOptions_e(IntEnum):
    """swCosmeticConfigOptions_e (3 constants, from SwConst)."""
    swConfigOptions_ThisConfiguration = 1
    swConfigOptions_AllConfiguration = 2
    swConfigOptions_SpecifyConfiguration = 3

class swCosmeticEndConditions_e(IntEnum):
    """swCosmeticEndConditions_e (4 constants, from SwConst)."""
    swEndConditionBlind = 0
    swEndConditionBlindUptoNext = 1
    swEndConditionThrough = 2
    swEndConditionBlind2Dia = 3

class swCosmeticStandardType_e(IntEnum):
    """swCosmeticStandardType_e (18 constants, from SwConst)."""
    swStandardType_StandardAnsiInch = 0
    swStandardType_StandardAnsiMetric = 1
    swStandardType_StandardBSI = 2
    swStandardType_StandardDME = 3
    swStandardType_StandardDIN = 4
    swStandardType_StandardHascoMetric = 5
    swStandardType_StandardHelicoilInch = 6
    swStandardType_StandardHelicoilMetric = 7
    swStandardType_StandardISO = 8
    swStandardType_StandardJIS = 9
    swStandardType_StandardPCS = 10
    swStandardType_StandardProgressive = 11
    swStandardType_StandardSuperior = 12
    swStandardType_StandardGB = 13
    swStandardType_StandardKS = 14
    swStandardType_StandardIS = 15
    swStandardType_StandardAS = 16
    swStandardType_StandardNone = -2

class swCosmeticThreadDiameterType_e(IntEnum):
    """swCosmeticThreadDiameterType_e (3 constants, from SwConst)."""
    swCosmeticThread_ConicalOffset = 1
    swCosmeticThread_MajorDiameter = 2
    swCosmeticThread_MinorDiameter = 3

class swCosmeticThreadType_e(IntEnum):
    """swCosmeticThreadType_e (3 constants, from SwConst)."""
    swApplyCosmeticThread_Blind = 0
    swApplyCosmeticThread_UpToNext = 1
    swApplyCosmeticThread_ThroughFeature = 2

class swCosmeticWeldBeadMode_e(IntEnum):
    """swCosmeticWeldBeadMode_e (2 constants, from SwConst)."""
    swCosmeticWeldBeadMode_WeldGeometry = 0
    swCosmeticWeldBeadMode_WeldPath = 1

class swCosmeticWeldBeadSide_e(IntEnum):
    """swCosmeticWeldBeadSide_e (3 constants, from SwConst)."""
    swCosmeticWeldBeadSide_selection = 1
    swCosmeticWeldBeadSide_bothSides = 2
    swCosmeticWeldBeadSide_allAround = 3

class swCosmosWorksMat(IntEnum):
    """swCosmosWorksMat (6 constants, from SwConst)."""
    swCosmosWorksMatNone = 0
    swCosmosWorksMatAcrylic = 1
    swCosmosWorksMatAluminum = 2
    swCosmosWorksMatNylon = 3
    swCosmosWorksMatRubber = 4
    swCosmosWorksMatSteel = 5

class swCreateAngRunDimError_e(IntEnum):
    """swCreateAngRunDimError_e (5 constants, from SwConst)."""
    swCreateAngRunDimError_Undefined = -1
    swCreateAngRunDimError_GenFailure = 0
    swCreateAngRunDimError_Success = 1
    swCreateAngRunDimError_IdenticalDimension = 2
    swCreateAngRunDimError_SelectAnotherEntity = 3

class swCreateCommandGroupErrors(IntEnum):
    """swCreateCommandGroupErrors (3 constants, from SwConst)."""
    swCreateCommandGroup_Failed = 0
    swCreateCommandGroup_Success = 1
    swCreateCommandGroup_Exceeds_ToolBarIDs = 2

class swCreateExplodeStepError_e(IntEnum):
    """swCreateExplodeStepError_e (7 constants, from SwConst)."""
    swCreateExplodeStepError_Successful = 0
    swCreateExplodeStepError_Generic = 1
    swCreateExplodeStepError_NoExplodeView = 2
    swCreateExplodeStepError_NoComponents = 3
    swCreateExplodeStepError_InvalidRadialAxis = 4
    swCreateExplodeStepError_OpenExplodePMP = 5
    swCreateExplodeStepError_EditingComponentInContext = 6

class swCreateFacesBodyAction_e(IntEnum):
    """swCreateFacesBodyAction_e (4 constants, from SwConst)."""
    swCreateFacesBodyActionCap = 1
    swCreateFacesBodyActionGrow = 2
    swCreateFacesBodyActionGrowFromParent = 3
    swCreateFacesBodyActionLeaveRubber = 4

class swCreateFeatureBodyOpts_e(IntEnum):
    """swCreateFeatureBodyOpts_e (2 constants, from SwConst)."""
    swCreateFeatureBodyCheck = 1
    swCreateFeatureBodySimplify = 2

class swCreateFeatureError_e(IntEnum):
    """swCreateFeatureError_e (9 constants, from SwConst)."""
    swCreateFeatureError_GenricError_GeometricError = 0
    swCreateFeatureError_GenricError_UnknownError = 1
    swCreateFeatureError_MateController_MateNotSet = 2
    swCreateFeatureError_MateController_MateTypeNotSupported = 3
    swCreateFeatureError_MateController_FailedToSolveMates = 4
    swCreateFeatureError_MateController_DimensionValueOutOfLimit = 5
    swCreateFeatureError_MateController_MateSelectionsPositionDataMismatch = 6
    swCreateFeatureError_SolidToSheetMetal_Success = 7
    swCreateFeatureError_SolidToSheetMetal_FixedFaceOrEdgeIsMissing = 8

class swCreateOrdDimError_e(IntEnum):
    """swCreateOrdDimError_e (11 constants, from SwConst)."""
    swCreateOrdDimErr_Undefined = -1
    swCreateOrdDimErr_Success = 0
    swCreateOrdDimErr_GenFailure = 1
    swCreateOrdDimErr_GenNoInternalDims = 2
    swCreateOrdDimErr_GenBadSel = 3
    swCreateOrdDimErr_GenNeedModelLoaded = 4
    swCreateOrdDimErr_GenSamePartOnly = 5
    swCreateOrdDimErr_GenExtraSelection = 6
    swCreateOrdDimErr_OrdFailure = 7
    swCreateOrdDimErr_OrdDupInGroup = 8
    swCreateOrdDimErr_OrdBadDir = 9

class swCreatePartExplodeStepError_e(IntEnum):
    """swCreatePartExplodeStepError_e (5 constants, from SwConst)."""
    swCreatePartExplodeStepError_Successful = 0
    swCreatePartExplodeStepError_Generic = 1
    swCreatePartExplodeStepError_NoBodies = 2
    swCreatePartExplodeStepError_OpenExplodePMP = 3
    swCreatePartExplodeStepError_InactiveConfiguration = 4

class swCreateSectionViewAtOptions_e(IntEnum):
    """swCreateSectionViewAtOptions_e (8 constants, from SwConst)."""
    swCreateSectionView_NotAligned = 1
    swCreateSectionView_OffsetSection = 2
    swCreateSectionView_ChangeDirection = 4
    swCreateSectionView_ScaleWithModel = 8
    swCreateSectionView_Partial = 16
    swCreateSectionView_DisplaySurfaceCut = 32
    swCreateSectionView_ExcludeFasteners = 64
    swCreateSectionView_CutSurfaceBodies = 128

class swCreateSeedCutType_e(IntEnum):
    """swCreateSeedCutType_e (5 constants, from SwConst)."""
    swCreateSeedCutNone = 0
    swCreateSeedCutCircle = 1
    swCreateSeedCutSquare = 2
    swCreateSeedCutDiamond = 3
    swCreateSeedCutPolygon = 4

class swCreateWireBodyOptions_e(IntEnum):
    """swCreateWireBodyOptions_e (2 constants, from SwConst)."""
    swCreateWireBodyByDefault = 0
    swCreateWireBodyMergeCurves = 1

class swCropViewErrors_e(IntEnum):
    """swCropViewErrors_e (5 constants, from SwConst)."""
    swCropViewErrors_Unknown = 0
    swCropViewErrors_NoError = 1
    swCropViewErrors_CannotCropDetailOrBrokenView = 2
    swCropViewErrors_CannotUnfoldView = 3
    swCropViewErrors_IncorrectProfile = 4

class swCrossHatchFilter_e(IntEnum):
    """swCrossHatchFilter_e (5 constants, from SwConst)."""
    swCrossHatchInclude = 0
    swCrossHatchExclude = 1
    swCrossHatchOnly = 2
    swCrossHatchAndExplodeOnly = 3
    swSolidHatchOnly = 4

class swCurveDrivenPatternAlignment_e(IntEnum):
    """swCurveDrivenPatternAlignment_e (2 constants, from SwConst)."""
    swCurvePatternTangentToCurve = 0
    swCurvePatternAlignToSeed = 1

class swCurveDrivenPatternCurveMethod_e(IntEnum):
    """swCurveDrivenPatternCurveMethod_e (2 constants, from SwConst)."""
    swCurvePatternTransformCurve = 0
    swCurvePatternOffsetCurve = 1

class swCurveTypes_e(IntEnum):
    """swCurveTypes_e (8 constants, from SwConst)."""
    LINE_TYPE = 3001
    CIRCLE_TYPE = 3002
    ELLIPSE_TYPE = 3003
    INTERSECTION_TYPE = 3004
    BCURVE_TYPE = 3005
    SPCURVE_TYPE = 3006
    CONSTPARAM_TYPE = 3008
    TRIMMED_TYPE = 3009

class swCustomInfoAddResult_e(IntEnum):
    """swCustomInfoAddResult_e (5 constants, from SwConst)."""
    swCustomInfoAddResult_AddedOrChanged = 0
    swCustomInfoAddResult_GenericFail = 1
    swCustomInfoAddResult_MismatchAgainstExistingType = 2
    swCustomInfoAddResult_MismatchAgainstSpecifiedType = 3
    swCustomInfoAddResult_MismatchAgainstLegacyTypes = 4

class swCustomInfoDeleteResult_e(IntEnum):
    """swCustomInfoDeleteResult_e (3 constants, from SwConst)."""
    swCustomInfoDeleteResult_OK = 0
    swCustomInfoDeleteResult_NotPresent = 1
    swCustomInfoDeleteResult_LinkedProp = 2

class swCustomInfoGetResult_e(IntEnum):
    """swCustomInfoGetResult_e (3 constants, from SwConst)."""
    swCustomInfoGetResult_CachedValue = 0
    swCustomInfoGetResult_ResolvedValue = 2
    swCustomInfoGetResult_NotPresent = 1

class swCustomInfoSetResult_e(IntEnum):
    """swCustomInfoSetResult_e (4 constants, from SwConst)."""
    swCustomInfoSetResult_OK = 0
    swCustomInfoSetResult_NotPresent = 1
    swCustomInfoSetResult_TypeMismatch = 2
    swCustomInfoSetResult_LinkedProp = 3

class swCustomInfoType_e(IntEnum):
    """swCustomInfoType_e (7 constants, from SwConst)."""
    swCustomInfoUnknown = 0
    swCustomInfoText = 30
    swCustomInfoDate = 64
    swCustomInfoNumber = 3
    swCustomInfoDouble = 5
    swCustomInfoYesOrNo = 11
    swCustomInfoEquation = 105

class swCustomLinkSetResult_e(IntEnum):
    """swCustomLinkSetResult_e (4 constants, from SwConst)."""
    swCustomLinkSetResult_OK = 0
    swCustomLinkSetResult_NotPresent = 1
    swCustomLinkSetResult_Legacy = 2
    swCustomLinkSetResult_UserProp = 3

class swCustomPropertyAddOption_e(IntEnum):
    """swCustomPropertyAddOption_e (3 constants, from SwConst)."""
    swCustomPropertyOnlyIfNew = 0
    swCustomPropertyDeleteAndAdd = 1
    swCustomPropertyReplaceValue = 2

class swCutListExclusionStatus_e(IntEnum):
    """swCutListExclusionStatus_e (2 constants, from SwConst)."""
    swCutListExclusionStatus_Success = 0
    swCutListExclusionStatus_InvalidEntities = 1

class swCutListTransferOptions_e(IntEnum):
    """swCutListTransferOptions_e (3 constants, from SwConst)."""
    swCutListTransferOptions_None = 0
    swCutListTransferOptions_FileProperties = 1
    swCutListTransferOptions_CutListProperties = 2

class swCutListType_e(IntEnum):
    """swCutListType_e (3 constants, from SwConst)."""
    swSolidBodyCutList = 1
    swSheetmetalCutlist = 2
    swWeldmentCutlist = 3

class swCutSweepOption_e(IntEnum):
    """swCutSweepOption_e (2 constants, from SwConst)."""
    swProfileSweep = 1
    swSolidSweep = 2

class swDatumDisplayType_e(IntEnum):
    """swDatumDisplayType_e (3 constants, from SwConst)."""
    swDatumDisplayType_Default = 0
    swDatumDisplayType_Square = 1
    swDatumDisplayType_Roundgb = 2

class swDatumGbLeaderStyle_e(IntEnum):
    """swDatumGbLeaderStyle_e (3 constants, from SwConst)."""
    swDatumLeaderStyle_Horizontal = 1
    swDatumLeaderStyle_Vertical = 2
    swDatumLeaderStyle_Perpendicular = 3

class swDatumTagTextParts_e(IntEnum):
    """swDatumTagTextParts_e (4 constants, from SwConst)."""
    swDatumTagTextPrefix = 1
    swDatumTagTextSuffix = 2
    swDatumTagTextCalloutAbove = 3
    swDatumTagTextCalloutBelow = 4

class swDatumTargetAreaShape_e(IntEnum):
    """swDatumTargetAreaShape_e (4 constants, from SwConst)."""
    swDatumTargetAreaNone = 0
    swDatumTargetAreaPoint = 1
    swDatumTargetAreaCircle = 2
    swDatumTargetAreaRectangle = 3

class swDefaultBOMPartNumberSource_e(IntEnum):
    """swDefaultBOMPartNumberSource_e (2 constants, from SwConst)."""
    swDefaultBOMPartNumberSource_DocumentName = 0
    swDefaultBOMPartNumberSource_ConfigurationName = 1

class swDeleteSelectionOptions_e(IntEnum):
    """swDeleteSelectionOptions_e (3 constants, from SwConst)."""
    swDelete_Children = 1
    swDelete_Absorbed = 2
    swDelete_Advanced = 4

class swDesignTableErrors_e(IntEnum):
    """swDesignTableErrors_e (35 constants, from SwConst)."""
    swDTblNoError = 0
    swDTblCfgInvalid = 1
    swDTblCorrupt = 2
    swDTblExiting = 3
    swDTblNoFileName = 4
    swDTblCurrentlyEditing = 5
    swDTblTooManyColumns = 6
    swDTblLinkChanged = 7
    swDTblFileNotFound = 8
    swDTblInvalidColumnValue = 9
    swDTblInvalidColCustomProp = 10
    swDTblInvalidColumnDimName = 11
    swDTblInvalidColumnFeatName = 12
    swDTblInvalidColumnKeyWord = 13
    swDTblInvalidConfigName = 14
    swDTblDataInvalidComponetState = 15
    swDTblDataInvalidFeatureState = 16
    swDTblInvalidYesNoData = 17
    swDTblDisplayStateError = 18
    swDTblModelFeatRequired = 19
    swDTblParentConfigInvalid = 20
    swDTblInvalidRowNameKeyword = 21
    swDTblTolTypeInvalid = 22
    swDTblNotSuppressible = 23
    swDTblTableIsEmpty = 24
    swDTblNegitiveDimension = 25
    swDTbUnUsedConfiguration = 26
    swDTbCannotOpen = 27
    swDTInvalidComponentName = 28
    swDTNeedsComponent = 29
    swDTDimValueRangeError = 30
    swDTDimAngleValueRangeError = 31
    swDTInvalidEquation = 32
    swDTConfigCircularDefinition = 33
    swDTInvalidUserSpecifiedConfigName = 34

class swDesignTableSourceTypes_e(IntEnum):
    """swDesignTableSourceTypes_e (3 constants, from SwConst)."""
    swDesignTableSourceNone = 1
    swDesignTableSourceFromFile = 2
    swDesignTableSourceLinked = 3

class swDesignTableUpdateOptions_e(IntEnum):
    """swDesignTableUpdateOptions_e (3 constants, from SwConst)."""
    swUpdateDesignTableSelected = 1
    swUpdateDesignTableAll = 2
    swUpdateDesignTableNone = 3

class swDestroyNotifyType_e(IntEnum):
    """swDestroyNotifyType_e (2 constants, from SwConst)."""
    swDestroyNotifyDestroy = 0
    swDestroyNotifyHidden = 1

class swDetCircleShowType_e(IntEnum):
    """swDetCircleShowType_e (3 constants, from SwConst)."""
    swDetCirclePROFILE = 0
    swDetCircleCIRCLE = 1
    swDetCircleDONTSHOW = 2

class swDetViewStyle_e(IntEnum):
    """swDetViewStyle_e (5 constants, from SwConst)."""
    swDetViewSTANDARD = 0
    swDetViewBROKEN = 1
    swDetViewLEADER = 2
    swDetViewNOLEADER = 3
    swDetViewCONNECTED = 4

class swDetailingBalloonAutoBalloons_e(IntEnum):
    """swDetailingBalloonAutoBalloons_e (2 constants, from SwConst)."""
    swStraightAutoBalloonLeader = 0
    swBentAutoBalloonLeader = 1

class swDetailingChamferDimLeaderStyle_e(IntEnum):
    """swDetailingChamferDimLeaderStyle_e (5 constants, from SwConst)."""
    swDetailChamferDimLeaderHorizBeside = 1
    swDetailChamferDimLeaderHorizAbove = 2
    swDetailChamferDimLeaderAngBeside = 3
    swDetailChamferDimLeaderAngAbove = 4
    swDetailChamferDimLeaderAlongEdge = 5

class swDetailingChamferDimLeaderTextStyle_e(IntEnum):
    """swDetailingChamferDimLeaderTextStyle_e (4 constants, from SwConst)."""
    swDetailChamferDimDistDist = 1
    swDetailChamferDimDistAng = 2
    swDetailChamferDimAngDist = 3
    swDetailChamferDimCDist = 4

class swDetailingChamferDimXStyle_e(IntEnum):
    """swDetailingChamferDimXStyle_e (2 constants, from SwConst)."""
    swDetailingChamferDimXStyleUpperCaseX = 1
    swDetailingChamferDimXStyleLowerCaseX = 2

class swDetailingDimFractionScaleIndex_e(IntEnum):
    """swDetailingDimFractionScaleIndex_e (10 constants, from SwConst)."""
    swDetailingDimFractionScale_100Percent = 0
    swDetailingDimFractionScale_90Percent = 1
    swDetailingDimFractionScale_80Percent = 2
    swDetailingDimFractionScale_70Percent = 3
    swDetailingDimFractionScale_60Percent = 4
    swDetailingDimFractionScale_50Percent = 5
    swDetailingDimFractionScale_40Percent = 6
    swDetailingDimFractionScale_30Percent = 7
    swDetailingDimFractionScale_20Percent = 8
    swDetailingDimFractionScale_10Percent = 9

class swDetailingDimFractionStyle_e(IntEnum):
    """swDetailingDimFractionStyle_e (4 constants, from SwConst)."""
    swDetailingDimFractionStyle_Slash = 0
    swDetailingDimFractionStyle_Stack = 1
    swDetailingDimFractionStyle_DiagonalStack = 2
    swDetailingDimFractionStyle_Dash = 3

class swDetailingDimTrailingZero_e(IntEnum):
    """swDetailingDimTrailingZero_e (9 constants, from SwConst)."""
    swDimSmartTrailingZeroes = 0
    swDimShowTrailingZeroes = 1
    swDimRemoveTrailingZeroes = 2
    swDimStandardTrailingZeroes = 3
    swDimRemoveOnlyOnZero = 4
    swDimSameAsSource = 5
    swDimSameAsDocumentDimension = 6
    swDimSameAsDocumentTolerance = 7
    swDimSameAsDimension = 8

class swDetailingDimXpertChamferInstanceStyle_e(IntEnum):
    """swDetailingDimXpertChamferInstanceStyle_e (3 constants, from SwConst)."""
    swDetailingDimXpertChamferNone = 1
    swDetailingDimXpertChamferTyp = 2
    swDetailingDimXpertChamferInstance = 3

class swDetailingDimXpertChamferStyle_e(IntEnum):
    """swDetailingDimXpertChamferStyle_e (2 constants, from SwConst)."""
    swDetailingDimXpertChamferDistDist = 1
    swDetailingDimXpertChamferDistAngle = 2

class swDetailingDimXpertFilletInstanceStyle_e(IntEnum):
    """swDetailingDimXpertFilletInstanceStyle_e (3 constants, from SwConst)."""
    swDetailingDimXpertFilletNone = 1
    swDetailingDimXpertFilletTyp = 2
    swDetailingDimXpertFilletInstance = 3

class swDetailingDimXpertSlotStyle_e(IntEnum):
    """swDetailingDimXpertSlotStyle_e (2 constants, from SwConst)."""
    swDetailingDimXpertSlotCenter = 1
    swDetailingDimXpertSlotOverall = 2

class swDetailingDualDimPosition_e(IntEnum):
    """swDetailingDualDimPosition_e (6 constants, from SwConst)."""
    swDualDimensionsSideBySide = 1
    swDualDimensionsAboveAndBelow = 2
    swDualDimensionsOnRight = 1
    swDualDimensionsOnTop = 2
    swDualDimensionsOnLeft = 3
    swDualDimensionsOnBottom = 4

class swDetailingForeshortenedDiameterStyle_e(IntEnum):
    """swDetailingForeshortenedDiameterStyle_e (2 constants, from SwConst)."""
    swForeshortenedStyleDoubleArrowhead = 1
    swForeshortenedStyleZigZagLeader = 2

class swDetailingGtolMaterialConditionSymbolPlacement_e(IntEnum):
    """swDetailingGtolMaterialConditionSymbolPlacement_e (2 constants, from SwConst)."""
    swDetailingGtolMaterialConditionSymbolPlacement_ASME = 0
    swDetailingGtolMaterialConditionSymbolPlacement_ISO = 1

class swDetailingHalfSectionArrow_e(IntEnum):
    """swDetailingHalfSectionArrow_e (2 constants, from SwConst)."""
    swDetailingHalfSectionArrow_AlternativeDisplay = 0
    swDetailingHalfSectionArrow_StandardDisplay = 1

class swDetailingLeadingZero_e(IntEnum):
    """swDetailingLeadingZero_e (3 constants, from SwConst)."""
    swLeadingZero_FollowStandard = 1
    swLeadingZero_Show = 2
    swLeadingZero_DoNotShow = 3

class swDetailingLinearForeshortened_e(IntEnum):
    """swDetailingLinearForeshortened_e (4 constants, from SwConst)."""
    swDetailingLinearForeshortened_DoubleArrow = 0
    swDetailingLinearForeshortened_Zigzag = 1
    swDetailingLinearForeshortened_Line = 2
    swDetailingLinearForeshortened_SingleArrow = 3

class swDetailingNoteTextContent_e(IntEnum):
    """swDetailingNoteTextContent_e (4 constants, from SwConst)."""
    swDetailingNoteTextCustom = 1
    swDetailingNoteTextItemNumber = 2
    swDetailingNoteTextQuantity = 3
    swDetailingNoteTextCustomProperty = 4

class swDetailingSFSymbolStandard_e(IntEnum):
    """swDetailingSFSymbolStandard_e (3 constants, from SwConst)."""
    swDetailingSFSymbolStandard_1302_1992 = 0
    swDetailingSFSymbolStandard_1302_2002 = 1
    swDetailingSFSymbolStandard_21920_1 = 2

class swDetailingSectionViewLineStyle_e(IntEnum):
    """swDetailingSectionViewLineStyle_e (3 constants, from SwConst)."""
    swDetailingSectionViewLineStyleDisplay_StandardWithConnector = 0
    swDetailingSectionViewLineStyleDisplay_AlternateWithoutConnector = 1
    swDetailingSectionViewLineStyleDisplay_StandardWithoutConnector = 2

class swDetailingStandard_e(IntEnum):
    """swDetailingStandard_e (8 constants, from SwConst)."""
    swDetailingStandardANSI = 1
    swDetailingStandardISO = 2
    swDetailingStandardDIN = 3
    swDetailingStandardJIS = 4
    swDetailingStandardBS = 5
    swDetailingStandardGOST = 6
    swDetailingStandardGB = 7
    swDetailingStandardUserDefined = 8

class swDetailingToleranceTextSizing_e(IntEnum):
    """swDetailingToleranceTextSizing_e (2 constants, from SwConst)."""
    swToleranceTextSizeUsingScaleValue = 1
    swToleranceTextSizeUsingHeightValue = 2

class swDetailingViewLabelsDelimiter_e(IntEnum):
    """swDetailingViewLabelsDelimiter_e (6 constants, from SwConst)."""
    swDetailingViewLabelsDelimiter_none = 0
    swDetailingViewLabelsDelimiter_XcolonX = 1
    swDetailingViewLabelsDelimiter_XslashX = 2
    swDetailingViewLabelsDelimiter_XcolonXparen = 3
    swDetailingViewLabelsDelimiter_XslashXparen = 4
    swDetailingViewLabelsDelimiter_numberX = 5

class swDetailingViewLabelsLabel_e(IntEnum):
    """swDetailingViewLabelsLabel_e (4 constants, from SwConst)."""
    swDetailingViewLabelsLabel_none = 0
    swDetailingViewLabelsLabel_X = 1
    swDetailingViewLabelsLabel_XdashX = 2
    swDetailingViewLabelsLabel_XspaceX = 3

class swDetailingViewLabelsName_e(IntEnum):
    """swDetailingViewLabelsName_e (5 constants, from SwConst)."""
    swDetailingViewLabelsName_none = 0
    swDetailingViewLabelsName_VIEW = 1
    swDetailingViewLabelsName_viewtype = 2
    swDetailingViewLabelsName_custom = 3
    swDetailingViewLabelsName_DrawingTree = 4

class swDetailingViewLabelsScale_e(IntEnum):
    """swDetailingViewLabelsScale_e (4 constants, from SwConst)."""
    swDetailingViewLabelsScale_none = 0
    swDetailingViewLabelsScale_SCALE = 1
    swDetailingViewLabelsScale_SCALEcolon = 2
    swDetailingViewLabelsScale_SCALEcustom = 3

class swDetailingViewRotation_e(IntEnum):
    """swDetailingViewRotation_e (5 constants, from SwConst)."""
    swDetailingViewRotation_None = 0
    swDetailingViewRotation_DisplaySymbolAngle = 1
    swDetailingViewRotation_DisplaySymbol = 2
    swDetailingViewRotation_DisplayROTATEDAngleCWCCW = 3
    swDetailingViewRotation_DisplayAngle = 4

class swDetailingVirtualSharp_e(IntEnum):
    """swDetailingVirtualSharp_e (5 constants, from SwConst)."""
    swDetailingVirtualSharpNone = 0
    swDetailingVirtualSharpPlus = 1
    swDetailingVirtualSharpStar = 2
    swDetailingVirtualSharpWitness = 3
    swDetailingVirtualSharpDot = 4

class swDimXpertAnnotationType_e(IntEnum):
    """swDimXpertAnnotationType_e (36 constants, from SwDimXpert)."""
    swDimXpertAnnotationType_unknown = 0
    swDimXpertDimTol_DistanceBetween = 101
    swDimXpertDimTol_CounterBore = 102
    swDimXpertDimTol_Depth = 103
    swDimXpertDimTol_CounterSinkDiameter = 104
    swDimXpertDimTol_ChamferDimension = 105
    swDimXpertDimTol_AngleBetween = 106
    swDimXpertDimTol_CounterSinkAngle = 107
    swDimXpertDimTol_ConeAngle = 108
    swDimXpertDimTol_Diameter = 109
    swDimXpertDimTol_Length = 110
    swDimXpertDimTol_Radius = 111
    swDimXpertDimTol_Width = 112
    swDimXpertDimTol_CompositeDistanceBetween = 113
    swDimXpertDimTol_PatternAngleBetween = 114
    swDimXpertDatum = 150
    swDimXpertGeoTol_Position = 201
    swDimXpertGeoTol_CompositePosition = 202
    swDimXpertGeoTol_Symmetry = 203
    swDimXpertGeoTol_Concentricity = 204
    swDimXpertGeoTol_LineProfile = 205
    swDimXpertGeoTol_CompositeLineProfile = 206
    swDimXpertGeoTol_SurfaceProfile = 207
    swDimXpertGeoTol_CompositeSurfaceProfile = 208
    swDimXpertGeoTol_Angularity = 210
    swDimXpertGeoTol_Parallelism = 211
    swDimXpertGeoTol_Perpendicularity = 212
    swDimXpertGeoTol_TotalRunout = 213
    swDimXpertGeoTol_CircularRunout = 214
    swDimXpertGeoTol_Flatness = 215
    swDimXpertGeoTol_Circularity = 216
    swDimXpertGeoTol_Cylindricity = 217
    swDimXpertGeoTol_Straightness = 218
    swDimXpertGeoTol_Tangency = 219
    swDimXpertDimTol_AngleSize = 220
    swDimXpertDimTol_AngleBetweenCircular = 221

class swDimXpertAutoDimSchemePartType_e(IntEnum):
    """swDimXpertAutoDimSchemePartType_e (2 constants, from SwDimXpert)."""
    swDimXpertAutoDimSchemePartType_Prismatic = 0
    swDimXpertAutoDimSchemePartType_Turned = 1

class swDimXpertAutoDimSchemePatternType_e(IntEnum):
    """swDimXpertAutoDimSchemePatternType_e (2 constants, from SwDimXpert)."""
    swDimXpertAutoDimSchemePatternType_Linear = 0
    swDimXpertAutoDimSchemePatternType_Polar = 1

class swDimXpertAutoDimSchemeToleranceType_e(IntEnum):
    """swDimXpertAutoDimSchemeToleranceType_e (2 constants, from SwDimXpert)."""
    swDimXpertAutoDimSchemeToleranceType_PlusMinus = 0
    swDimXpertAutoDimSchemeToleranceType_Geometric = 1

class swDimXpertBlockPrecision_e(IntEnum):
    """swDimXpertBlockPrecision_e (3 constants, from SwConst)."""
    swDimXpertBlockPrecsionTwoDecimals = 0
    swDimXpertBlockPrecisionThreeDecimals = 1
    swDimXpertBlockPrecisionFourDecimals = 2

class swDimXpertBlockToleranceType_e(IntEnum):
    """swDimXpertBlockToleranceType_e (3 constants, from SwDimXpert)."""
    swDimXpertBlockToleranceType_unknown = 0
    swDimXpertBlockToleranceType_ASMEInch = 1
    swDimXpertBlockToleranceType_ISO2768 = 2

class swDimXpertChamferAngleType_e(IntEnum):
    """swDimXpertChamferAngleType_e (3 constants, from SwDimXpert)."""
    swDimXpertChamferAngleType_unknown = 0
    swDimXpertChamferAngleType_Concave = 1
    swDimXpertChamferAngleType_Convex = 2

class swDimXpertChamferDimensionType_e(IntEnum):
    """swDimXpertChamferDimensionType_e (4 constants, from SwDimXpert)."""
    swDimXpertChamferDimensionType_unknown = 0
    swDimXpertChamferDimensionType_Angle = 1
    swDimXpertChamferDimensionType_LinearDistance1 = 2
    swDimXpertChamferDimensionType_LinearDistance2 = 3

class swDimXpertChamferType_e(IntEnum):
    """swDimXpertChamferType_e (4 constants, from SwDimXpert)."""
    swDimXpertChamferType_unknown = 0
    swDimXpertChamferType_DistanceAngle = 1
    swDimXpertChamferType_DistanceDistance = 2
    swDimXpertChamferType_Vertex = 3

class swDimXpertCombineAnnotation_e(IntEnum):
    """swDimXpertCombineAnnotation_e (4 constants, from SwDimXpert)."""
    swDimXpertCombineAnnotation_swDimXpertCombineFailed = 0
    swDimXpertCombineAnnotation_swDimXpertCombineSucceeded = 1
    swDimXpertCombineAnnotation_swDimXpertBreakFailed = 2
    swDimXpertCombineAnnotation_swDimXpertBreakSucceeded = 3

class swDimXpertCompoundHoleType_e(IntEnum):
    """swDimXpertCompoundHoleType_e (5 constants, from SwDimXpert)."""
    swDimXpertCompoundHoleType_unknown = 0
    swDimXpertCompoundHoleType_Compound = 1
    swDimXpertCompoundHoleType_Counterbore = 2
    swDimXpertCompoundHoleType_Countersink = 3
    swDimXpertCompoundHoleType_Simple = 4

class swDimXpertDimensionPositionOption_e(IntEnum):
    """swDimXpertDimensionPositionOption_e (4 constants, from SwDimXpert)."""
    swDimXpertDimensionPositionOption_N = 0
    swDimXpertDimensionPositionOption_X = 1
    swDimXpertDimensionPositionOption_Y = 2
    swDimXpertDimensionPositionOption_Z = 3

class swDimXpertDimensionToleranceType_e(IntEnum):
    """swDimXpertDimensionToleranceType_e (11 constants, from SwDimXpert)."""
    swDimXpertDimensionToleranceType_unknown = 0
    swDimXpertDimTolType_BlockTolerance = 1
    swDimXpertDimTolType_BlockToleranceNoNominal = 2
    swDimXpertDimTolType_ISOLimitsAndFits = 3
    swDimXpertDimTolType_ISOLimitsAndFitsNoNominal = 4
    swDimXpertDimTolType_LimitDimension = 5
    swDimXpertDimTolType_MAXTolerance = 6
    swDimXpertDimTolType_MINTolerance = 7
    swDimXpertDimTolType_NoTolerance = 8
    swDimXpertDimTolType_PlusMinusDimension = 9
    swDimXpertDimTolType_PlusMinusNoNominal = 10

class swDimXpertDisplayDatumGtolLinearDimAttachmentType_e(IntEnum):
    """swDimXpertDisplayDatumGtolLinearDimAttachmentType_e (2 constants, from SwConst)."""
    swDimXpertDisplayDatumGtolLinearDimAttachmentType_ValueSide = 0
    swDimXpertDisplayDatumGtolLinearDimAttachmentType_ValueTop = 1

class swDimXpertDisplayDatumGtolSurfaceAttachmentType_e(IntEnum):
    """swDimXpertDisplayDatumGtolSurfaceAttachmentType_e (2 constants, from SwConst)."""
    swDimXpertDisplayDatumGtolSurfaceAttachmentType_ValueSide = 0
    swDimXpertDisplayDatumGtolSurfaceAttachmentType_ValueTop = 1

class swDimXpertDisplayGtolLinearDimAttachmentType_e(IntEnum):
    """swDimXpertDisplayGtolLinearDimAttachmentType_e (2 constants, from SwConst)."""
    swDimXpertDisplayGtolLinearDimAttachmentType_ValueSide = 0
    swDimXpertDisplayGtolLinearDimAttachmentType_ValueTop = 1

class swDimXpertDisplayHoleDimensionType_e(IntEnum):
    """swDimXpertDisplayHoleDimensionType_e (2 constants, from SwConst)."""
    swDimXpertDisplayHoleDimensionType_Diameters = 0
    swDimXpertDisplayHoleDimensionType_DiameterDepth = 1

class swDimXpertDisplaySlotDimensionType_e(IntEnum):
    """swDimXpertDisplaySlotDimensionType_e (2 constants, from SwConst)."""
    swDimXpertDisplaySlotDimensionType_LengthRadius = 0
    swDimXpertDisplaySlotDimensionType_LengthWidth = 1

class swDimXpertDistanceFosUsage_e(IntEnum):
    """swDimXpertDistanceFosUsage_e (4 constants, from SwDimXpert)."""
    swDimXpertDistanceFosUsage_unknown = 0
    swDimXpertDistanceFosUsage_Center = 1
    swDimXpertDistanceFosUsage_MaximumSide = 2
    swDimXpertDistanceFosUsage_MinimumSide = 3

class swDimXpertFeatureFilters_e(IntEnum):
    """swDimXpertFeatureFilters_e (16 constants, from SwDimXpert)."""
    swDimXpertFeatureFilters_Plane = 1
    swDimXpertFeatureFilters_Surface = 2
    swDimXpertFeatureFilters_Cone = 4
    swDimXpertFeatureFilters_Cylinder = 8
    swDimXpertFeatureFilters_Boss = 16
    swDimXpertFeatureFilters_Fillet = 32
    swDimXpertFeatureFilters_Chamfer = 64
    swDimXpertFeatureFilters_SimpleHole = 128
    swDimXpertFeatureFilters_Counterbore = 256
    swDimXpertFeatureFilters_Countersink = 512
    swDimXpertFeatureFilters_Slot = 1024
    swDimXpertFeatureFilters_Notch = 2048
    swDimXpertFeatureFilters_Pocket = 4096
    swDimXpertFeatureFilters_SurfOfRev = 8192
    swDimXpertFeatureFilters_Torus = 16384
    swDimXpertFeatureFilters_CompoundHole = 32768

class swDimXpertFeatureSelectorOption_e(IntEnum):
    """swDimXpertFeatureSelectorOption_e (25 constants, from SwDimXpert)."""
    swDimXpertFeatureSelectorOption_Default = -1
    swDimXpertFeatureSelectorOption_Plane = 0
    swDimXpertFeatureSelectorOption_Cylinder = 1
    swDimXpertFeatureSelectorOption_Sphere = 2
    swDimXpertFeatureSelectorOption_Freeform = 3
    swDimXpertFeatureSelectorOption_Cone = 4
    swDimXpertFeatureSelectorOption_SimpleHole = 5
    swDimXpertFeatureSelectorOption_Slot = 6
    swDimXpertFeatureSelectorOption_Width = 7
    swDimXpertFeatureSelectorOption_Boss = 8
    swDimXpertFeatureSelectorOption_Tab = 9
    swDimXpertFeatureSelectorOption_Fillet = 10
    swDimXpertFeatureSelectorOption_Chamfer = 11
    swDimXpertFeatureSelectorOption_ConicalHole = 12
    swDimXpertFeatureSelectorOption_Pocket = 13
    swDimXpertFeatureSelectorOption_Notch = 14
    swDimXpertFeatureSelectorOption_Extrude = 15
    swDimXpertFeatureSelectorOption_SplitPlane = 16
    swDimXpertFeatureSelectorOption_SplitCylinder = 17
    swDimXpertFeatureSelectorOption_CntrBore = 18
    swDimXpertFeatureSelectorOption_CntrSink = 19
    swDimXpertFeatureSelectorOption_CompoundHole = 20
    swDimXpertFeatureSelectorOption_HolePattern = 21
    swDimXpertFeatureSelectorOption_Pattern = 22
    swDimXpertFeatureSelectorOption_MixedPattern = 23

class swDimXpertFeatureType_e(IntEnum):
    """swDimXpertFeatureType_e (20 constants, from SwDimXpert)."""
    swDimXpertFeatureType_unknown = 0
    swDimXpertFeature_Plane = 1
    swDimXpertFeature_Cylinder = 2
    swDimXpertFeature_Cone = 3
    swDimXpertFeature_Extrude = 4
    swDimXpertFeature_Fillet = 5
    swDimXpertFeature_Chamfer = 6
    swDimXpertFeature_CompoundHole = 7
    swDimXpertFeature_CompoundWidth = 8
    swDimXpertFeature_CompoundNotch = 9
    swDimXpertFeature_CompoundClosedSlot3D = 10
    swDimXpertFeature_IntersectPoint = 11
    swDimXpertFeature_IntersectLine = 12
    swDimXpertFeature_IntersectCircle = 13
    swDimXpertFeature_IntersectPlane = 14
    swDimXpertFeature_Pattern = 15
    swDimXpertFeature_Sphere = 16
    swDimXpertFeature_BestfitPlane = 17
    swDimXpertFeature_Surface = 18
    swDimXpertFeature_RefPlane = 19

class swDimXpertGeneralTolClass_e(IntEnum):
    """swDimXpertGeneralTolClass_e (6 constants, from SwConst)."""
    swDimXpertGeneralTolClass_Fine = 0
    swDimXpertGeneralTolClass_Medium = 1
    swDimXpertGeneralTolClass_Coarse = 2
    swDimXpertGeneralTolClass_VeryCoarse = 3
    swDimXpertGeneralTolClass_Custom1 = 4
    swDimXpertGeneralTolClass_Custom2 = 5

class swDimXpertGtolType_e(IntEnum):
    """swDimXpertGtolType_e (14 constants, from SwDimXpert)."""
    swDimXpertGtolType_Straightness = 0
    swDimXpertGtolType_Flatness = 1
    swDimXpertGtolType_Circularity = 2
    swDimXpertGtolType_Cylindricity = 3
    swDimXpertGtolType_SurfaceProfile = 4
    swDimXpertGtolType_LineProfile = 5
    swDimXpertGtolType_Angularity = 6
    swDimXpertGtolType_Perpendicularity = 7
    swDimXpertGtolType_Parallelism = 8
    swDimXpertGtolType_Position = 9
    swDimXpertGtolType_Symmetry = 10
    swDimXpertGtolType_Concentricity = 11
    swDimXpertGtolType_CircularRunout = 12
    swDimXpertGtolType_TotalRunout = 13

class swDimXpertISO2768PartType_e(IntEnum):
    """swDimXpertISO2768PartType_e (5 constants, from SwDimXpert)."""
    swDimXpertISO2768PartType_unknown = 0
    swDimXpertISO2768PartType_Fine = 1
    swDimXpertISO2768PartType_Medium = 2
    swDimXpertISO2768PartType_Coarse = 3
    swDimXpertISO2768PartType_VeryCoarse = 4

class swDimXpertMaterialConditionModifier_e(IntEnum):
    """swDimXpertMaterialConditionModifier_e (5 constants, from SwDimXpert)."""
    swDimXpertMaterialConditionModifier_unknown = 0
    swDimXpertMCM_LMC = 1
    swDimXpertMCM_MMC = 2
    swDimXpertMCM_NoMCM = 3
    swDimXpertMCM_RFS = 4

class swDimXpertOrientationZoneType_e(IntEnum):
    """swDimXpertOrientationZoneType_e (3 constants, from SwDimXpert)."""
    swDimXpertOrientationZoneType_unknown = 0
    swDimXpertOrientationZoneType_Cylindrical = 1
    swDimXpertOrientationZoneType_Planar = 2

class swDimXpertPatternTreatmentType_e(IntEnum):
    """swDimXpertPatternTreatmentType_e (3 constants, from SwDimXpert)."""
    swDimXpertPatternTreatmentType_unknown = 0
    swDimXpertPatternTreatmentType_CircularPattern = 1
    swDimXpertPatternTreatmentType_IndividualFeatures = 2

class swDimXpertPositionZoneType_e(IntEnum):
    """swDimXpertPositionZoneType_e (7 constants, from SwDimXpert)."""
    swDimXpertPositionZoneType_unknown = 0
    swDimXpertPositionZoneType_Boundary = 1
    swDimXpertPositionZoneType_CylindricalPosition = 2
    swDimXpertPositionZoneType_PlanarPosition = 3
    swDimXpertPositionZoneType_RadialPositionArc = 4
    swDimXpertPositionZoneType_RadialPositionPlanar = 5
    swDimXpertPositionZoneType_SphericalPosition = 6

class swDimXpertStraightnessZoneType_e(IntEnum):
    """swDimXpertStraightnessZoneType_e (4 constants, from SwDimXpert)."""
    swDimXpertStraightnessZoneType_unknown = 0
    swDimXpertStraightnessZoneType_Cylindrical = 1
    swDimXpertStraightnessZoneType_PlanarMedian = 2
    swDimXpertStraightnessZoneType_Surface = 3

class swDimXpertTolType_e(IntEnum):
    """swDimXpertTolType_e (3 constants, from SwConst)."""
    swDimXpertTolType_Bilateral = 0
    swDimXpertTolType_Symmetric = 1
    swDimXpertTolType_GeneralOrBlock = 2

class swDimXpertTreeDisplay_e(IntEnum):
    """swDimXpertTreeDisplay_e (3 constants, from SwConst)."""
    swDimXpertTreeDisplay_Flat = 1
    swDimXpertTreeDisplay_Annotation = 2
    swDimXpertTreeDisplay_Feature = 3

class swDimensionArrowsSide_e(IntEnum):
    """swDimensionArrowsSide_e (4 constants, from SwConst)."""
    swDimArrowsInside = 0
    swDimArrowsOutside = 1
    swDimArrowsSmart = 2
    swDimArrowsFollowDoc = 3

class swDimensionDrivenState_e(IntEnum):
    """swDimensionDrivenState_e (3 constants, from SwConst)."""
    swDimensionDrivenUnknown = 0
    swDimensionDriven = 1
    swDimensionDriving = 2

class swDimensionParamType_e(IntEnum):
    """swDimensionParamType_e (4 constants, from SwConst)."""
    swDimensionParamTypeUnknown = -1
    swDimensionParamTypeDoubleLinear = 0
    swDimensionParamTypeDoubleAngular = 1
    swDimensionParamTypeInteger = 2

class swDimensionPrecisionSettings_e(IntEnum):
    """swDimensionPrecisionSettings_e (3 constants, from SwConst)."""
    swDoNotChangePrecisionSetting = -1
    swPrecisionFollowsDocumentSetting = -2
    swTolerancePrecisionFollowsNominal = -3

class swDimensionPrefix_e(IntEnum):
    """swDimensionPrefix_e (7 constants, from SwConst)."""
    swDimensionPrefix_None = 0
    swDimensionPrefix_2X = 1
    swDimensionPrefix_3X = 2
    swDimensionPrefix_4X = 3
    swDimensionPrefix_5X = 4
    swDimensionPrefix_6X = 5
    swDimensionPrefix_Unknown = 6

class swDimensionSymbol_e(IntEnum):
    """swDimensionSymbol_e (41 constants, from SwConst)."""
    swDimensionSymbol_None = 0
    swDimensionSymbol_Unknown = 1
    swDimensionSymbol_Diameter = 2
    swDimensionSymbol_Depth = 3
    swDimensionSymbol_Degree = 4
    swDimensionSymbol_Centerline = 5
    swDimensionSymbol_CenterOfMass = 6
    swDimensionSymbol_Counterbore = 7
    swDimensionSymbol_Countersink = 8
    swDimensionSymbol_ConicalTaper = 9
    swDimensionSymbol_Continuous = 10
    swDimensionSymbol_ControlledRadius = 11
    swDimensionSymbol_Delta = 12
    swDimensionSymbol_Encompassing = 13
    swDimensionSymbol_FlattenedLength = 14
    swDimensionSymbol_FreeState = 15
    swDimensionSymbol_Independency = 16
    swDimensionSymbol_LeastMaterialCondition = 17
    swDimensionSymbol_MaximumMaterialCondition = 18
    swDimensionSymbol_PartingLine = 19
    swDimensionSymbol_PlusMinus = 20
    swDimensionSymbol_ProjectedToleranceZone = 21
    swDimensionSymbol_RegardlessOfFeatureSize = 22
    swDimensionSymbol_Rho = 23
    swDimensionSymbol_SlopeUp = 24
    swDimensionSymbol_SlopeDown = 25
    swDimensionSymbol_SlopeInvertedUp = 26
    swDimensionSymbol_SlopeInvertedDown = 27
    swDimensionSymbol_SphericalRadius = 28
    swDimensionSymbol_SphericalDiameter = 29
    swDimensionSymbol_Square = 30
    swDimensionSymbol_SquareBS = 31
    swDimensionSymbol_Statistical = 32
    swDimensionSymbol_TangentPlane = 33
    swDimensionSymbol_Translation = 34
    swDimensionSymbol_UnequallyDisposedProfile = 35
    swDimensionSymbol_Radius = 36
    swDimensionSymbol_Angle = 37
    swDimensionSymbol_SlotLength = 38
    swDimensionSymbol_SlotWidth = 39
    swDimensionSymbol_CalloutText = 40

class swDimensionTextParts_e(IntEnum):
    """swDimensionTextParts_e (9 constants, from SwConst)."""
    swDimensionTextAll = 0
    swDimensionTextPrefix = 1
    swDimensionTextSuffix = 2
    swDimensionTextCalloutAbove = 3
    swDimensionTextCalloutBelow = 4
    swDimensionTextPrefixDefinition = 5
    swDimensionTextSuffixDefinition = 6
    swDimensionTextCalloutAboveDefinition = 7
    swDimensionTextCalloutBelowDefinition = 8

class swDimensionToleranceWarning_e(IntEnum):
    """swDimensionToleranceWarning_e (2 constants, from SwConst)."""
    swDimensionTolerance_ValidForType = 0
    swDimensionTolerance_NotValidForType = 1

class swDimensionType_e(IntEnum):
    """swDimensionType_e (17 constants, from SwConst)."""
    swDimensionTypeUnknown = 0
    swOrdinateDimension = 1
    swLinearDimension = 2
    swAngularDimension = 3
    swArcLengthDimension = 4
    swRadialDimension = 5
    swDiameterDimension = 6
    swHorOrdinateDimension = 7
    swVertOrdinateDimension = 8
    swZAxisDimension = 9
    swChamferDimension = 10
    swHorLinearDimension = 11
    swVertLinearDimension = 12
    swScalarDimension = 13
    swRadialLinearDimension = 14
    swDiametricLinearDimension = 15
    swAngularOrdinateDimension = 16

class swDisplayCircularReferencesInEquations_e(IntEnum):
    """swDisplayCircularReferencesInEquations_e (3 constants, from SwConst)."""
    swDisplayCircularReferencesInEquationsEverywhere = 0
    swDisplayCircularReferencesInEquationsInEquationDialogOnly = 1
    swDisplayCircularReferencesInEquationsNever = 2

class swDisplayDimensionLeaderText_e(IntEnum):
    """swDisplayDimensionLeaderText_e (4 constants, from SwConst)."""
    swSolidLeaderAlignedText = 1
    swBrokenLeaderHorizontalText = 2
    swBrokenLeaderAlignedText = 3
    swSolidLeaderHorizontalText = 4

class swDisplayMode_e(IntEnum):
    """swDisplayMode_e (10 constants, from SwConst)."""
    swDisplayModeUNKNOWN = -1
    swWIREFRAME = 0
    swHIDDEN_GREYED = 1
    swHIDDEN = 2
    swSHADED = 3
    swFACETED_WIREFRAME = 4
    swFACETED_HIDDEN_GREYED = 5
    swFACETED_HIDDEN = 6
    swSHADED_EDGES = 7
    swDisplayModeDEFAULT = 8

class swDisplayPaneIndex_e(IntEnum):
    """swDisplayPaneIndex_e (4 constants, from SwConst)."""
    swDisplayPaneNone = 0
    swDisplayPaneLifeCycleTab = 1
    swDisplayPaneTab = 2
    swDisplayPaneAIContentTab = 3

class swDisplayPotentialCircularReferencesInEquations_e(IntEnum):
    """swDisplayPotentialCircularReferencesInEquations_e (3 constants, from SwConst)."""
    swDisplayPotentialCircularReferencesInEquationsEverywhere = 0
    swDisplayPotentialCircularReferencesInEquationsInEquationDialogOnly = 1
    swDisplayPotentialCircularReferencesInEquationsNever = 2

class swDisplayStateCreationChoices_e(IntEnum):
    """swDisplayStateCreationChoices_e (4 constants, from SwConst)."""
    swDisplayStateCreation_AskUser = -1
    swDisplayStateCreation_PW = 1
    swDisplayStateCreation_SW = 2
    swDisplayStateCreation_BothPWSW = 3

class swDisplayStateOpts_e(IntEnum):
    """swDisplayStateOpts_e (3 constants, from SwConst)."""
    swThisDisplayState = 1
    swAllDisplayState = 2
    swSpecifyDisplayState = 3

class swDisplayTangentEdges_e(IntEnum):
    """swDisplayTangentEdges_e (3 constants, from SwConst)."""
    swTangentEdgesHidden = 0
    swTangentEdgesVisibleAndFonted = 1
    swTangentEdgesVisible = 2

class swDistanceMateArcConditions_e(IntEnum):
    """swDistanceMateArcConditions_e (4 constants, from SwConst)."""
    swArcCondition_NotSet = 0
    swArcCondition_Center = 1
    swArcCondition_Minimum = 2
    swArcCondition_Maximum = 3

class swDocTemplateTypes_e(IntEnum):
    """swDocTemplateTypes_e (5 constants, from SwConst)."""
    swDocTemplateTypeNONE = 1
    swDocTemplateTypePART = 2
    swDocTemplateTypeASSEMBLY = 4
    swDocTemplateTypeDRAWING = 8
    swDocTemplateTypeInContext = 16

class swDocumentTypes_e(IntEnum):
    """swDocumentTypes_e (8 constants, from SwConst)."""
    swDocNONE = 0
    swDocPART = 1
    swDocASSEMBLY = 2
    swDocDRAWING = 3
    swDocSDM = 4
    swDocLAYOUT = 5
    swDocIMPORTED_PART = 6
    swDocIMPORTED_ASSEMBLY = 7

class swDofStatus_e(IntEnum):
    """swDofStatus_e (7 constants, from SwConst)."""
    swDofStatus_Unused = 0
    swDofStatus_Static = 1
    swDofStatus_StaticNormal = 2
    swDofStatus_Free = 3
    swDofStatus_FreeNormal = 4
    swDofStatus_Instantaneous = 5
    swDofStatus_InstantaneousNormal = 6

class swDraftAnalysisFaceType_e(IntEnum):
    """swDraftAnalysisFaceType_e (4 constants, from SwConst)."""
    swDraftAnalysisFaceTypePositive = 0
    swDraftAnalysisFaceTypeNegative = 1
    swDraftAnalysisFaceTypeNoDraft = 2
    swDraftAnalysisFaceTypeStraddle = 3

class swDraftAnalysisOptions_e(IntEnum):
    """swDraftAnalysisOptions_e (2 constants, from SwConst)."""
    swDraftAnalysisFlipDir = 1
    swDraftAnalysisFindSteep = 2

class swDraftAnalysisShow_e(IntEnum):
    """swDraftAnalysisShow_e (7 constants, from SwConst)."""
    swDraftAnalysisShowPositive = 1
    swDraftAnalysisShowNegative = 2
    swDraftAnalysisShowDraftRequired = 4
    swDraftAnalysisShowStraddle = 8
    swDraftAnalysisShowPositiveSteep = 16
    swDraftAnalysisShowNegativeSteep = 32
    swDraftAnalysisShowSurface = 64

class swDraftFacePropagationType_e(IntEnum):
    """swDraftFacePropagationType_e (5 constants, from SwConst)."""
    swFacePropNone = 0
    swFacePropTangent = 1
    swFacePropAllLoops = 2
    swFacePropInnerLoops = 3
    swFacePropOuterLoops = 4

class swDraftStepType_e(IntEnum):
    """swDraftStepType_e (2 constants, from SwConst)."""
    swDraftTaperedStep = 3
    swDraftPerpendicular = 6

class swDraftType_e(IntEnum):
    """swDraftType_e (3 constants, from SwConst)."""
    swNeutralPlaneDraft = 0
    swPartingLineDraft = 1
    swStepDraft = 3

class swDragArrowManipulatorOptions_e(IntEnum):
    """swDragArrowManipulatorOptions_e (2 constants, from SwConst)."""
    swDragArrowManipulatorDirection1 = 0
    swDragArrowManipulatorDirection2 = 1

class swDrawingComponentLineFontOption_e(IntEnum):
    """swDrawingComponentLineFontOption_e (5 constants, from SwConst)."""
    swDrawingComponentLineFontVisible = 1
    swDrawingComponentLineFontHidden = 2
    swDrawingComponentLineFontTangent = 3
    swDrawingComponentLineFontHatch = 4
    swDrawingComponentLineFontSpeedpak = 5

class swDrawingMode_e(IntEnum):
    """swDrawingMode_e (3 constants, from SwConst)."""
    swDrawingMode_None = 0
    swDrawingMode_Resolved = 1
    swDrawingMode_Detailing = 2

class swDrawingNotify_e(IntEnum):
    """swDrawingNotify_e (63 constants, from SwConst)."""
    swDrawingRegenNotify = 1
    swDrawingDestroyNotify = 2
    swDrawingRegenPostNotify = 3
    swDrawingViewNewNotify = 4
    swDrawingNewSelectionNotify = 5
    swDrawingFileSaveNotify = 6
    swDrawingFileSaveAsNotify = 7
    swDrawingLoadFromStorageNotify = 8
    swDrawingSaveToStorageNotify = 9
    swDrawingAutoSaveNotify = 10
    swDrawingAutoSaveToStorageNotify = 11
    swDrawingConfigChangeNotify = 12
    swDrawingConfigChangePostNotify = 13
    swDrawingViewNewNotify2 = 14
    swDrawingAddItemNotify = 15
    swDrawingRenameItemNotify = 16
    swDrawingDeleteItemNotify = 17
    swDrawingModifyNotify = 18
    swDrawingFileReloadNotify = 19
    swDrawingAddCustomPropertyNotify = 20
    swDrawingChangeCustomPropertyNotify = 21
    swDrawingDeleteCustomPropertyNotify = 22
    swDrawingFileSaveAsNotify2 = 23
    swDrawingDeleteSelectionPreNotify = 24
    swDrawingFileReloadPreNotify = 25
    swDrawingFileSavePostNotify = 26
    swDrawingLoadFromStorageStoreNotify = 27
    swDrawingSaveToStorageStoreNotify = 28
    swDrawingFeatureManagerTreeRebuildNotify = 29
    swDrawingViewCreatePreNotify = 30
    swDrawingDynamicHighlightNotify = 31
    swDrawingDimensionChangeNotify = 32
    swDrawingFileReloadCancelNotify = 33
    swDrawingFileSavePostCancelNotify = 34
    swDrawingSketchSolveNotify = 35
    swDrawingDeleteItemPreNotify = 36
    swDrawingClearSelectionsNotify = 37
    swDrawingEquationEditorPreNotify = 38
    swDrawingEquationEditorPostNotify = 39
    swDrawingAddDvePagePreNotify = 40
    swDrawingUnitsChangeNotify = 41
    swDrawingDestroyNotify2 = 42
    swDrawingUndoPostNotify = 43
    swDrawingUserSelectionPreNotify = 44
    swDrawingRedoPostNotify = 45
    swDrawingRedoPreNotify = 46
    swDrawingUndoPreNotify = 47
    swDrawingAutoSaveToStorageStoreNotify = 48
    swDrawingInsertTableNotify = 49
    swDrawingModifyTableNotify = 50
    swDrawingUserSelectionPostNotify = 51
    swDrawingActivateSheetPreNotify = 52
    swDrawingActivateSheetPostNotify = 53
    swDrawingCommandManagerTabActivatedPreNotify = 54
    swDrawingFeatureManagerTabActivatedPreNotify = 55
    swDrawingFeatureManagerTabActivatedNotify = 56
    swDrawingRenameDisplayTitleNotify = 57
    swDrawingDisplayPaneExpandNotify = 58
    swDrawingDisplayPaneCollapseNotify = 59
    swDrawingStateChangeNotify = 60
    swViewPositionChangeNotify = 61
    swDrawingAddDependencyNotify = 62
    swDrawingDeleteDependencyNotify = 63

class swDrawingProjectionType_e(IntEnum):
    """swDrawingProjectionType_e (2 constants, from SwConst)."""
    swDrawing1stAngleProjection = 1
    swDrawing3rdAngleProjection = 2

class swDrawingSheetsZonesLetterLayout_e(IntEnum):
    """swDrawingSheetsZonesLetterLayout_e (2 constants, from SwConst)."""
    swDrawingSheetsZonesLetterLayout_Column = 0
    swDrawingSheetsZonesLetterLayout_Row = 1

class swDrawingSheetsZonesOrigin_e(IntEnum):
    """swDrawingSheetsZonesOrigin_e (4 constants, from SwConst)."""
    swDrawingSheetsZones_UpperLeft = 0
    swDrawingSheetsZones_UpperRight = 1
    swDrawingSheetsZones_LowerLeft = 2
    swDrawingSheetsZones_LowerRight = 3

class swDrawingViewTypes_e(IntEnum):
    """swDrawingViewTypes_e (10 constants, from SwConst)."""
    swDrawingSheet = 1
    swDrawingSectionView = 2
    swDrawingDetailView = 3
    swDrawingProjectedView = 4
    swDrawingAuxiliaryView = 5
    swDrawingStandardView = 6
    swDrawingNamedView = 7
    swDrawingRelativeView = 8
    swDrawingDetachedView = 9
    swDrawingAlternatePositionView = 10

class swDwgImportEntitiesPositioning_e(IntEnum):
    """swDwgImportEntitiesPositioning_e (2 constants, from SwConst)."""
    swDwgEntitiesCentered = 1
    swDwgEntitiesSpecifyPosition = 2

class swDwgPaperSizes_e(IntEnum):
    """swDwgPaperSizes_e (13 constants, from SwConst)."""
    swDwgPaperAsize = 0
    swDwgPaperAsizeVertical = 1
    swDwgPaperBsize = 2
    swDwgPaperCsize = 3
    swDwgPaperDsize = 4
    swDwgPaperEsize = 5
    swDwgPaperA4size = 6
    swDwgPaperA4sizeVertical = 7
    swDwgPaperA3size = 8
    swDwgPaperA2size = 9
    swDwgPaperA1size = 10
    swDwgPaperA0size = 11
    swDwgPapersUserDefined = 12

class swDwgTemplates_e(IntEnum):
    """swDwgTemplates_e (14 constants, from SwConst)."""
    swDwgTemplateAsize = 0
    swDwgTemplateAsizeVertical = 1
    swDwgTemplateBsize = 2
    swDwgTemplateCsize = 3
    swDwgTemplateDsize = 4
    swDwgTemplateEsize = 5
    swDwgTemplateA4size = 6
    swDwgTemplateA4sizeVertical = 7
    swDwgTemplateA3size = 8
    swDwgTemplateA2size = 9
    swDwgTemplateA1size = 10
    swDwgTemplateA0size = 11
    swDwgTemplateCustom = 12
    swDwgTemplateNone = 13

class swDxfFormat_e(IntEnum):
    """swDxfFormat_e (9 constants, from SwConst)."""
    swDxfFormat_R12 = 0
    swDxfFormat_R13 = 1
    swDxfFormat_R14 = 2
    swDxfFormat_R2000 = 3
    swDxfFormat_R2004 = 4
    swDxfFormat_R2007 = 5
    swDxfFormat_R2010 = 6
    swDxfFormat_R2013 = 7
    swDxfFormat_R2018 = 8

class swDxfMultisheet_e(IntEnum):
    """swDxfMultisheet_e (3 constants, from SwConst)."""
    swDxfActiveSheetOnly = 0
    swDxfSeparateSheets = 1
    swDxfMultiSheet = 2

class swDynamicMode_e(IntEnum):
    """swDynamicMode_e (7 constants, from SwConst)."""
    swNoDynamics = 0
    swSpinDynamics = 1
    swPanDynamics = 2
    swZoomDynamics = 3
    swUnknownDynamics = 4
    swAnimDynamics = 5
    swDragDynamics = 6

class swEdgeFlangeError_e(IntEnum):
    """swEdgeFlangeError_e (8 constants, from SwConst)."""
    swEdgeFlangeError_NoError = 0
    swEdgeFlangeError_EdgeNotSpecified = 1
    swEdgeFlangeError_SketchNotSpecified = 2
    swEdgeFlangeError_NumberOfEdgesAndSketchesNotEqual = 3
    swEdgeFlangeError_EdgeAlreadyExists = 4
    swEdgeFlangeError_InvalidEdge = 5
    swEdgeFlangeError_MustSpecifyAtLeastOneEdge = 6
    swEdgeFlangeError_GenericError = 7

class swEdgeUntrimType_e(IntEnum):
    """swEdgeUntrimType_e (2 constants, from SwConst)."""
    swEdgeUntrimTypeExtendEdges = 2
    swEdgeUntrimTypeConnectEndPoints = 1

class swEdgesHiddenEdgeDisplay_e(IntEnum):
    """swEdgesHiddenEdgeDisplay_e (2 constants, from SwConst)."""
    swEdgesHiddenEdgeDisplaySolid = 1
    swEdgesHiddenEdgeDisplayDashed = 2

class swEdgesInContextEditTransparencyType_e(IntEnum):
    """swEdgesInContextEditTransparencyType_e (3 constants, from SwConst)."""
    swEdgesInContextEditTransparency_OpaqueAssembly = 1
    swEdgesInContextEditTransparency_MaintainAssembly = 2
    swEdgesInContextEditTransparency_ForceAssembly = 3

class swEdgesShadedModeDisplay_e(IntEnum):
    """swEdgesShadedModeDisplay_e (3 constants, from SwConst)."""
    swEdgesShadedModeDisplayNone = 1
    swEdgesShadedModeDisplayHLR = 2
    swEdgesShadedModeDisplayWireframe = 3

class swEdgesTangentEdgeDisplay_e(IntEnum):
    """swEdgesTangentEdgeDisplay_e (3 constants, from SwConst)."""
    swEdgesTangentEdgeDisplayVisible = 1
    swEdgesTangentEdgeDisplayPhantom = 2
    swEdgesTangentEdgeDisplayRemoved = 3

class swEditBalloonOption_e(IntEnum):
    """swEditBalloonOption_e (2 constants, from SwConst)."""
    swEditBalloonOption_Replace = 0
    swEditBalloonOption_Resequence = 1

class swEditPartCommandStatus_e(IntEnum):
    """swEditPartCommandStatus_e (7 constants, from SwConst)."""
    swEditPartFailure = -1
    swEditPartAsmMustBeSaved = -2
    swEditPartCompMustBeSelected = -3
    swEditPartCompMustBeResolved = -4
    swEditPartCompMustHaveWriteAccess = -5
    swEditPartSuccessful = 0
    swEditPartCompNotPositioned = 1

class swEdrawingSaveAsOption_e(IntEnum):
    """swEdrawingSaveAsOption_e (3 constants, from SwConst)."""
    swEdrawingSaveActive = 1
    swEdrawingSaveAll = 2
    swEdrawingSaveSelected = 3

class swEdrawingsAttachmentOption_e(IntEnum):
    """swEdrawingsAttachmentOption_e (4 constants, from SwConst)."""
    swEdrawingsAttachNone = 0
    swEdrawingsAttachActive = 1
    swEdrawingsAttachAll = 2
    swEdrawingsAttachSelected = 3

class swEdrawingsAttachmentType_e(IntEnum):
    """swEdrawingsAttachmentType_e (4 constants, from SwConst)."""
    swAP_Unknown = 0
    swAP_203 = 1
    swAP_214 = 2
    swAP_242 = 3

class swElectricalConnectionPointType_e(IntEnum):
    """swElectricalConnectionPointType_e (6 constants, from SwConst)."""
    swElectricalConnectionPoint_Harness = 1
    swElectricalConnectionPoint_CableOrWire = 2
    swElectricalConnectionPoint_Conduit = 3
    swElectricalConnectionPoint_RibbonCable = 4
    swElectricalConnectionPoint_CableTray = 5
    swElectricalConnectionPoint_Trunking = 6

class swElectricalRouteSubType_e(IntEnum):
    """swElectricalRouteSubType_e (4 constants, from SWRoutingLib)."""
    swRouteSubType_Harness = 0
    swRouteSubType_CableWire = 1
    swRouteSubType_Conduit = 2
    swRouteSubType_Ribbon = 3

class swElectricalStreamType_e(IntEnum):
    """swElectricalStreamType_e (4 constants, from SWRoutingLib)."""
    swAllStreams = 0
    swFromToListStream = 2
    swSegmentDataStream = 3
    swWireListStream = 4

class swElectricalSubType_e(IntEnum):
    """swElectricalSubType_e (6 constants, from SwConst)."""
    swElectricalSubType_ElectricalHarness = 0
    swElectricalSubType_ElectricalCableWire = 1
    swElectricalSubType_ElectricalConduit = 2
    swElectricalSubType_ElectricalStandardCable = 3
    swElectricalSubType_NotElectrical = 20
    swElectricalSubType_ElectricalRibbonCable = 30

class swEllipsePts_e(IntEnum):
    """swEllipsePts_e (5 constants, from SwConst)."""
    swEllipseStartPt = 0
    swEllipseEndPt = 1
    swEllipseCenterPt = 2
    swEllipseMajorPt = 3
    swEllipseMinorPt = 4

class swEndCapThicknessDirection_e(IntEnum):
    """swEndCapThicknessDirection_e (3 constants, from SwConst)."""
    swExtendOutward = 1
    swExtendInward = 2
    swSpecifyInset = 3

class swEndConditions_e(IntEnum):
    """swEndConditions_e (11 constants, from SwConst)."""
    swEndCondBlind = 0
    swEndCondThroughAll = 1
    swEndCondThroughNext = 2
    swEndCondUpToVertex = 3
    swEndCondUpToSurface = 4
    swEndCondOffsetFromSurface = 5
    swEndCondMidPlane = 6
    swEndCondUpToBody = 7
    swEndCondThroughAllBoth = 9
    swEndCondUpToSelection = 10
    swEndCondUpToNext = 11

class swEndShape_e(IntEnum):
    """swEndShape_e (2 constants, from SwConst)."""
    swEndShape_DrillPoint = 0
    swEndShape_FlatBottom = 1

class swExcludeFromBOMError_e(IntEnum):
    """swExcludeFromBOMError_e (3 constants, from SwConst)."""
    swExcludeFromBOM_Fail = 0
    swExcludeFromBOM_Success = 1
    swExcludeFromBOM_EnvelopedComponent = 2

class swExplodeDirectionIndex_e(IntEnum):
    """swExplodeDirectionIndex_e (4 constants, from SwConst)."""
    swExplodeDirectionIndex_Unknown = -1
    swExplodeDirectionIndex_XAxis = 0
    swExplodeDirectionIndex_YAxis = 1
    swExplodeDirectionIndex_ZAxis = 2

class swExportDataFileType_e(IntEnum):
    """swExportDataFileType_e (1 constants, from SwConst)."""
    swExportPdfData = 1

class swExportDataSheetsToExport_e(IntEnum):
    """swExportDataSheetsToExport_e (3 constants, from SwConst)."""
    swExportData_ExportAllSheets = 1
    swExportData_ExportCurrentSheet = 2
    swExportData_ExportSpecifiedSheets = 3

class swExportFlatPatternViewOptions_e(IntEnum):
    """swExportFlatPatternViewOptions_e (2 constants, from SwConst)."""
    swExportFlatPatternOption_None = 0
    swExportFlatPatternOption_RemoveBends = 1

class swExportGeomOptions_e(IntEnum):
    """swExportGeomOptions_e (4 constants, from SwConst)."""
    swExportNone = -2
    swExportGeomAsPoly = -1
    swExportViewAsBlock = 0
    swExportTopLevelCompAsBlock = 1

class swExportSVPJFileFormatGroupType_e(IntEnum):
    """swExportSVPJFileFormatGroupType_e (2 constants, from SwConst)."""
    swExportSVPJGroupType_ByAppearance = 0
    swExportSVPJGroupType_ByPart = 1

class swExportToDWG_e(IntEnum):
    """swExportToDWG_e (3 constants, from SwConst)."""
    swExportToDWG_ExportSheetMetal = 1
    swExportToDWG_ExportSelectedFacesOrLoops = 2
    swExportToDWG_ExportAnnotationViews = 3

class swExportTubeDataReportType_e(IntEnum):
    """swExportTubeDataReportType_e (2 constants, from SWRoutingLib)."""
    swExportTubeDataReportType_Tangent = 1
    swExportTubeDataReportType_XYZ = 2

class swExternalFileReferencesConfig_e(IntEnum):
    """swExternalFileReferencesConfig_e (3 constants, from SwConst)."""
    swExternalFileReferencesConfigNone = 0
    swExternalFileReferencesCurrentConfig = 1
    swExternalFileReferencesNamedConfig = 2

class swExternalFileReferencesUpdate_e(IntEnum):
    """swExternalFileReferencesUpdate_e (4 constants, from SwConst)."""
    swExternalFileReferencesUpdateNone = 0
    swExternalFileReferencesBreakAll = 1
    swExternalFileReferencesLockAll = 2
    swExternalFileReferencesunlockAll = 3

class swExternalReferenceStatus_e(IntEnum):
    """swExternalReferenceStatus_e (5 constants, from SwConst)."""
    swExternalReferenceBroken = 0
    swExternalReferenceLocked = 1
    swExternalReferenceInContext = 3
    swExternalReferenceOutOfContext = 4
    swExternalReferenceDangling = 5

class swExternalReferencesUpdateOutOfDateLinkedDesignTable_e(IntEnum):
    """swExternalReferencesUpdateOutOfDateLinkedDesignTable_e (3 constants, from SwConst)."""
    swUpdateDesignTable_Prompt = 0
    swUpdateDesignTable_Model = 1
    swUpdateLinkedDesignTable_ExcelFile = 2

class swExtrudeFrom_e(IntEnum):
    """swExtrudeFrom_e (4 constants, from SwConst)."""
    swExtrudeFrom_SketchPlane = 0
    swExtrudeFrom_SurfaceFacePlane = 1
    swExtrudeFrom_Vertex = 2
    swExtrudeFrom_Offset = 3

class swFMViewNotify_e(IntEnum):
    """swFMViewNotify_e (3 constants, from SwConst)."""
    swFMViewActivateNotify = 1
    swFMViewDeactivateNotify = 2
    swFMViewDestroyNotify = 3

class swFaceCoincidentResult_e(IntEnum):
    """swFaceCoincidentResult_e (9 constants, from SwConst)."""
    swFaceCoincidentUnknownResult = -1
    swFaceCoincident_True = 0
    swFaceCoincident_TrueReversed = 1
    swFaceCoincident_FalseTopology = 2
    swFaceCoincident_FalseBoundary1 = 3
    swFaceCoincident_FalseBoundary2 = 4
    swFaceCoincident_FalseFace1 = 5
    swFaceCoincident_FalseFace2 = 6
    swFaceCoincident_FalseSurface = 7

class swFaceDeleteOption_e(IntEnum):
    """swFaceDeleteOption_e (4 constants, from SwConst)."""
    swFaceDelete_Default = 0
    swFaceDelete_Patch = 1
    swFaceDelete_Fill = 2
    swFaceDelete_FillWithTangent = 3

class swFaceUntrimType_e(IntEnum):
    """swFaceUntrimType_e (3 constants, from SwConst)."""
    swFaceUntrimTypeAllEdges = 0
    swFaceUntrimTypeInternalEdges = 1
    swFaceUntrimTypeExternalEdges = 2

class swFamilyTableDimColumnType_e(IntEnum):
    """swFamilyTableDimColumnType_e (3 constants, from SwConst)."""
    swFamilyTable_TableControlled = 1
    swFamilyTable_MarkedForDrawing = 2
    swFamilyTable_NotMarkedForDrawing = 4

class swFamilyTableGetConfigurationCriteria_e(IntEnum):
    """swFamilyTableGetConfigurationCriteria_e (3 constants, from SwConst)."""
    GetAllConfigurationsAvailableNames = 0
    GetJustEnabledConfigurationNames = 1
    GetJustVisibleConfigurationNames = 2

class swFastenerTableTypes_e(IntEnum):
    """swFastenerTableTypes_e (3 constants, from SwConst)."""
    swSizeTable = 0
    swThreadDataTable = 1
    swScrewClearancesTable = 2

class swFaultEntityErrorCode_e(IntEnum):
    """swFaultEntityErrorCode_e (36 constants, from SwConst)."""
    swBodyCorrupt = 1
    swBodyInvalidIdentifiers = 2
    swBodyInsideOut = 3
    swBodyRegionsInconsistent = 4
    swEdgeNonPeriodicCurve = 5
    swEdgeNonPeriodicNomGeom = 6
    swEdgeVertexNotLie = 7
    swEdgeVertexNotLieNomGeom = 8
    swEdgeWrongDir = 9
    swEdgeWrongDirNomGeom = 10
    swEdgeSpcurveOutOfTol = 11
    swEdgeSpcurveOutOfTolNomGeom = 12
    swEdgeVerticesTouch = 13
    swEdgeBadFaceOrder = 14
    swEdgeBadWire = 15
    swFaceBadVertex = 16
    swFaceBadEdge = 17
    swFaceBadEdgeOrder = 18
    swFaceNoAccomVertex = 19
    swFaceBadLoops = 20
    swFaceSelfIntersecting = 21
    swFaceBadWireframe = 22
    swFaceCheckerFailure = 23
    swFaceFaceInconsistency = 24
    swGeomStateSelfIntersect = 25
    swGeomDegenerate = 26
    swRegionBadShells = 27
    swShellBadTopologyGeometry = 28
    swShellIntersect = 29
    swTopolNotG1Continuous = 30
    swTopolSizeBoxViolation = 31
    swTopolStateCheckFail = 32
    swTopolStateNoGeometry = 33
    swEntityStateInvalid = 34
    swTopolMissingGeometry = 35
    swEdgeTouchEdge = 36

class swFeatMgrPane_e(IntEnum):
    """swFeatMgrPane_e (5 constants, from SwConst)."""
    swFeatMgrPaneTop = 0
    swFeatMgrPaneBottom = 1
    swFeatMgrPaneTopHidden = 2
    swFeatMgrPaneBottomHidden = 3
    swFeatMgrPaneFlyout = 4

class swFeatureChamferOption_e(IntEnum):
    """swFeatureChamferOption_e (4 constants, from SwConst)."""
    swFeatureChamferFlipDirection = 1
    swFeatureChamferKeepFeature = 2
    swFeatureChamferTangentPropagation = 4
    swFeatureChamferPropagateFeatToParts = 8

class swFeatureDimensionParameter_e(IntEnum):
    """swFeatureDimensionParameter_e (4 constants, from SwConst)."""
    swPatternSpacing1 = 1
    swPatternInstanceCount1 = 2
    swPatternSpacing2 = 3
    swPatternInstanceCount2 = 4

class swFeatureEditStatus_e(IntEnum):
    """swFeatureEditStatus_e (3 constants, from SwConst)."""
    swFeature_Editable = 0
    swFeature_NonEditable = 1
    swFeature_UnderEditing = 2

class swFeatureError_e(IntEnum):
    """swFeatureError_e (56 constants, from SwConst)."""
    swFeatureErrorNone = 0
    swFeatureErrorUnknown = 1
    swFeatureErrorFilletNoLoop = 10
    swFeatureErrorFilletNoFace = 11
    swFeatureErrorFilletInvalidRadius = 12
    swFeatureErrorFilletNoEdge = 13
    swFeatureErrorFilletModelGeometry = 14
    swFeatureErrorFilletRadiusTooSmall = 15
    swFeatureErrorFilletCannotExtend = 16
    swFeatureErrorFilletRadiusEliminateElement = 17
    swFeatureErrorFilletRadiusTooBig = 18
    swFeatureErrorFilletRadiusTooBig2 = 19
    swFeatureErrorExtrusionDisjoint = 30
    swFeatureErrorExtrusionNoEndFound = 31
    swFeatureErrorExtrusionBadGeometricConditions = 32
    swFeatureErrorExtrusionCutContourOpenAndClosed = 33
    swFeatureErrorExtrusionCutContourInvalid = 34
    swFeatureErrorExtrusionOpenCutContourInvalid = 35
    swFeatureErrorExtrusionBossContourOpenAndClosed = 36
    swFeatureErrorExtrusionBossContourInvalid = 37
    swFeatureErrorMateInvalidEdge = 38
    swFeatureErrorMateInvalidFace = 39
    swFeatureErrorMateFailedCreatingSurface = 40
    swFeatureErrorMateInvalidEntity = 41
    swFeatureErrorMateUnknownTangent = 42
    swFeatureErrorMateDanglingGeometry = 43
    swFeatureErrorMateEntityNotLinear = 44
    swFeatureErrorMateEntityFailed = 45
    swFeatureErrorMateOverdefined = 46
    swFeatureErrorMateIlldefined = 47
    swFeatureErrorMateBroken = 48
    swFeatureErrorFeatureDeprecated = 49
    swFeatureErrorFeatureObsolete = 50
    swSketchErrorExtRefFail = 51
    swFeatureErrorPartialEdgeFilletNoIntersection = 52
    swFeatureErrorPartialEdgeFilletUpdateFailed = 53
    swFeatureErrorPartialEdgeFilletNoPropagateEdges = 54
    swFeatureErrorPartialEdgeFilletNoStartEdge = 55
    swFeatureErrorPartialEdgeFilletNoEndEdge = 56
    swFeatureErrorPartialEdgeFilletNoMainEdge = 57
    swFeatureErrorPartialEdgeFilletOffsetTooBig = 58
    swFeatureErrorPartialEdgeFilletNoReferenceEntity = 59
    swFeatureErrorPartialEdgeFilletTooManyRefEntities = 60
    swFeatureErrorPartialEdgeFilletInvalidOffsetValue = 61
    swFeatureErrorPartialEdgeFilletCrossOverEndCondition = 62
    swFeatureErrorPartialEdgeFilletMissingReferenceEntity = 63
    swFeatureErrorPartialEdgeFilletInvalidReferenceEntity = 64
    swFeatureErrorPartialEdgeFilletNotSupported = 65
    swFeatureErrorPartialEdgeFilletNotSupportedForClosedLoop = 66
    swFeatureErrorPartialEdgeFilletMultiProjectionPoint = 67
    swFeatureErrorPartialEdgeFilletFailedToRepair = 68
    swFeatureErrorSweptFlangeInvalidProfileOrPath = 69
    swFeatureErrorSweptFlangeSelfIntersectingGeometry = 70
    swFeatureErrorCutNotIntersectModel = 71
    swFeatureErrorSketchContainsSelfIntersectingContour = 72
    swFeatureErrorMissingItemsInFeature = 73

class swFeatureFillSurfaceOptions_e(IntEnum):
    """swFeatureFillSurfaceOptions_e (5 constants, from SwConst)."""
    swOptimizeSurface = 1
    swTryToFormSolid = 2
    swMergeResult = 4
    swReverseDirection = 8
    swReverseSurface = 16

class swFeatureFilletOptions_e(IntEnum):
    """swFeatureFilletOptions_e (15 constants, from SwConst)."""
    swFeatureFilletPropagate = 1
    swFeatureFilletUniformRadius = 2
    swFeatureFilletVarRadiusType = 4
    swFeatureFilletUseHelpPoint = 8
    swFeatureFilletUseTangentHoldLine = 16
    swFeatureFilletCornerType = 32
    swFeatureFilletAttachEdges = 64
    swFeatureFilletKeepFeatures = 128
    swFeatureFilletCurvatureContinuous = 256
    swFeatureFilletConstantWidth = 512
    swFeatureFilletNoTrimNoAttached = 1024
    swFeatureFilletReverseFace1Dir = 2048
    swFeatureFilletReverseFace2Dir = 4096
    swFeatureFilletPropagateFeatToParts = 8192
    swFeatureFilletAsymmetric = 16384

class swFeatureFilletProfileType_e(IntEnum):
    """swFeatureFilletProfileType_e (4 constants, from SwConst)."""
    swFeatureFilletCircular = 0
    swFeatureFilletConicRho = 1
    swFeatureFilletConicRadius = 2
    swFeatureFilletConicRhoZeroChamfer = 3

class swFeatureFilletType_e(IntEnum):
    """swFeatureFilletType_e (4 constants, from SwConst)."""
    swFeatureFilletType_Simple = 0
    swFeatureFilletType_VariableRadius = 1
    swFeatureFilletType_Face = 2
    swFeatureFilletType_FullRound = 3

class swFeatureManagerDisplayWarnings_e(IntEnum):
    """swFeatureManagerDisplayWarnings_e (3 constants, from SwConst)."""
    swFeatureManagerDisplayAllWarnings = 0
    swFeatureManagerDisplayNoWarnings = 1
    swFeatureManagerDisplayWarningsExceptTopLevel = 2

class swFeatureManagerTreeViewCADFamily_e(IntEnum):
    """swFeatureManagerTreeViewCADFamily_e (2 constants, from SwConst)."""
    swFeatureManagerTreeViewCADFamily_CADFamilyOnly = 0
    swFeatureManagerTreeViewCADFamily_CADFamilyAndConfiguration = 1

class swFeatureModifier_e(IntEnum):
    """swFeatureModifier_e (8 constants, from SwConst)."""
    swGeometricFeatureModifier_None = 0
    swGeometricFeatureModifier_MaximumMaterialCondition = 1
    swGeometricFeatureModifier_LeastMaterialCondition = 2
    swGeometricFeatureModifier_ProjectedTolerance = 3
    swGeometricFeatureModifier_TangentPlane = 4
    swGeometricFeatureModifier_FreeState = 5
    swGeometricFeatureModifier_ToleranceAsDiameter = 6
    swGeometricFeatureModifier_Unknown = 7

class swFeatureNameID_e(IntEnum):
    """swFeatureNameID_e (130 constants, from SwConst)."""
    swFmChamfer = 0
    swFmFillet = 1
    swFmCavity = 2
    swFmDraft = 3
    swFmMirrorSolid = 4
    swFmCirPattern = 5
    swFmLPattern = 6
    swFmMirrorPattern = 7
    swFmShell = 8
    swFmBlend = 9
    swFmBlendCut = 10
    swFmExtrusion = 11
    swFmBoss = 12
    swFmCut = 13
    swFmRefCurve = 14
    swFmRevolution = 15
    swFmRevCut = 16
    swFmSweep = 17
    swFmSweepCut = 18
    swFmStock = 19
    swFmSurfCut = 20
    swFmThicken = 21
    swFmThickenCut = 22
    swFmVarFillet = 23
    swFmSketchHole = 24
    swFmHoleWzd = 25
    swFmImported = 26
    swFmBaseBody = 27
    swFmDerivedLPattern = 28
    swFmCosmeticThread = 29
    swFmSheetMetal = 30
    swFmFlattenBends = 31
    swFmProcessBends = 32
    swFmOneBend = 33
    swFmBaseFlange = 34
    swFmSketchBend = 35
    swFmSM3dBend = 36
    swFmEdgeFlange = 37
    swFmFlatPattern = 38
    swFmCenterMark = 39
    swFmDrSheet = 40
    swFmAbsoluteView = 41
    swFmDetailView = 42
    swFmRelativeView = 43
    swFmSectionPartView = 44
    swFmSectionAssemView = 45
    swFmUnfoldedView = 46
    swFmAuxiliaryView = 47
    swFmDetailCircle = 48
    swFmDrSectionLine = 49
    swFmBomTableFeature = 50
    swFmHoleTableFeature = 51
    swFmRevisionTableFeature = 52
    swFmMateCoincident = 53
    swFmMateConcentric = 54
    swFmMateDistanceDim = 55
    swFmMateParallel = 56
    swFmMateTangent = 57
    swFmReference = 58
    swFmRefPlane = 59
    swFmRefAxis = 60
    swFmReferenceCurve = 61
    swFmRefSurface = 62
    swFmCoordinateSystem = 63
    swFmAttribute = 64
    swFmProfileFeature = 65
    swFmFeatureFolder = 66
    swFmSurfaceBodyFolder = 67
    swFmSolidBodyFolder = 68
    swFmLibraryFeature = 69
    swFmBreakCorner = 70
    swFmCornerTrim = 71
    swFmWeldMemberFeat = 72
    swFmFormToolInstance = 73
    swFmAEMGravity = 74
    swFmAEMLinearForce = 75
    swFmAEMTorque = 76
    swFmAEMLinearMotor = 77
    swFmAEMRotationalMotor = 78
    swFmAEMLinearSpring = 79
    swFmAEMTorsionalSpring = 80
    swFmAEMLinearMotionSpring = 81
    swFmAEMTorsionalMotionSpring = 82
    swFmAEMLinearDamper = 83
    swFmAEMTorsionalDamper = 84
    swFmAEM3DContact = 85
    swFmCrossBreak = 86
    swFmSweepThread = 87
    swFmTabAndSlot = 88
    swFmMatePerpendicular = 89
    swFmMateLock = 90
    swFmMateCamTangent = 91
    swFmMateSlot = 92
    swFmMatePlanarAngleDim = 93
    swFmMateHinge = 94
    swFmMateRackPinionDim = 95
    swFmMateGearDim = 96
    swFmMateScrew = 97
    swFmMateUniversalJoint = 98
    swFmMateSymmetric = 99
    swFmMateWidth = 100
    swFmMateProfileCenter = 101
    swFmMateLinearCoupler = 102
    swFmCurvePattern = 103
    swFmSketchPattern = 104
    swFmFillPattern = 105
    swFmTablePattern = 106
    swFmDimPattern = 107
    swFmLocalLPattern = 108
    swFmLocalCirPattern = 109
    swFmLocalCurvePattern = 110
    swFmLocalSketchPattern = 111
    swFmLocalChainPattern = 112
    swFmGroundPlane = 113
    swFmBoundingBox = 114
    swFmNormalCut = 115
    swFmMirrorComponent = 116
    swFmSweptFlange = 117
    swFmSMGusset = 118
    swFmBeltAndChain = 119
    swFmCornerRelief = 120
    swFmStrctSysFeat = 121
    swFmStrctSysGrpFeat = 122
    swFmStrctSysMbrFeat = 123
    swFmStrctSysCnrMgmtFeat = 124
    swFmStrctSysCnrGrpFeat = 125
    swFmStrctSysCnrFeat = 126
    swFmMateController = 127
    swFmSolidToSheetMetal = 128
    swFmFamilyTableFeature = 129

class swFeatureScope_e(IntEnum):
    """swFeatureScope_e (3 constants, from SwConst)."""
    swFeatureScope_AllBodies = 0
    swFeatureScope_SelectedBodiesWithAutoSelect = 1
    swFeatureScope_SelectedBodiesWithOutAutoSelect = 2

class swFeatureSuppressionAction_e(IntEnum):
    """swFeatureSuppressionAction_e (3 constants, from SwConst)."""
    swSuppressFeature = 0
    swUnSuppressFeature = 1
    swUnSuppressDependent = 2

class swFeatureTreeFolderType_e(IntEnum):
    """swFeatureTreeFolderType_e (3 constants, from SwConst)."""
    swFeatureTreeFolder_EmptyBefore = 1
    swFeatureTreeFolder_Containing = 2
    swFeatureTreeFolder_Mold = 3

class swFeatureTreeState_e(IntEnum):
    """swFeatureTreeState_e (3 constants, from SwConst)."""
    swFlyoutFeatureTree_Hidden = 0
    swFlyoutFeatureTree_ShownUnExpanded = 1
    swFlyoutFeatureTree_ShownExpanded = 2

class swFeaturesToPatternType_e(IntEnum):
    """swFeaturesToPatternType_e (2 constants, from SwConst)."""
    swFeaturesToPatternSelectedFeatures = 0
    swFeaturesToPatternCreateSeedCut = 1

class swFileCloseNotifyReason_e(IntEnum):
    """swFileCloseNotifyReason_e (2 constants, from SwConst)."""
    swFileCloseNotifyReason_Unknown = 0
    swFileCloseNotifyReason_CloseForReload = 1

class swFileFormatType_e(IntEnum):
    """swFileFormatType_e (4 constants, from SwConst)."""
    swFileFormatType_STEP = 0
    swFileFormatType_STEP_ED1 = 1
    swFileFormatType_STEP_ED2 = 2
    swFileFormatType_STEP_ED3 = 3

class swFileLoadError_e(IntEnum):
    """swFileLoadError_e (25 constants, from SwConst)."""
    swGenericError = 1
    swFileNotFoundError = 2
    swIdMatchError = 4
    swReadOnlyWarn = 8
    swSharingViolationWarn = 16
    swDrawingANSIUpdateWarn = 32
    swSheetScaleUpdateWarn = 64
    swNeedsRegenWarn = 128
    swBasePartNotLoadedWarn = 256
    swFileAlreadyOpenWarn = 512
    swInvalidFileTypeError = 1024
    swDrawingsOnlyRapidDraftWarn = 2048
    swViewOnlyRestrictions = 4096
    swFutureVersion = 8192
    swViewMissingReferencedConfig = 16384
    swDrawingSFSymbolConvertWarn = 32768
    swFileWithSameTitleAlreadyOpen = 65536
    swLiquidMachineDoc = 131072
    swLowResourcesError = 262144
    swNoDisplayData = 524288
    swAddinInteruptError = 1048576
    swFileRequiresRepairError = 2097152
    swFileCriticalDataRepairError = 4194304
    swApplicationBusy = 8388608
    swConnectedIsOffline = 16777216

class swFileLoadWarning_e(IntEnum):
    """swFileLoadWarning_e (21 constants, from SwConst)."""
    swFileLoadWarning_IdMismatch = 1
    swFileLoadWarning_ReadOnly = 2
    swFileLoadWarning_SharingViolation = 4
    swFileLoadWarning_DrawingANSIUpdate = 8
    swFileLoadWarning_SheetScaleUpdate = 16
    swFileLoadWarning_NeedsRegen = 32
    swFileLoadWarning_BasePartNotLoaded = 64
    swFileLoadWarning_AlreadyOpen = 128
    swFileLoadWarning_DrawingsOnlyRapidDraft = 256
    swFileLoadWarning_ViewOnlyRestrictions = 512
    swFileLoadWarning_ViewMissingReferencedConfig = 1024
    swFileLoadWarning_DrawingSFSymbolConvert = 2048
    swFileLoadWarning_RevolveDimTolerance = 4096
    swFileLoadWarning_ModelOutOfDate = 8192
    swFileLoadWarning_DimensionsReferencedIncorrectlyToModels = 16384
    swFileLoadWarning_ComponentMissingReferencedConfig = 32768
    swFileLoadWarning_InvisibleDoc_LinkedDesignTableUpdateFail = 65536
    swFileLoadWarning_MissingDesignTable = 131072
    swFileLoadWarning_AutomaticRepair = 262144
    swFileLoadWarning_CriticalDataRepair = 524288
    swFileLoadWarning_MissingExternalReferences = 1048576

class swFileSaveError_e(IntEnum):
    """swFileSaveError_e (17 constants, from SwConst)."""
    swGenericSaveError = 1
    swReadOnlySaveError = 2
    swFileNameEmpty = 4
    swFileNameContainsAtSign = 8
    swFileLockError = 16
    swFileSaveFormatNotAvailable = 32
    swFileSaveWithRebuildError = 64
    swFileSaveAsDoNotOverwrite = 128
    swFileSaveAsInvalidFileExtension = 256
    swFileSaveAsNoSelection = 512
    swFileSaveAsBadEDrawingsVersion = 1024
    swFileSaveAsNameExceedsMaxPathLength = 2048
    swFileSaveAsNotSupported = 4096
    swFileSaveRequiresSavingReferences = 8192
    swFileSaveAsDetachedDrawingsNotSupported = 16384
    swFileSaveDoNotUpgradeError = 32768
    swFileSaveIncompatibleItemsError = 65536

class swFileSaveTo3DExperienceError_e(IntEnum):
    """swFileSaveTo3DExperienceError_e (3 constants, from SwConst)."""
    swFileSaveTo3DExperienceError_swGenericError = 1
    swFileSaveTo3DExperienceError_swConnectedIsOffline = 2
    swFileSaveTo3DExperienceError_swFileAlreadyExists = 3

class swFileSaveTypes_e(IntEnum):
    """swFileSaveTypes_e (4 constants, from SwConst)."""
    swFileSave = 1
    swFileSaveAs = 2
    swFileSaveAsCopy = 3
    swFileSaveAsCopyAndOpen = 4

class swFileSaveWarning_e(IntEnum):
    """swFileSaveWarning_e (12 constants, from SwConst)."""
    swFileSaveWarning_RebuildError = 1
    swFileSaveWarning_NeedsRebuild = 2
    swFileSaveWarning_ViewsNeedUpdate = 4
    swFileSaveWarning_AnimatorNeedToSolve = 8
    swFileSaveWarning_AnimatorFeatureEdits = 16
    swFileSaveWarning_EdrwingsBadSelection = 32
    swFileSaveWarning_AnimatorLightEdits = 64
    swFileSaveWarning_AnimatorCameraViews = 128
    swFileSaveWarning_AnimatorSectionViews = 256
    swFileSaveWarning_MissingOLEObjects = 512
    swFileSaveWarning_OpenedViewOnly = 1024
    swFileSaveWarning_XmlInvalid = 2048

class swFilletOverFlowType_e(IntEnum):
    """swFilletOverFlowType_e (3 constants, from SwConst)."""
    swFilletOverFlowType_Default = 0
    swFilletOverFlowType_KeepEdge = 1
    swFilletOverFlowType_KeepSurface = 2

class swFitTolDisplay_e(IntEnum):
    """swFitTolDisplay_e (3 constants, from SwConst)."""
    swFitTolDisplay_StackedWithLine = 1
    swFitTolDisplay_Stacked = 2
    swFitTolDisplay_Linear = 3

class swFitType_e(IntEnum):
    """swFitType_e (4 constants, from SwConst)."""
    swFitUSER = 0
    swFitCLEARANCE = 1
    swFitTRANSITIONAL = 2
    swFitPRESS = 3

class swFlangeDimTypes_e(IntEnum):
    """swFlangeDimTypes_e (3 constants, from SwConst)."""
    swFlangeDimTypeOuterVirtualSharp = 1
    swFlangeDimTypeInnerVirtualSharp = 2
    swFlangeDimTypeBendTangentArc = 3

class swFlangeOffsetTypes_e(IntEnum):
    """swFlangeOffsetTypes_e (6 constants, from SwConst)."""
    swFlangeOffsetBlind = 1
    swFlangeOffsetUpToVertex = 2
    swFlangeOffsetUpToSurface = 3
    swFlangeOffsetFromSurface = 4
    swFlangeOffsetMidPlane = 5
    swFlangeOffsetUptoEdgeAndMerge = 6

class swFlangePositionTypes_e(IntEnum):
    """swFlangePositionTypes_e (6 constants, from SwConst)."""
    swFlangePositionTypeMaterialInside = 1
    swFlangePositionTypeMaterialOutside = 2
    swFlangePositionTypeBendOutside = 3
    swFlangePositionTypeBendCenterLine = 4
    swFlangePositionTypeBendSharp = 5
    swFlangePositionTypeBendTangent = 6

class swFlattenRouteErrorType_e(IntEnum):
    """swFlattenRouteErrorType_e (5 constants, from SWRoutingLib)."""
    swNeedsToSaveVirtualComponentError = 1
    swProblemInRouteAssemblyError = 2
    swDuplicateComponentError = 3
    swRouteAssemblyNotSelected = 4
    swFlattenRouteNoError = 5

class swForceUpdateElectricalDataError_e(IntEnum):
    """swForceUpdateElectricalDataError_e (5 constants, from SWRoutingLib)."""
    swForceUpdateElectricalData_Success = 0
    swForceUpdateElectricalData_IncorrectStreamInput = 1
    swForceUpdateElectricalData_IsNotARouteAssembly = 2
    swForceUpdateElectricalData_BadStreamData = 3
    swForceUpdateElectricalData_RouteInEditMode = 4

class swFractionDisplay_e(IntEnum):
    """swFractionDisplay_e (3 constants, from SwConst)."""
    swNONE = 0
    swDECIMAL = 1
    swFRACTION = 2

class swGTolTextParts_e(IntEnum):
    """swGTolTextParts_e (4 constants, from SwConst)."""
    swGTolTextPrefix = 1
    swGTolTextSuffix = 2
    swGTolTextCalloutAbove = 3
    swGTolTextCalloutBelow = 4

class swGeneralImportFreePointCurveEntityOptions_e(IntEnum):
    """swGeneralImportFreePointCurveEntityOptions_e (2 constants, from SwConst)."""
    swGeneralImportAsSketches = 0
    swGeneralImportAs3dCurves = 1

class swGeneralImportSurfaceSolidEntityOptions_e(IntEnum):
    """swGeneralImportSurfaceSolidEntityOptions_e (4 constants, from SwConst)."""
    swGeneralImportTryFormingSolids = 0
    swGeneralImportKnitSurfaces = 1
    swGeneralImportDoNotKnit = 2
    swGeneralImportByBrep = 3

class swGeneralImportUnitsOptions_e(IntEnum):
    """swGeneralImportUnitsOptions_e (2 constants, from SwConst)."""
    swGeneralImportFileSpecifiedUnit = 0
    swGeneralImportDocumentTemplateSpeciedUnit = 1

class swGeomType_e(IntEnum):
    """swGeomType_e (15 constants, from SwConst)."""
    swPOINT = 0
    swLINE = 1
    swARC = 2
    swSPLINECURVE = 3
    swELLIPSE = 4
    swTEXT = 5
    swHATCH = 6
    swPARABOLA = 7
    sw3DPLANE = 8
    sw3DCYLINDER = 9
    sw3DSPHERE = 10
    sw3DPARAMETRICSURFACE = 11
    swDIM = 12
    swSUBSKETCH = 13
    swINVALIDGTYPE = 99

class swGeometricCharacteristic_e(IntEnum):
    """swGeometricCharacteristic_e (16 constants, from SwConst)."""
    swGeometricCharacteristic_None = 0
    swGeometricCharacteristic_Unknown = 1
    swGeometricCharacteristic_Straightness = 2
    swGeometricCharacteristic_Flatness = 3
    swGeometricCharacteristic_Circularity = 4
    swGeometricCharacteristic_Cylindricity = 5
    swGeometricCharacteristic_LineProfile = 6
    swGeometricCharacteristic_SurfaceProfile = 7
    swGeometricCharacteristic_Angularity = 8
    swGeometricCharacteristic_Parallelism = 9
    swGeometricCharacteristic_Perpendicularity = 10
    swGeometricCharacteristic_Position = 11
    swGeometricCharacteristic_Concentricity = 12
    swGeometricCharacteristic_Symmetry = 13
    swGeometricCharacteristic_CircularRunout = 14
    swGeometricCharacteristic_TotalRunout = 15

class swGeometryToSave_e(IntEnum):
    """swGeometryToSave_e (3 constants, from SwConst)."""
    swGeometryToSave_AllComponents = 0
    swGeometryToSave_ExteriorFaces = 1
    swGeometryToSave_IncludeSpecificComponents = 2

class swGetOpenFileNameOptions_e(IntEnum):
    """swGetOpenFileNameOptions_e (16 constants, from SwConst)."""
    swGetOpenFileNameOptions_Silent = 1
    swGetOpenFileNameOptions_ReadOnly = 2
    swGetOpenFileNameOptions_ViewOnly = 4
    swGetOpenFileNameOptions_RapidDraft = 8
    swGetOpenFileNameOptions_LoadModel = 16
    swGetOpenFileNameOptions_AutoMissingConfig = 32
    swGetOpenFileNameOptions_OverrideDefaultLoadLightweight = 64
    swGetOpenFileNameOptions_LoadLightweight = 128
    swGetOpenFileNameOptions_DontLoadHiddenComponents = 256
    swGetOpenFileNameOptions_LoadExternalReferencesInMemory = 512
    swGetOpenFileNameOptions_OpenDetailingMode = 1024
    swGetOpenFileNameOptions_LDR_EditAssembly = 2048
    swGetOpenFileNameOptions_SpeedPak = 4096
    swGetOpenFileNameOptions_AdvancedConfig = 8192
    swGetOpenFileNameOptions_UseLargeAssemblySettings = 16384
    swGetOpenFileNameOptions_SelectedSheets = 32768

class swGlobalBBoxLWTADirectionType_e(IntEnum):
    """swGlobalBBoxLWTADirectionType_e (10 constants, from SwConst)."""
    swBBox_LWTADir_Unspecified = 0
    swBBox_LWTDir_XYZ = 1
    swBBox_LWTDir_YXZ = 2
    swBBox_LWTDir_YZX = 3
    swBBox_LWTDir_ZYX = 4
    swBBox_LWTDir_ZXY = 5
    swBBox_LWTDir_XZY = 6
    swBBox_AxisDir_X = 7
    swBBox_AxisDir_Y = 8
    swBBox_AxisDir_Z = 9

class swGlobalBoundingBoxFitOptions_e(IntEnum):
    """swGlobalBoundingBoxFitOptions_e (3 constants, from SwConst)."""
    swBoundingBoxType_BestFit = 1
    swBoundingBoxType_CustomPlane = 2
    swBoundingBoxType_CustomCoordSys = 3

class swGlobalBoundingBoxResult_e(IntEnum):
    """swGlobalBoundingBoxResult_e (3 constants, from SwConst)."""
    swGlobalBoundingBoxResult_Success = 0
    swGlobalBoundingBoxResult_NoValidBodiesFound = 1
    swGlobalBoundingBoxResult_NonPlanarFaceSelected = 2

class swGtolDecimalSeparatorType_e(IntEnum):
    """swGtolDecimalSeparatorType_e (2 constants, from SwConst)."""
    swGeometricTolerance_Decimal_Separator_Period = 0
    swGeometricTolerance_Decimal_Separator_Comma = 1

class swGtolFormatConversionError_e(IntEnum):
    """swGtolFormatConversionError_e (1 constants, from SwConst)."""
    swGtolFormatConversionFail = 1

class swGtolFormatSchemaVersion_e(IntEnum):
    """swGtolFormatSchemaVersion_e (1 constants, from SwConst)."""
    swGtolFormatSchemaVersion_SW2023 = 1

class swGtolFormatType_e(IntEnum):
    """swGtolFormatType_e (2 constants, from SwConst)."""
    GTOL_SW2021 = 1
    GTOL_SW2022 = 2

class swGtolGeomCharSymbol_e(IntEnum):
    """swGtolGeomCharSymbol_e (19 constants, from SwConst)."""
    swGcsNONE = 12
    swGcsSYMMETRY = 13
    swGcsSTRAIGHT = 14
    swGcsFLAT = 15
    swGcsROUND = 16
    swGcsCYL = 17
    swGcsLINEPROF = 18
    swGcsSURFPROF = 19
    swGcsANG = 20
    swGcsPERP = 21
    swGcsPARALLEL = 22
    swGcsPOSITION = 23
    swGcsCONC = 24
    swGcsCIRCRUNOUT = 25
    swGcsTOTALRUNOUT = 26
    swGcsCIRCOPENRUNOUT = 27
    swGcsTOTALOPENRUNOUT = 28
    swGcsUBUTTON = 29
    swGcsSQUARE = 30

class swGtolIndicatorBorderType_e(IntEnum):
    """swGtolIndicatorBorderType_e (4 constants, from SwConst)."""
    swGtolIndicatorBorderType_OrientationPlane = 0
    swGtolIndicatorBorderType_IntersectionPlane = 1
    swGtolIndicatorBorderType_CollectionPlane = 2
    swGtolIndicatorBorderType_DirectionFeature = 3

class swGtolMatCondition_e(IntEnum):
    """swGtolMatCondition_e (12 constants, from SwConst)."""
    swMcNONE = 0
    swMcMMC = 1
    swMcRFS = 2
    swMcLMC = 3
    swMsNONE = 4
    swMsPROJTOLZONE = 5
    swMsDIA = 6
    swMsSPHDIA = 7
    swMsRAD = 8
    swMsSPHRAD = 9
    swMsREF = 10
    swMsARCLEN = 11

class swGtolTolType_e(IntEnum):
    """swGtolTolType_e (6 constants, from SwConst)."""
    swGtolTolType_None = 0
    swGtolTolType_Unknown = 1
    swGtolTolType_ProjectedTolerance = 2
    swGtolTolType_Square = 3
    swGtolTolType_UnequallyDisposedProfile = 4
    swGtolTolType_MAX = 5

class swGuideCurveInfluence_e(IntEnum):
    """swGuideCurveInfluence_e (4 constants, from SwConst)."""
    swGuideCurveInfluenceNextGuide = 0
    swGuideCurveInfluenceNextSharp = 1
    swGuideCurveInfluenceNextEdge = 2
    swGuideCurveInfluenceNextGlobal = 3

class swGussetProfileLocationType_e(IntEnum):
    """swGussetProfileLocationType_e (3 constants, from SwConst)."""
    swGussetProfileLocationStart = 0
    swGussetProfileLocationCenter = 1
    swGussetProfileLocationEnd = 2

class swGussetProfileType_e(IntEnum):
    """swGussetProfileType_e (2 constants, from SwConst)."""
    swGussetProfilePolygon = 0
    swGussetProfileTriangle = 1

class swGussetThicknessType_e(IntEnum):
    """swGussetThicknessType_e (3 constants, from SwConst)."""
    swGussetThicknessInner = 0
    swGussetThicknessBothSides = 1
    swGussetThicknessOuter = 2

class swHandleActiveXCreationFailure_e(IntEnum):
    """swHandleActiveXCreationFailure_e (3 constants, from SwConst)."""
    swHandleActiveXCreationFailure_Cancel = 1
    swHandleActiveXCreationFailure_Retry = 2
    swHandleActiveXCreationFailure_Continue = 3

class swHandleWindowFromHandleCreationFailure_e(IntEnum):
    """swHandleWindowFromHandleCreationFailure_e (3 constants, from SwConst)."""
    swHandleWindowFromHandleCreationFailure_Cancel = 1
    swHandleWindowFromHandleCreationFailure_Retry = 2
    swHandleWindowFromHandleCreationFailure_Continue = 3

class swHealActionType_e(IntEnum):
    """swHealActionType_e (3 constants, from SwConst)."""
    swHealAction_Shrink = 0
    swHealAction_GrowParent = 1
    swHealAction_Cap = 2

class swHelixDefinedBy_e(IntEnum):
    """swHelixDefinedBy_e (4 constants, from SwConst)."""
    swHelixDefinedByPitchAndRevolution = 0
    swHelixDefinedByHeightAndRevolution = 1
    swHelixDefinedByHeightAndPitch = 2
    swHelixDefinedBySpiral = 3

class swHemPositionTypes_e(IntEnum):
    """swHemPositionTypes_e (2 constants, from SwConst)."""
    swHemPositionTypeInside = 0
    swHemPositionTypeOutside = 1

class swHemTypes_e(IntEnum):
    """swHemTypes_e (5 constants, from SwConst)."""
    swHemTypeOpen = 0
    swHemTypeClosed = 1
    swHemTypeTearDrop = 2
    swHemTypeRolled = 3
    swHemTypeDouble = 4

class swHingeMateEntityType_e(IntEnum):
    """swHingeMateEntityType_e (3 constants, from SwConst)."""
    swHingeMateEntityType_Concentric = 0
    swHingeMateEntityType_Coincident = 1
    swHingeMateEntityType_Angle = 2

class swHlrQuality_e(IntEnum):
    """swHlrQuality_e (2 constants, from SwConst)."""
    swPreciseHlr = 0
    swFastHlr = 1

class swHoleElementOrientation_e(IntEnum):
    """swHoleElementOrientation_e (2 constants, from SwConst)."""
    swHoleElementOrientation_Nearside = 0
    swHoleElementOrientation_Farside = 1

class swHoleSeriesWhichParts_e(IntEnum):
    """swHoleSeriesWhichParts_e (3 constants, from SwConst)."""
    swHoleSeriesFirstPart = 0
    swHoleSeriesMiddleParts = 1
    swHoleSeriesLastPart = 2

class swHoleTableTagOrder_e(IntEnum):
    """swHoleTableTagOrder_e (3 constants, from SwConst)."""
    swHoleTableTagOrder_XY = 1
    swHoleTableTagOrder_ReduceToolPath = 2
    swHoleTableTagOrder_Radial = 3

class swHoleTableTagPrefixApply_e(IntEnum):
    """swHoleTableTagPrefixApply_e (2 constants, from SwConst)."""
    swHoleTableTagPrefixApply_AllHolesOfSameSize = 1
    swHoleTableTagPrefixOption_OnlySpecifiedHole = 2

class swHoleTableTagStyle_e(IntEnum):
    """swHoleTableTagStyle_e (3 constants, from SwConst)."""
    swHoleTable_AlphaNumericTags = 1
    swHoleTable_NumericTags = 2
    swHoleTable_ManualTags = 3

class swHorizontalAutoSplitApply_e(IntEnum):
    """swHorizontalAutoSplitApply_e (2 constants, from SwConst)."""
    swHorizontalAutoSplitApply_ThisTimeOnly = 0
    swHorizontalAutoSplitApply_Continuousely = 1

class swHorizontalAutoSplitPlacementOfSplitTable_e(IntEnum):
    """swHorizontalAutoSplitPlacementOfSplitTable_e (2 constants, from SwConst)."""
    swHorizontalAutoSplitPlacementOfSplitTable_NextToLastSplit = 0
    swHorizontalAutoSplitPlacementOfSplitTable_BelowLastSplit = 1

class swIFCExportSaveType_e(IntEnum):
    """swIFCExportSaveType_e (3 constants, from SwConst)."""
    swIFCExportSaveType_BREP = 0
    swIFCExportSaveType_BREPAndTessellation = 1
    swIFCExportSaveType_Tessellation = 2

class swIFCOmniUniClassPreference_e(IntEnum):
    """swIFCOmniUniClassPreference_e (2 constants, from SwConst)."""
    swIFCSaveAsOmniClass = 0
    swIFCSaveAsUniClass2 = 1

class swIGESCurveRepresentation_e(IntEnum):
    """swIGESCurveRepresentation_e (2 constants, from SwConst)."""
    swIGES_CURVES_BSPLINE = 0
    swIGES_CURVES_PSPLINE = 1

class swIGESPreferredSystem_e(IntEnum):
    """swIGESPreferredSystem_e (11 constants, from SwConst)."""
    swIGES_STANDARD = 0
    swIGES_NURBS = 1
    swIGES_ANSYS = 2
    swIGES_COSMOS = 3
    swIGES_MASCAM = 4
    swIGES_SURFCAM = 5
    swIGES_SMARTCAM = 6
    swIGES_TEKSOFT = 7
    swIGES_ALPHACAM = 8
    swIGES_MULTICAM = 9
    swIGES_ALIAS = 10

class swIGESRepresentation_e(IntEnum):
    """swIGESRepresentation_e (5 constants, from SwConst)."""
    swIGES_TRMSRF = 0
    swIGES_CURVES = 1
    swIGES_TRMSRFANDCURVES = 2
    swIGES_BREP = 3
    swIGES_BOUNDEDSRF = 4

class swImageQualityShaded_e(IntEnum):
    """swImageQualityShaded_e (3 constants, from SwConst)."""
    swShadedImageQualityCoarse = 1
    swShadedImageQualityFine = 2
    swShadedImageQualityCustom = 3

class swImageQualityWireframe_e(IntEnum):
    """swImageQualityWireframe_e (2 constants, from SwConst)."""
    swWireframeImageQualityOptimal = 1
    swWireframeImageQualityCustom = 2

class swImageSizeToUse_e(IntEnum):
    """swImageSizeToUse_e (6 constants, from SwConst)."""
    swImageSizeToUse_20x20 = 20
    swImageSizeToUse_32x32 = 32
    swImageSizeToUse_40x40 = 40
    swImageSizeToUse_64x64 = 64
    swImageSizeToUse_96x96 = 96
    swImageSizeToUse_128x128 = 128

class swImportDxfDwg_ImportMethod_e(IntEnum):
    """swImportDxfDwg_ImportMethod_e (5 constants, from SwConst)."""
    swImportDxfDwg_DoNotImportSheet = 0
    swImportDxfDwg_ImportToDrawing = 1
    swImportDxfDwg_ImportToPartSketch = 2
    swImportDxfDwg_ImportToExistingDrawing = 3
    swImportDxfDwg_ImportToExistingPart = 4

class swImportDxfDwg_LayerVisibility_e(IntEnum):
    """swImportDxfDwg_LayerVisibility_e (3 constants, from SwConst)."""
    swImportDxfDwg_LayerMaintain = 0
    swImportDxfDwg_LayerVisible = 1
    swImportDxfDwg_LayerHidden = 2

class swImportModelItemsSource_e(IntEnum):
    """swImportModelItemsSource_e (4 constants, from SwConst)."""
    swImportModelItemsFromEntireModel = 0
    swImportModelItemsFromSelectedFeature = 1
    swImportModelItemsFromSelectedComponent = 2
    swImportModelItemsFromAssemblyOnly = 3

class swImportNeutralAssemblyStructureMapping_e(IntEnum):
    """swImportNeutralAssemblyStructureMapping_e (3 constants, from SwConst)."""
    swImportNeutralAssemblyStructureMapping_Default = 0
    swImportNeutralAssemblyStructureMapping_MultipleParts = 1
    swImportNeutralAssemblyStructureMapping_MultibodyPart = 2

class swImportNeutralCurvesAndPointsOptions_e(IntEnum):
    """swImportNeutralCurvesAndPointsOptions_e (2 constants, from SwConst)."""
    swImportNeutralCurvesAndPointsOptions_AsSketches = 0
    swImportNeutralCurvesAndPointsOptions_As3DCurves = 1

class swImportNeutralKnitOption_e(IntEnum):
    """swImportNeutralKnitOption_e (2 constants, from SwConst)."""
    swImportNeutralKnitOption_FormSolids = 0
    swImportNeutralKnitOption_DoNotKnit = 1

class swImportNeutralUnits_e(IntEnum):
    """swImportNeutralUnits_e (2 constants, from SwConst)."""
    swImportNeutralUnits_ImportFileUnits = 0
    swImportNeutralUnits_TemplateUnits = 1

class swImportPartCustomPropertiesToOptions_e(IntEnum):
    """swImportPartCustomPropertiesToOptions_e (3 constants, from SwConst)."""
    swImportPropertiesToFileProperties = 1
    swImportPropertiesToCutlistProperties = 2
    swImportPartCustomPropertiesNone = 3

class swImportSheetMetalInformation_e(IntEnum):
    """swImportSheetMetalInformation_e (3 constants, from SwConst)."""
    swImportWithUnlockedProperties = 1
    swImportWithoutUnlockedProperties = 2
    swImportUnlockedPropertiesNone = 3

class swImportStlVrmlModelType_e(IntEnum):
    """swImportStlVrmlModelType_e (3 constants, from SwConst)."""
    swImportStlVrmlModelType_Graphics = 0
    swImportStlVrmlModelType_Surface = 1
    swImportStlVrmlModelType_Solid = 2

class swImprintingFacesOpts_e(IntEnum):
    """swImprintingFacesOpts_e (3 constants, from SwConst)."""
    swImprintingFacesOnTool = 1
    swImprintingFacesOnOverlapping = 2
    swImprintingFacesOnExtendFace = 4

class swInConfigurationOpts_e(IntEnum):
    """swInConfigurationOpts_e (6 constants, from SwConst)."""
    swConfigPropertySuppressFeatures = 0
    swThisConfiguration = 1
    swAllConfiguration = 2
    swSpecifyConfiguration = 3
    swLinkedToParent = 4
    swSpeedpakConfiguration = 5

class swInContextEditTransparencyType_e(IntEnum):
    """swInContextEditTransparencyType_e (3 constants, from SwConst)."""
    swInContextEditTransparencyOpaque = 0
    swInContextEditTransparencyForce = 1
    swInContextEditTransparencyMaintain = 2

class swIndentSelectionState_e(IntEnum):
    """swIndentSelectionState_e (2 constants, from SwConst)."""
    swIndentSelectionStateKeepSelection = 0
    swIndentSelectionStateRemoveSelection = 1

class swInsertAnnotation_e(IntEnum):
    """swInsertAnnotation_e (26 constants, from SwConst)."""
    swInsertCThreads = 1
    swInsertDatums = 2
    swInsertDatumTargets = 4
    swInsertDimensions = 8
    swInsertInstanceCounts = 16
    swInsertGTols = 32
    swInsertNotes = 64
    swInsertSFSymbols = 128
    swInsertWelds = 256
    swInsertAxes = 512
    swInsertCurves = 1024
    swInsertPlanes = 2048
    swInsertSurfaces = 4096
    swInsertPoints = 8192
    swInsertOrigins = 16384
    swInsertDimensionsMarkedForDrawing = 32768
    swInsertHoleWizardProfileDimensions = 65536
    swInsertHoleWizardLocationDimensions = 131072
    swInsertRefPoints = 262144
    swInsertDimensionsNotMarkedForDrawing = 524288
    swInsertholeCallout = 1048576
    swInsertWeldBeads = 2097152
    swInsertSketches = 4194304
    swInsertWeldBeads_ET = 8388608
    swInsertTolerancedDims = 16777216
    swInsertCenterOfMass = 33554432

class swInsertAssyOptions_e(IntEnum):
    """swInsertAssyOptions_e (12 constants, from SwConst)."""
    swInsertAssySurfaceBodies = 1
    swInsertAssyMaterials = 2
    swInsertAssyRefPlanes = 4
    swInsertAssyRefAxes = 8
    swInsertAssyCoordinateSystems = 16
    swInsertAssyCosmeticThreads = 32
    swInsertAssyVisualProperties = 64
    swInsertAssySketches = 128
    swInsertAssyCustomProperties = 256
    swInsertAssyHoleWizardData = 512
    swInsertAssyGraphicsBodies = 1024
    swInsertAssyPartCutListProps = 2048

class swInsertEdgeFlangeOptions_e(IntEnum):
    """swInsertEdgeFlangeOptions_e (8 constants, from SwConst)."""
    swInsertEdgeFlangeUseDefaultRadius = 1
    swInsertEdgeFlangeFlipDir = 2
    swInsertEdgeFlangeDoOffset = 4
    swInsertEdgeFlangeReverseOffsetDir = 8
    swInsertEdgeFlangeTearClip = 16
    swInsertEdgeFlangeTrimSideBend = 32
    swInsertEdgeFlangeUseReliefRatio = 64
    swInsertEdgeFlangeUseDefaultRelief = 128

class swInsertNewAssemblyErrorCode_e(IntEnum):
    """swInsertNewAssemblyErrorCode_e (6 constants, from SwConst)."""
    swInsertNewAssemblyError_ErrorUknown = 0
    swInsertNewAssemblyError_NoError = 1
    swInsertNewAssemblyError_FilePathEmpty = 2
    swInsertNewAssemblyError_FileAlreadyExists = 3
    swInsertNewAssemblyError_FolderDoesNotExist = 4
    swInsertNewAssemblyError_ExtensionNotSldAsm = 5

class swInsertNewPartErrorCode_e(IntEnum):
    """swInsertNewPartErrorCode_e (8 constants, from SwConst)."""
    swInsertNewPartError_ErrorUknown = 0
    swInsertNewPartError_NoError = 1
    swInsertNewPartError_FilePathEmpty = 2
    swInsertNewPartError_FileAlreadyExists = 3
    swInsertNewPartError_FolderDoesNotExist = 4
    swInsertNewPartError_ExtensionNotSldPrt = 5
    swInsertNewPartError_NotAFaceOrPlane = 6
    swInsertNewPartError_CannotSelectFaceOrPlane = 7

class swInsertOptions_e(IntEnum):
    """swInsertOptions_e (3 constants, from SwConst)."""
    swInsertOption_BeforeSelectedSheet = 0
    swInsertOption_AfterSelectedSheet = 1
    swInsertOption_MoveToEnd = 2

class swInsertPartOptions_e(IntEnum):
    """swInsertPartOptions_e (24 constants, from SwConst)."""
    swInsertPartImportSolids = 1
    swInsertPartImportSurfaces = 2
    swInsertPartImportAxes = 4
    swInsertPartImportPlanes = 8
    swInsertPartImportCosmeticThreads = 16
    swInsertPartImportAbsorbedSketchs = 32
    swInsertPartImportUnabsorbedSketchs = 64
    swInsertPartImportCustomProperties = 128
    swInsertPartImportCoordinateSystem = 256
    swInsertPartBreakLink = 512
    swInsertPartImportModelDimensions = 1024
    swInsertPartImportCutListProperties = 2048
    swInsertPartImportHoleWzdData = 4096
    swInsertPartImportSMInfo = 8192
    swInsertPartImportIndProps = 16384
    swInsertPartImportCustomToFileProperties = 32768
    swInsertPartImportCustomToCutlistProperties = 65536
    swInsertPartImportDimXpertAnnotations = 131072
    swInsertPartDontZoomAll = 262144
    swInsertPartImportMaterial = 524288
    swInsertPartImportPropagateVisualPropertiesFromOriginalPart = 1048576
    swInsertPartImportPoints = 2097152
    swInsertPartImportPartMaterial = 4194304
    swInsertPartImportGraphicBodies = 8388608

class swInsertSlicingError_e(IntEnum):
    """swInsertSlicingError_e (9 constants, from SwConst)."""
    swInsertSlicingError_NoError = 0
    swInsertSlicingError_GenericError = 1
    swInsertSlicingError_InvalidTotalAngle = 2
    swInsertSlicingError_InvalidSlicesToGenerateOption = 4
    swInsertSlicingError_InvalidSlicingPlaneEntities = 8
    swInsertSlicingError_EntitiesCannotFormPlane = 16
    swInsertSlicingError_NoBodiesInsideBox = 32
    swInsertSlicingError_InvalidSlicingData = 64
    swInsertSlicingError_InvalidNumberOfPlanes = 128

class swInsertTableColumnWidthStyle_e(IntEnum):
    """swInsertTableColumnWidthStyle_e (3 constants, from SwConst)."""
    swInsertColumn_DefaultWidth = 0
    swInsertColumn_SingleLineTight = 1
    swInsertColumn_MultilineTight = 2

class swInstanceToVaryModificationType_e(IntEnum):
    """swInstanceToVaryModificationType_e (3 constants, from SwConst)."""
    swInstanceToVaryModificationType_D1Spacing = 1
    swInstanceToVaryModificationType_D2Spacing = 2
    swInstanceToVaryModificationType_Dimensions = 3

class swInterfaceBrightnessColor_e(IntEnum):
    """swInterfaceBrightnessColor_e (9 constants, from SwConst)."""
    swIBColor_FeatureMgrBkgnd = 0
    swIBColor_EnabledTextColor = 1
    swIBColor_DisabledTextColor = 2
    swIBColor_ActiveTabColor = 3
    swIBColor_InactiveTabColor = 4
    swIBColor_ButtonFillHotColor = 5
    swIBColor_ButtonFillCheckedColor = 6
    swIBColor_ButtonFillPressedColor = 7
    swIBColor_ButtonFillCheckedAndHotColor = 8

class swInterfaceBrightnessTheme_e(IntEnum):
    """swInterfaceBrightnessTheme_e (5 constants, from SwConst)."""
    swInterfaceBrightnessTheme_Light = 0
    swInterfaceBrightnessTheme_Medium = 1
    swInterfaceBrightnessTheme_Dark = 2
    swInterfaceBrightnessTheme_MediumLight = 3
    swInterfaceBrightnessTheme_3DExperience = 4

class swInterpolationType_e(IntEnum):
    """swInterpolationType_e (3 constants, from SwConst)."""
    swInvalidInterpolation = 0
    swCubicInterpolation = 1
    swAkimaInterpolation = 2

class swIntersectionType_e(IntEnum):
    """swIntersectionType_e (4 constants, from SwConst)."""
    swIntersectionSIMPLE = 1
    swIntersectionTANGENT = 2
    swIntersectionCOINCIDENCE_START = 3
    swIntersectionCOINCIDENCE_END = 4

class swIsolateVisibility_e(IntEnum):
    """swIsolateVisibility_e (3 constants, from SwConst)."""
    swIsolateVisibility_WIREFRAME = 0
    swIsolateVisibility_TRANSPARENT = 1
    swIsolateVisibility_HIDDEN = 2

class swJogDimensionPositionType_e(IntEnum):
    """swJogDimensionPositionType_e (3 constants, from SwConst)."""
    swJogDimensionPositionInsideOffset = 1
    swJogDimensionPositionOutsideOffset = 2
    swJogDimensionPositionOverallPosition = 3

class swJogOffsetTypes_e(IntEnum):
    """swJogOffsetTypes_e (5 constants, from SwConst)."""
    swJogOffsetBlind = 1
    swJogOffsetUpToVertex = 2
    swJogOffsetUpToSurface = 3
    swJogOffsetFromSurface = 4
    swJogOffsetMidPlane = 5

class swJogPositionType_e(IntEnum):
    """swJogPositionType_e (4 constants, from SwConst)."""
    swJogPositionBendCenterline = 1
    swJogPositionMaterialInside = 2
    swJogPositionMaterialOutside = 3
    swJogPositionBendOutside = 4

class swKeepReplacedCompOption_e(IntEnum):
    """swKeepReplacedCompOption_e (4 constants, from SwConst)."""
    swKeepBothNewItemNumber = 0
    swKeepBothSameItemNumber = 1
    swKeepItemNumber = 2
    swKeepNewItemNumberRemoveReplacedComp = 3

class swKernelErrorCode_e(IntEnum):
    """swKernelErrorCode_e (34 constants, from SwConst)."""
    swErrorSuccess = 1
    swErrorError = 0
    swErrorNotEntity = -100022
    swErrorInvalidParameter = -100120
    swErrorSurfaceDiscontinuous = -100129
    swErrorCurveDiscontinuous = -100131
    swErrorInvalidEntity = -100914
    swErrorInvalidSharing = -100921
    swErrorInvalidKnots = -100978
    swErrorInvalidGeometry = -100999
    swErrorHasInvalidentity = -101004
    swErrorBodyDontKnit = -101041
    swErrorInvalidPattern = -101042
    swErrorCurveShort = -101057
    swErrorFailed = -101063
    swErrorCheckFailed = -105061
    swErrorGeometryMissing = -113803
    swErrorTopologySelfx = -113804
    swErrorGeometrySelfx = -113805
    swErrorGeometryDegenerate = -113806
    swErrorInvalidGeometry2 = -113808
    swErrorCheckFailed2 = -113812
    swErrorFaceFaceInconsistent = -113816
    swErrorVertexNotOnCurve = -113818
    swErrorVerticesTouch = -113821
    swErrorLoopsInconsistent = -113826
    swErrorGeometryDiscontinuous = -113827
    swErrorFacecheckFailed = -113829
    swErrorFaceRedundant = -116402
    swErrorInconsistentDirs = -116403
    swErrorEdgeisectInvalid = -116404
    swErrorInvalidLoop = -116405
    swErrorEdgeIncorrectOrder = -116406
    swErrorUnknown = -1

class swLargeDesignReviewState_e(IntEnum):
    """swLargeDesignReviewState_e (3 constants, from SwConst)."""
    swLargeDesignReviewState_None = 0
    swLargeDesignReviewState_LDR = 1
    swLargeDesignReviewState_LDR_EditAssembly = 2

class swLayerItemsOption_e(IntEnum):
    """swLayerItemsOption_e (5 constants, from SwConst)."""
    swLayerItemsOption_Annotations = 1
    swLayerItemsOption_SketchSegments = 2
    swLayerItemsOption_SketchBlockInstance = 4
    swLayerItemsOption_SketchPoint = 8
    swLayerItemsOption_SketchHatch = 16

class swLayerOverride_e(IntEnum):
    """swLayerOverride_e (4 constants, from SwConst)."""
    swLayerOverrideNone = 0
    swLayerOverrideColor = 1
    swLayerOverrideStyle = 2
    swLayerOverrideWidth = 4

class swLeaderLineVisibility_e(IntEnum):
    """swLeaderLineVisibility_e (4 constants, from SwConst)."""
    swLeaderLineBoth = 0
    swLeaderLineFirst = 1
    swLeaderLineSecond = 2
    swLeaderLineNone = 3

class swLeaderSide_e(IntEnum):
    """swLeaderSide_e (3 constants, from SwConst)."""
    swLS_SMART = 0
    swLS_LEFT = 1
    swLS_RIGHT = 2

class swLeaderStyle_e(IntEnum):
    """swLeaderStyle_e (11 constants, from SwConst)."""
    swNO_LEADER = 0
    swSTRAIGHT = 1
    swBENT = 2
    swUNDERLINED = 3
    swAlwaysAttachToBalloon = 4100
    swSPLINE = 4
    swAttachLeaderTop = 256
    swAttachLeaderCenter = 512
    swAttachLeaderBottom = 1024
    swAttachLeaderNearest = 2048
    swVDA = 8

class swLengthUnit_e(IntEnum):
    """swLengthUnit_e (11 constants, from SwConst)."""
    swMM = 0
    swCM = 1
    swMETER = 2
    swINCHES = 3
    swFEET = 4
    swFEETINCHES = 5
    swANGSTROM = 6
    swNANOMETER = 7
    swMICRON = 8
    swMIL = 9
    swUIN = 10

class swLibFeatDimensionType_e(IntEnum):
    """swLibFeatDimensionType_e (2 constants, from SwConst)."""
    swLibFeatLocatingDimension = 0
    swLibFeatSizeDimension = 1

class swLibFeatureData_e(IntEnum):
    """swLibFeatureData_e (2 constants, from SwConst)."""
    swLibFeatureData_FeatureRespect = 0
    swLibFeatureData_PartRespect = 1

class swLicenseType_e(IntEnum):
    """swLicenseType_e (10 constants, from SwConst)."""
    swLicenseType_Full = 0
    swLicenseType_Educational = 1
    swLicenseType_Student = 2
    swLicenseType_StudentDesignKit = 3
    swLicenseType_PersonalEdition = 4
    swLicenseType_Full_Office = 5
    swLicenseType_Full_Professional = 6
    swLicenseType_Full_Premium = 7
    swLicenseType_Maker = 8
    swLicenseType_Full_Ultimate = 9

class swLineEndCaps_e(IntEnum):
    """swLineEndCaps_e (3 constants, from SwConst)."""
    swLineEndCapFlat = 1
    swLineEndCapRound = 2
    swLineEndCapSquare = 3

class swLineStyles_e(IntEnum):
    """swLineStyles_e (8 constants, from SwConst)."""
    swLineCONTINUOUS = 0
    swLineHIDDEN = 1
    swLinePHANTOM = 2
    swLineCHAIN = 3
    swLineCENTER = 4
    swLineSTITCH = 5
    swLineCHAINTHICK = 6
    swLineDEFAULT = 7

class swLineTypes_e(IntEnum):
    """swLineTypes_e (9 constants, from SwConst)."""
    swLF_VISIBLE = 0
    swLF_HIDDEN = 1
    swLF_SKETCH = 2
    swLF_DETAIL = 3
    swLF_SECTION = 4
    swLF_DIMENSION = 5
    swLF_CENTER = 6
    swLF_HATCH = 7
    swLF_TANGENT = 8

class swLineWeights_e(IntEnum):
    """swLineWeights_e (12 constants, from SwConst)."""
    swLW_NONE = -1
    swLW_THIN = 0
    swLW_NORMAL = 1
    swLW_THICK = 2
    swLW_THICK2 = 3
    swLW_THICK3 = 4
    swLW_THICK4 = 5
    swLW_THICK5 = 6
    swLW_THICK6 = 7
    swLW_NUMBER = 8
    swLW_LAYER = 9
    swLW_CUSTOM = 10

class swLinkBomToDisplayStateError_e(IntEnum):
    """swLinkBomToDisplayStateError_e (3 constants, from SwConst)."""
    swLinkBomToDisplayState_Success = 0
    swLinkBomToDisplayState_InvalidDisplayState = 1
    swLinkBomToDisplayState_MultipleConfigurations = 2

class swLinkDimensionError_e(IntEnum):
    """swLinkDimensionError_e (13 constants, from SwConst)."""
    swLinkDimensionError_ErrorUknown = 0
    swLinkDimensionError_NoError = 1
    swLinkDimensionError_LinkAcrossDocs = 2
    swLinkDimensionError_IncompatibleDimTypes = 3
    swLinkDimensionError_AlreadyLinked = 4
    swLinkDimensionError_ReadOnlyOrDriven = 5
    swLinkDimensionError_IncompatibleValues = 6
    swLinkDimensionError_DrivenByEquation = 7
    swLinkDimensionError_CannotLink = 8
    swLinkDimensionError_UnableToCreateSharedParam = 9
    swLinkDimensionError_UnlinkFailure = 10
    swLinkDimensionError_EmptyString = 11
    swLinkDimensionError_InvalidString = 12

class swLinkString(IntEnum):
    """swLinkString (3 constants, from SwConst)."""
    swLinkStringNone = 0
    swLinkStringUserDefined = 1
    swLinkStringTroubleShootTip = 2

class swLoadAddinError_e(IntEnum):
    """swLoadAddinError_e (9 constants, from SwConst)."""
    swUnknownError = -1
    swSuccess = 0
    swAddinNotLoaded = 1
    swAddinAlreadyLoaded = 2
    swFileNotFound = 3
    swAddinsDisabled = 4
    swLoadConflict = 5
    swRegistrationError = 6
    swLicenseError = 7

class swLoadDetachedModelRules_e(IntEnum):
    """swLoadDetachedModelRules_e (4 constants, from SwConst)."""
    swLoadDetachedModelPrompt = 0
    swLoadDetachedModelAuto = 1
    swDoNotLoadDetachedModel = 2
    swLoadDetailedModel = 3

class swLoadExternalReferences_e(IntEnum):
    """swLoadExternalReferences_e (4 constants, from SwConst)."""
    swLoadExternalReferences_Prompt = 0
    swLoadExternalReferences_All = 1
    swLoadExternalReferences_None = 2
    swLoadExternalReferences_ChangedOnly = 3

class swLocalCurvePatternAlignment_e(IntEnum):
    """swLocalCurvePatternAlignment_e (2 constants, from SwConst)."""
    swLocalCurvePatternTangentToCurve = 0
    swLocalCurvePatternAlignToSeed = 1

class swLocalCurvePatternCurveMethod_e(IntEnum):
    """swLocalCurvePatternCurveMethod_e (2 constants, from SwConst)."""
    swLocalCurvePatternTransformCurve = 0
    swLocalCurvePatternOffsetCurve = 1

class swLocalCurvePatternReferencePoint_e(IntEnum):
    """swLocalCurvePatternReferencePoint_e (3 constants, from SwConst)."""
    swLocalCurvePatternSelectedPoint = 0
    swLocalCurvePatternBoundingBoxCenter = 1
    swLocalCurvePatternComponentOrigin = 2

class swLocalSketchPatternReferencePoint_e(IntEnum):
    """swLocalSketchPatternReferencePoint_e (3 constants, from SwConst)."""
    swLocalSketchPatternSelectedPoint = 0
    swLocalSketchPatternBoundingBoxCenter = 1
    swLocalSketchPatternComponentOrigin = 2

class swLocationLabelText_e(IntEnum):
    """swLocationLabelText_e (5 constants, from SwConst)."""
    swLocationLabelTextSheet = 0
    swLocationLabelTextSheetWithLabel = 1
    swLocationLabelTextZone = 2
    swLocationLabelTextViewLetter = 3
    swLocationLabelTextText = 4

class swLoftedBendFacetOptions_e(IntEnum):
    """swLoftedBendFacetOptions_e (4 constants, from SwConst)."""
    swChordTolerance = 0
    swBendsPerTransitionSegment = 1
    swMaxSegmentLength = 2
    swAngleBetweenSegments = 3

class swLoopProcessOption_e(IntEnum):
    """swLoopProcessOption_e (3 constants, from SwConst)."""
    swLoopProcess_Together = 0
    swLoopProcess_Independent = 1
    swLoopProcess_Auto = 2

class swMBDSTEP242PublishEdition_e(IntEnum):
    """swMBDSTEP242PublishEdition_e (3 constants, from SwConst)."""
    swPublishSTEP242Edition_1_0 = 1
    swPublishSTEP242Edition_2_0 = 2
    swPublishSTEP242Edition_3_0 = 3

class swMacroFeatureEntityIdType_e(IntEnum):
    """swMacroFeatureEntityIdType_e (5 constants, from SwConst)."""
    swMacroFeatureEntityIdNotApplied = -1
    swMacroFeatureEntityIdUndefined = 0
    swMacroFeatureEntityIdUnique = 1
    swMacroFeatureEntityIdDerived = 2
    swMacroFeatureEntityIdUserDefined = 3

class swMacroFeatureOptions_e(IntEnum):
    """swMacroFeatureOptions_e (6 constants, from SwConst)."""
    swMacroFeatureByDefault = 0
    swMacroFeatureAlwaysAtEnd = 1
    swMacroFeatureIsPatternable = 2
    swMacroFeatureIsDragable = 4
    swMacroFeatureNoCachedBody = 8
    swMacroFeatureEmbedMacroFile = 16

class swMacroFeatureParamType_e(IntEnum):
    """swMacroFeatureParamType_e (3 constants, from SwConst)."""
    swMacroFeatureParamTypeString = 0
    swMacroFeatureParamTypeDouble = 1
    swMacroFeatureParamTypeInteger = 2

class swMacroFeatureSecurityOptions_e(IntEnum):
    """swMacroFeatureSecurityOptions_e (7 constants, from SwConst)."""
    swMacroFeatureSecurityByDefault = 0
    swMacroFeatureSecurityCannotBeDeleted = 1
    swMacroFeatureSecurityNotEditable = 2
    swMacroFeatureSecurityCannotBeSuppressed = 4
    swMacroFeatureSecurityCannotBeReplaced = 8
    swMacroFeatureSecurityEnableNote = 16
    swMacroFeatureSecurityCannotBeRolledBack = 32

class swMacroMethods_e(IntEnum):
    """swMacroMethods_e (3 constants, from SwConst)."""
    swMethodsWithoutArguments = 1
    swMethodsWithArguments = 2
    swAllMethods = 3

class swManipulatorCursor_e(IntEnum):
    """swManipulatorCursor_e (3 constants, from SwConst)."""
    swManipulatorMoveCursor = 1
    swManipulatorRotateCursor = 2
    swManipulatorMoveRotateCursor = 3

class swManipulatorOptions_e(IntEnum):
    """swManipulatorOptions_e (2 constants, from SwConst)."""
    swManipulatorOpts_Default = 0
    swManipulatorOpts_KeepAfterComponentModify = 1

class swManipulatorRepresentation_e(IntEnum):
    """swManipulatorRepresentation_e (16 constants, from SwConst)."""
    swManipulatorRepresentationNone = 0
    swManipulatorRepresentationSquare = 1
    swManipulatorRepresentationCircle = 2
    swManipulatorRepresentationDiamond = 3
    swManipulatorRepresentationTriangle = 4
    swManipulatorRepresentationArrow = 5
    swManipulatorRepresentationTextBox = 6
    swManipulatorRepresentationRotationHandle = 7
    swManipulatorRepresentationPanHandle = 8
    swManipulatorRepresentationScaleHandle = 9
    swManipulatorRepresentationSurfTopol = 10
    swManipulatorRepresentationWireTopol = 11
    swManipulatorRepresentationMiscTopol = 12
    swManipulatorRepresentationBitmap = 13
    swManipulatorRepresentationShadow = 14
    swManipulatorRepresentationEmpty = 15

class swManipulatorType_e(IntEnum):
    """swManipulatorType_e (3 constants, from SwConst)."""
    swTriadManipulator = 0
    swDragArrowManipulator = 1
    swPlaneManipulator = 2

class swMassPropertiesStatus_e(IntEnum):
    """swMassPropertiesStatus_e (3 constants, from SwConst)."""
    swMassPropertiesStatus_OK = 0
    swMassPropertiesStatus_UnknownError = 1
    swMassPropertiesStatus_NoBody = 2

class swMassPropertyAccuracyLevel_e(IntEnum):
    """swMassPropertyAccuracyLevel_e (3 constants, from SwConst)."""
    swMassPropertyAccuracyLevel_Lower = 0
    swMassPropertyAccuracyLevel_Medium = 1
    swMassPropertyAccuracyLevel_Higher = 2

class swMassPropertyMoment_e(IntEnum):
    """swMassPropertyMoment_e (2 constants, from SwConst)."""
    swMassPropertyMomentAboutCenterOfMass = 0
    swMassPropertyMomentAboutCoordSys = 1

class swMateAlign_e(IntEnum):
    """swMateAlign_e (6 constants, from SwConst)."""
    swMateAlignALIGNED = 0
    swMateAlignANTI_ALIGNED = 1
    swMateAlignCLOSEST = 2
    swAlignNONE = 0
    swAlignSAME = 1
    swAlignAGAINST = 2

class swMateEntity2ReferenceType_e(IntEnum):
    """swMateEntity2ReferenceType_e (14 constants, from SwConst)."""
    swMateEntity2ReferenceType_Point = 0
    swMateEntity2ReferenceType_Line = 1
    swMateEntity2ReferenceType_Circle = 2
    swMateEntity2ReferenceType_Plane = 3
    swMateEntity2ReferenceType_Cylinder = 4
    swMateEntity2ReferenceType_Sphere = 5
    swMateEntity2ReferenceType_Set = 6
    swMateEntity2ReferenceType_Cone = 7
    swMateEntity2ReferenceType_SweptSurface = 8
    swMateEntity2ReferenceType_MultipleSurface = 9
    swMateEntity2ReferenceType_GenSurface = 10
    swMateEntity2ReferenceType_Ellipse = 11
    swMateEntity2ReferenceType_GeneralCurve = 12
    swMateEntity2ReferenceType_UNKNOWN = 13

class swMateEntityTypes_e(IntEnum):
    """swMateEntityTypes_e (8 constants, from SwConst)."""
    swMateUnsupported = 0
    swMatePoint = 1
    swMateLine = 2
    swMatePlane = 3
    swMateCylinder = 4
    swMateCone = 5
    swMateSphere = 6
    swMateCircle = 7

class swMateReferenceAlignment_e(IntEnum):
    """swMateReferenceAlignment_e (4 constants, from SwConst)."""
    swMateReferenceAlignment_Any = 0
    swMateReferenceAlignment_Aligned = 1
    swMateReferenceAlignment_AntiAligned = 2
    swMateReferenceAlignment_Closest = 3

class swMateReferenceIndex_e(IntEnum):
    """swMateReferenceIndex_e (3 constants, from SwConst)."""
    swMateReference_Primary = 0
    swMateReference_Secondary = 1
    swMateReference_Tertiary = 2

class swMateReferenceType_e(IntEnum):
    """swMateReferenceType_e (5 constants, from SwConst)."""
    swMateReferenceType_default = 0
    swMateReferenceType_Tangent = 1
    swMateReferenceType_Coincident = 2
    swMateReferenceType_Concentric = 3
    swMateReferenceType_Parallel = 4

class swMateType_e(IntEnum):
    """swMateType_e (26 constants, from SwConst)."""
    swMateCOINCIDENT = 0
    swMateCONCENTRIC = 1
    swMatePERPENDICULAR = 2
    swMatePARALLEL = 3
    swMateTANGENT = 4
    swMateDISTANCE = 5
    swMateANGLE = 6
    swMateUNKNOWN = 7
    swMateSYMMETRIC = 8
    swMateCAMFOLLOWER = 9
    swMateGEAR = 10
    swMateWIDTH = 11
    swMateLOCKTOSKETCH = 12
    swMateRACKPINION = 13
    swMateMAXMATES = 14
    swMatePATH = 15
    swMateLOCK = 16
    swMateSCREW = 17
    swMateLINEARCOUPLER = 18
    swMateUNIVERSALJOINT = 19
    swMateCOORDINATE = 20
    swMateSLOT = 21
    swMateHINGE = 22
    swMateSLIDER = 23
    swMatePROFILECENTER = 24
    swMateMAGNETIC = 25

class swMateWidthOptions_e(IntEnum):
    """swMateWidthOptions_e (4 constants, from SwConst)."""
    swMateWidth_Centered = 0
    swMateWidth_Free = 1
    swMateWidth_Dimension = 2
    swMateWidth_Percent = 3

class swMaterialModifier_e(IntEnum):
    """swMaterialModifier_e (6 constants, from SwConst)."""
    swMaterialModifier_None = 0
    swMaterialModifier_Unknown = 1
    swMaterialModifier_MaximumMaterialCondition = 2
    swMaterialModifier_LeastMaterialCondition = 3
    swMaterialModifier_RegardlessOfFeatureSize = 4
    swMaterialModifier_Translation = 5

class swMatesDefaultMisalignment_e(IntEnum):
    """swMatesDefaultMisalignment_e (3 constants, from SwConst)."""
    swMatesAlignFirstConcentricMate = 0
    swMatesAlignSecondConcentricMate = 1
    swMatesSymmetric = 2

class swMeasureArcCircleOption_e(IntEnum):
    """swMeasureArcCircleOption_e (12 constants, from SwConst)."""
    swMeasureArcCircle_CenterToCenter = 0
    swMeasureArcCircle_MinimumDistance = 1
    swMeasureArcCircle_MaximumDistance = 2
    swMeasureArcCircle_CustomCenterToCenter = 3
    swMeasureArcCircle_CustomMinimumToMinimum = 4
    swMeasureArcCircle_CustomMaximumToMaximum = 5
    swMeasureArcCircle_CustomCenterToMinimum = 6
    swMeasureArcCircle_CustomCenterToMaximum = 7
    swMeasureArcCircle_CustomMinimumToCenter = 8
    swMeasureArcCircle_CustomMaximumToCenter = 9
    swMeasureArcCircle_CustomMinimumToMaximum = 10
    swMeasureArcCircle_CustomMaximumToMinimum = 11

class swMeasureProjectOnOption_e(IntEnum):
    """swMeasureProjectOnOption_e (3 constants, from SwConst)."""
    swMeasureProjectOn_None = 0
    swMeasureProjectOn_Screen = 1
    swMeasureProjectOn_FaceOrPlane = 2

class swMenuIdentifiers_e(IntEnum):
    """swMenuIdentifiers_e (9 constants, from SwConst)."""
    swFileMenu = 0
    swEditMenu = 1
    swViewMenu = 2
    swInsertMenu = 3
    swToolsMenu = 4
    swWindowMenu = 5
    swHelpMenu = 6
    swDeveloperToolsMenu = 7
    swViewToolbarsMenu = 8

class swMenuItemType_e(IntEnum):
    """swMenuItemType_e (3 constants, from SwConst)."""
    swMenuItemType_Default = 0
    swMenuItemType_Break = 1
    swMenuItemType_Separator = 2

class swMessageBoxBtn_e(IntEnum):
    """swMessageBoxBtn_e (6 constants, from SwConst)."""
    swMbAbortRetryIgnore = 1
    swMbOk = 2
    swMbOkCancel = 3
    swMbRetryCancel = 4
    swMbYesNo = 5
    swMbYesNoCancel = 6

class swMessageBoxIcon_e(IntEnum):
    """swMessageBoxIcon_e (4 constants, from SwConst)."""
    swMbWarning = 1
    swMbInformation = 2
    swMbQuestion = 3
    swMbStop = 4

class swMessageBoxResult_e(IntEnum):
    """swMessageBoxResult_e (7 constants, from SwConst)."""
    swMbHitAbort = 1
    swMbHitIgnore = 2
    swMbHitNo = 3
    swMbHitOk = 4
    swMbHitRetry = 5
    swMbHitYes = 6
    swMbHitCancel = 7

class swMinimumBendRadiusChecks_e(IntEnum):
    """swMinimumBendRadiusChecks_e (3 constants, from SWRoutingLib)."""
    swMinimumBendRadiusChecks_None = 0
    swMinimumBendRadiusChecks_WiresOnly = 1
    swMinimumBendRadiusChecks_CablesAndWires = 2

class swMirrorComponentMirrorType_e(IntEnum):
    """swMirrorComponentMirrorType_e (3 constants, from SwConst)."""
    swMirrorType_CenterOfBoundingBox = 0
    swMirrorType_CenterOfMass = 1
    swMirrorType_ComponentOrigin = 2

class swMirrorComponentNameModifier_e(IntEnum):
    """swMirrorComponentNameModifier_e (3 constants, from SwConst)."""
    swMirrorComponentName_Prefix = 0
    swMirrorComponentName_Suffix = 1
    swMirrorComponentName_Custom = 2

class swMirrorComponentOrientation2_e(IntEnum):
    """swMirrorComponentOrientation2_e (4 constants, from SwConst)."""
    swOrientation_MirroredX_MirroredY = 0
    swOrientation_MirroredAndFlippedX_MirroredY = 1
    swOrientation_MirroredX_MirroredAndFlippedY = 2
    swOrientation_MirroredAndFlippedX_MirroredAndFlippedY = 3

class swMirrorComponentOrientation_e(IntEnum):
    """swMirrorComponentOrientation_e (4 constants, from SwConst)."""
    swMirrorComponentOrientation_RotatePlaneY = 0
    swMirrorComponentOrientation_None = 1
    swMirrorComponentOrientation_RotatePlaneXY = 2
    swMirrorComponentOrientation_RotatePlaneX = 3

class swMirrorPartOptions_e(IntEnum):
    """swMirrorPartOptions_e (17 constants, from SwConst)."""
    swMirrorPartOptions_ImportSolids = 1
    swMirrorPartOptions_ImportSurfaces = 2
    swMirrorPartOptions_ImportAxes = 4
    swMirrorPartOptions_ImportPlanes = 8
    swMirrorPartOptions_ImportCosmeticThreads = 16
    swMirrorPartOptions_ImportAbsorbedSketchs = 32
    swMirrorPartOptions_ImportUnabsorbedSketchs = 64
    swMirrorPartOptions_ImportCustomProperties = 128
    swMirrorPartOptions_ImportCoordinateSystem = 256
    swMirrorPartOptions_ImportModelDimensions = 512
    swMirrorPartOptions_ImportHoleWizardData = 1024
    swMirrorPartOptions_ImportCutListProperties = 2048
    swMirrorPartOptions_ImportSMInfo = 4096
    swMirrorPartOptions_ImportIndProps = 8192
    swMirrorPartOptions_ImportDimXpertAnnotations = 16384
    swMirrorPartOptions_ImportBodyMaterial = 32768
    swMirrorPartOptions_ImportPartMaterial = 65536

class swMirrorPlaneType_e(IntEnum):
    """swMirrorPlaneType_e (2 constants, from SwConst)."""
    swMirrorPlaneType_Face = 0
    swMirrorPlaneType_Plane = 1

class swMirrorProfileOrAlignmentAxis_e(IntEnum):
    """swMirrorProfileOrAlignmentAxis_e (2 constants, from SwConst)."""
    swMirrorProfileOrAlignmentAxis_Horizontal = 1
    swMirrorProfileOrAlignmentAxis_Vertical = 2

class swMirrorViewPositions_e(IntEnum):
    """swMirrorViewPositions_e (3 constants, from SwConst)."""
    swMirrorViewPosition_NotDefined = -1
    swMirrorViewPosition_Horizontal = 0
    swMirrorViewPosition_Vertical = 1

class swModelRebuildStatus_e(IntEnum):
    """swModelRebuildStatus_e (3 constants, from SwConst)."""
    swModelRebuildStatus_FullyRebuilt = 0
    swModelRebuildStatus_NonFrozenFeatureNeedsRebuild = 1
    swModelRebuildStatus_FrozenFeatureNeedsRebuild = 2

class swModelRouteType_e(IntEnum):
    """swModelRouteType_e (9 constants, from SwConst)."""
    swModelRouteType_Harness = 0
    swModelRouteType_Tube = 1
    swModelRouteType_FabricatedPipe = 2
    swModelRouteType_FormedPipe = 3
    swModelRouteType_Trunking = 4
    swModelRouteType_UnknownRouteType = 5
    swModelRouteType_Electrical = 6
    swModelRouteType_AnyRouteType = 7
    swModelRouteType_MixedRouteType = 8

class swModifyTableNotifyReason_e(IntEnum):
    """swModifyTableNotifyReason_e (18 constants, from SwConst)."""
    swModifyTableNotifyReason_ColumnInsertionLeft = 0
    swModifyTableNotifyReason_ColumnInsertionRight = 1
    swModifyTableNotifyReason_RowInsertionAbove = 2
    swModifyTableNotifyReason_RowInsertionBelow = 3
    swModifyTableNotifyReason_ColumnRellocation = 4
    swModifyTableNotifyReason_RowRellocation = 5
    swModifyTableNotifyReason_ColumnDeletion = 6
    swModifyTableNotifyReason_CellDataModify = 7
    swModifyTableNotifyReason_ColumnPropertyModify = 8
    swModifyTableNotifyReason_CellMerge = 9
    swModifyTableNotifyReason_CellUnMerge = 10
    swModifyTableNotifyReason_EditMultiProp = 11
    swModifyTableNotifyReason_CustomPropertyModify = 12
    swModifyTableNotifyReason_TableSplitVerticallyLeft = 13
    swModifyTableNotifyReason_TableSplitVerticallyRight = 14
    swModifyTableNotifyReason_TableSplitHorizontallyAbove = 15
    swModifyTableNotifyReason_TableSplitHorizontallyBelow = 16
    swModifyTableNotifyReason_TableMerge = 17

class swMomentsOfInertiaReferenceFrame_e(IntEnum):
    """swMomentsOfInertiaReferenceFrame_e (3 constants, from SwConst)."""
    swMomentsOfInertiaReferenceFrame_CenterOfMass = 0
    swMomentsOfInertiaReferenceFrame_DefaultCoordinateSystem = 1
    swMomentsOfInertiaReferenceFrame_UserCoordinateSystem = 2

class swMotionContactFrictionType_e(IntEnum):
    """swMotionContactFrictionType_e (3 constants, from SwConst)."""
    swMotionContactFrictionOff = 0
    swMotionContactFrictionFull = 1
    swMotionContactFrictionDynamic = 2

class swMotionIntegratorType_e(IntEnum):
    """swMotionIntegratorType_e (3 constants, from SwMotionStudy)."""
    swMotionIntegrator_GSTIFF = 1
    swMotionIntegrator_WSTIFF = 2
    swMotionIntegrator_SI2_GSTIFF = 3

class swMotionMat_e(IntEnum):
    """swMotionMat_e (9 constants, from SwConst)."""
    swMotionMatNone = 1000
    swMotionMatAcrylic = 1001
    swMotionMatAluminumDry = 1002
    swMotionMatAluminumGreasy = 1003
    swMotionMatNylon = 1004
    swMotionMatRubberDry = 1005
    swMotionMatRubberGreasy = 1006
    swMotionMatSteelDry = 1007
    swMotionMatSteelGreasy = 1008

class swMotionPlotAxisComponent_e(IntEnum):
    """swMotionPlotAxisComponent_e (17 constants, from SwConst)."""
    swMotionPlotAxisComponent_X = 0
    swMotionPlotAxisComponent_Y = 1
    swMotionPlotAxisComponent_Z = 2
    swMotionPlotAxisComponent_MAGNITUDE = 3
    swMotionPlotAxisComponent_RADIAL_MAGNITUDE = 4
    swMotionPlotAxisComponent_EULER_PSI = 5
    swMotionPlotAxisComponent_EULER_THETA = 6
    swMotionPlotAxisComponent_EULER_PHI = 7
    swMotionPlotAxisComponent_YAW = 8
    swMotionPlotAxisComponent_PITCH = 9
    swMotionPlotAxisComponent_ROLL = 10
    swMotionPlotAxisComponent_RODRIGUEZ_PARAM1 = 11
    swMotionPlotAxisComponent_RODRIGUEZ_PARAM2 = 12
    swMotionPlotAxisComponent_RODRIGUEZ_PARAM3 = 13
    swMotionPlotAxisComponent_BRYANT_ANGLE1 = 14
    swMotionPlotAxisComponent_BRYANT_ANGLE2 = 15
    swMotionPlotAxisComponent_BRYANT_ANGLE3 = 16

class swMotionPlotAxisType_e(IntEnum):
    """swMotionPlotAxisType_e (34 constants, from SwConst)."""
    swMotionPlotAxisType_XAXISTIME = 0
    swMotionPlotAxisType_XAXISFRAME = 1
    swMotionPlotAxisType_CM_POSITION = 2
    swMotionPlotAxisType_PRESSURE_ANGLE = 3
    swMotionPlotAxisType_CM_VELOCITY = 4
    swMotionPlotAxisType_CM_ACCELERATION = 5
    swMotionPlotAxisType_TRANS_DISP = 6
    swMotionPlotAxisType_TRANS_VELOCITY = 7
    swMotionPlotAxisType_TRANS_ACCELERATION = 8
    swMotionPlotAxisType_ANGULAR_DISP = 9
    swMotionPlotAxisType_ANGULAR_VELOCITY = 10
    swMotionPlotAxisType_ANGULAR_ACCEL = 11
    swMotionPlotAxisType_TRANS_MOMENTUM = 12
    swMotionPlotAxisType_ANGULAR_MOMENTUM = 13
    swMotionPlotAxisType_REACTION_FORCE = 14
    swMotionPlotAxisType_REACTION_TORQUE = 15
    swMotionPlotAxisType_PROJ_ANGLES = 16
    swMotionPlotAxisType_EULER_ANGLES = 17
    swMotionPlotAxisType_PITCH = 18
    swMotionPlotAxisType_BRYANT_ANGLE = 19
    swMotionPlotAxisType_RODRIQUEZ_PARAM = 20
    swMotionPlotAxisType_MOTION_APPLIED_FORCE = 21
    swMotionPlotAxisType_MOTION_APPLIED_TORQUE = 22
    swMotionPlotAxisType_FRICTION_FORCE = 23
    swMotionPlotAxisType_FRICTION_MOMENT = 24
    swMotionPlotAxisType_KINETIC_ENERGY = 25
    swMotionPlotAxisType_TRANS_KINETIC_ENERGY = 26
    swMotionPlotAxisType_ANGULAR_KINETIC_ENERGY = 27
    swMotionPlotAxisType_POTENTIAL_ENERGY_DELTA = 28
    swMotionPlotAxisType_POWER_CONSUMPTION = 29
    swMotionPlotAxisType_TRACE_PATH = 30
    swMotionPlotAxisType_CONTACT_FORCE = 31
    swMotionPlotAxisType_REFLECTED_MASS = 32
    swMotionPlotAxisType_REFLECTED_INERTIA = 33

class swMotionStudyNotify_e(IntEnum):
    """swMotionStudyNotify_e (9 constants, from SwMotionStudy)."""
    swMotionStudyMotorTimeStepChangeNotify = 1
    swMotionStudyForceTimeStepChangeNotify = 2
    swMotionStudyPartCollideNotify = 3
    swMotionStudyMotorOutputTimeStepChangeNotify = 4
    swMotionStudyStartCalculateNotify = 5
    swMotionStudyStopCalculateNotify = 6
    swMotionStudyForceOutputTimeStepChangeNotify = 7
    swMotionStudySpecialEventNotify = 8
    swMotionStudyOutputTimeStepChangeNotify = 9

class swMotionStudyType_e(IntEnum):
    """swMotionStudyType_e (5 constants, from SwMotionStudy)."""
    swMotionStudyTypeAssembly = 1
    swMotionStudyTypePhysicalSimulation = 2
    swMotionStudyTypeCosmosMotion = 4
    swMotionStudyTypeLegacyCosmosMotion = 8
    swMotionStudyTypeNewCosmosMotion = 16

class swMouseDragMode_e(IntEnum):
    """swMouseDragMode_e (11 constants, from SwConst)."""
    swTranslateAssemblyComponent = 1
    swRotateAssemblyComponentAboutCenter = 2
    swRotateAssemblyComponentAboutAxis = 3
    swAssemblySmartMates = 4
    swRotateView = 5
    swTranslateView = 6
    swZoomView = 7
    swZoomToAreaOfView = 8
    swInsertDimension = 9
    swRollView = 10
    swTurnView = 11

class swMouseNotify_e(IntEnum):
    """swMouseNotify_e (12 constants, from SwConst)."""
    swMouseNotify = 1
    swMouseMoveNotify = 2
    swMouseLBtnDownNotify = 3
    swMouseLBtnUpNotify = 4
    swMouseRBtnDownNotify = 5
    swMouseRBtnUpNotify = 6
    swMouseMBtnDownNotify = 7
    swMouseMBtnUpNotify = 8
    swMouseLBtnDblClkNotify = 9
    swMouseRBtnDblClkNotify = 10
    swMouseMBtnDblClkNotify = 11
    swMouseSelectNotify = 12

class swMouse_e(IntEnum):
    """swMouse_e (150 constants, from SwCommands)."""
    swMouse_MouseMove = 1
    swMouse_LeftDown = 2
    swMouse_LeftUp = 4
    swMouse_RightDown = 8
    swMouse_RightUp = 16
    swMouse_MiddleDown = 32
    swMouse_MiddleUp = 64
    swMouse_Wheel = 128
    swMouse_Absolute = 256
    swMouse_Click = 512
    swMouse_DoubleClick = 1024
    swMouse_RightClick = 2048
    swMouse_RightDoubleClick = 4096
    swMouse_MiddleDoubleClick = 8192
    swMouse_SelectEDGES = 65536
    swMouse_SelectFACES = 131072
    swMouse_SelectVERTICES = 196608
    swMouse_SelectDATUMPLANES = 262144
    swMouse_SelectDATUMAXES = 327680
    swMouse_SelectDATUMPOINTS = 393216
    swMouse_SelectOLEITEMS = 458752
    swMouse_SelectATTRIBUTES = 524288
    swMouse_SelectSKETCHES = 589824
    swMouse_SelectSKETCHSEGS = 655360
    swMouse_SelectSKETCHPOINTS = 720896
    swMouse_SelectDRAWINGVIEWS = 786432
    swMouse_SelectGTOLS = 851968
    swMouse_SelectDIMENSIONS = 917504
    swMouse_SelectNOTES = 983040
    swMouse_SelectSECTIONLINES = 1048576
    swMouse_SelectDETAILCIRCLES = 1114112
    swMouse_SelectSECTIONTEXT = 1179648
    swMouse_SelectSHEETS = 1245184
    swMouse_SelectCOMPONENTS = 1310720
    swMouse_SelectMATES = 1376256
    swMouse_SelectBODYFEATURES = 1441792
    swMouse_SelectREFCURVES = 1507328
    swMouse_SelectEXTSKETCHSEGS = 1572864
    swMouse_SelectEXTSKETCHPOINTS = 1638400
    swMouse_SelectHELIX = 1703936
    swMouse_SelectREFERENCECURVES = 1703936
    swMouse_SelectREFSURFACES = 1769472
    swMouse_SelectCENTERMARKS = 1835008
    swMouse_SelectINCONTEXTFEAT = 1900544
    swMouse_SelectMATEGROUP = 1966080
    swMouse_SelectBREAKLINES = 2031616
    swMouse_SelectINCONTEXTFEATS = 2097152
    swMouse_SelectMATEGROUPS = 2162688
    swMouse_SelectSKETCHTEXT = 2228224
    swMouse_SelectSFSYMBOLS = 2293760
    swMouse_SelectDATUMTAGS = 2359296
    swMouse_SelectCOMPPATTERN = 2424832
    swMouse_SelectWELDS = 2490368
    swMouse_SelectCTHREADS = 2555904
    swMouse_SelectDTMTARGS = 2621440
    swMouse_SelectPOINTREFS = 2686976
    swMouse_SelectDCABINETS = 2752512
    swMouse_SelectEXPLVIEWS = 2818048
    swMouse_SelectEXPLSTEPS = 2883584
    swMouse_SelectEXPLLINES = 2949120
    swMouse_SelectSILHOUETTES = 3014656
    swMouse_SelectCONFIGURATIONS = 3080192
    swMouse_SelectOBJHANDLES = 3145728
    swMouse_SelectARROWS = 3211264
    swMouse_SelectZONES = 3276800
    swMouse_SelectREFEDGES = 3342336
    swMouse_SelectREFFACES = 3407872
    swMouse_SelectREFSILHOUETTE = 3473408
    swMouse_SelectBOMS = 3538944
    swMouse_SelectEQNFOLDER = 3604480
    swMouse_SelectSKETCHHATCH = 3670016
    swMouse_SelectIMPORTFOLDER = 3735552
    swMouse_SelectVIEWERHYPERLINK = 3801088
    swMouse_SelectMIDPOINTS = 3866624
    swMouse_SelectCUSTOMSYMBOLS = 3932160
    swMouse_SelectCOORDSYS = 3997696
    swMouse_SelectDATUMLINES = 4063232
    swMouse_SelectROUTECURVES = 4128768
    swMouse_SelectBOMTEMPS = 4194304
    swMouse_SelectROUTEPOINTS = 4259840
    swMouse_SelectCONNECTIONPOINTS = 4325376
    swMouse_SelectROUTESWEEPS = 4390912
    swMouse_SelectPOSGROUP = 4456448
    swMouse_SelectBROWSERITEM = 4521984
    swMouse_SelectFABRICATEDROUTE = 4587520
    swMouse_SelectSKETCHPOINTFEAT = 4653056
    swMouse_SelectEMPTYSPACE = 4718592
    swMouse_SelectCOMPSDONTOVERRIDE = 4718592
    swMouse_SelectLIGHTS = 4784128
    swMouse_SelectWIREBODIES = 4849664
    swMouse_SelectSURFACEBODIES = 4915200
    swMouse_SelectSOLIDBODIES = 4980736
    swMouse_SelectFRAMEPOINT = 5046272
    swMouse_SelectSURFBODIESFIRST = 5111808
    swMouse_SelectMANIPULATORS = 5177344
    swMouse_SelectPICTUREBODIES = 5242880
    swMouse_SelectSOLIDBODIESFIRST = 5308416
    swMouse_SelectHOLESERIES = 5439488
    swMouse_SelectLEADERS = 5505024
    swMouse_SelectSKETCHBITMAP = 5570560
    swMouse_SelectDOWELSYMS = 5636096
    swMouse_SelectEXTSKETCHTEXT = 5767168
    swMouse_SelectBLOCKINST = 6094848
    swMouse_SelectFTRFOLDER = 6160384
    swMouse_SelectSKETCHREGION = 6225920
    swMouse_SelectSKETCHCONTOUR = 6291456
    swMouse_SelectBOMFEATURES = 6356992
    swMouse_SelectANNOTATIONTABLES = 6422528
    swMouse_SelectBLOCKDEF = 6488064
    swMouse_SelectCENTERMARKSYMS = 6553600
    swMouse_SelectSIMULATION = 6619136
    swMouse_SelectSIMELEMENT = 6684672
    swMouse_SelectCENTERLINES = 6750208
    swMouse_SelectHOLETABLEFEATS = 6815744
    swMouse_SelectHOLETABLEAXES = 6881280
    swMouse_SelectWELDMENT = 6946816
    swMouse_SelectSUBWELDFOLDER = 7012352
    swMouse_SelectEXCLUDEMANIPULATORS = 7274496
    swMouse_SelectREVISIONTABLE = 7405568
    swMouse_SelectSUBSKETCHINST = 7471104
    swMouse_SelectWELDMENTTABLEFEATS = 7602176
    swMouse_SelectBODYFOLDER = 7733248
    swMouse_SelectREVISIONTABLEFEAT = 7798784
    swMouse_SelectSUBATOMFOLDER = 7929856
    swMouse_SelectWELDBEADS = 7995392
    swMouse_SelectEMBEDLINKDOC = 8060928
    swMouse_SelectJOURNAL = 8126464
    swMouse_SelectDOCSFOLDER = 8192000
    swMouse_SelectCOMMENTSFOLDER = 8257536
    swMouse_SelectCOMMENT = 8323072
    swMouse_SelectSWIFTANNOTATIONS = 8519680
    swMouse_SelectSWIFTFEATURES = 8650752
    swMouse_SelectCAMERAS = 8912896
    swMouse_SelectMATESUPPLEMENT = 9043968
    swMouse_SelectANNOTATIONVIEW = 9109504
    swMouse_SelectGENERALTABLEFEAT = 9306112
    swMouse_SelectDISPLAYSTATE = 9699328
    swMouse_SelectSUBSKETCHDEF = 10092544
    swMouse_SelectSWIFTSCHEMA = 10420224
    swMouse_SelectTITLEBLOCK = 12582912
    swMouse_SelectTITLEBLOCKTABLEFEAT = 13500416
    swMouse_SelectOBJGROUP = 13565952
    swMouse_SelectPLANESECTIONS = 14352384
    swMouse_SelectCOSMETICWELDS = 14417920
    swMouse_SelectMAGNETICLINES = 14745600
    swMouse_SelectPUNCHTABLEFEATS = 15335424
    swMouse_SelectREVISIONCLOUDS = 15728640
    swMouse_SelectBorder = 16646144
    swMouse_SelectSELECTIONSETFOLDER = 16908288
    swMouse_SelectSELECTIONSETNODE = 16973824

class swMoveCopyBodyFeatureTransformType_e(IntEnum):
    """swMoveCopyBodyFeatureTransformType_e (3 constants, from SwConst)."""
    swTransformType_None = 0
    swTransformType_Translation = 1
    swTransformType_Rotation = 2

class swMoveCopyError_e(IntEnum):
    """swMoveCopyError_e (3 constants, from SwConst)."""
    swMoveCopyErrorNone = 0
    swMoveCopyErrorSourceDoesNotExist = 1
    swMoveCopyErrorFail = 2

class swMoveCopyOptions_e(IntEnum):
    """swMoveCopyOptions_e (2 constants, from SwConst)."""
    swMoveCopyOptionsOverwriteExistingDocs = 1
    swMoveCopyOptionsCreateNewFolder = 2

class swMoveFaceType_e(IntEnum):
    """swMoveFaceType_e (3 constants, from SwConst)."""
    swMoveFaceTypeOffset = 0
    swMoveFaceTypeTranslate = 1
    swMoveFaceTypeRotate = 2

class swMoveFreezeBarTo_e(IntEnum):
    """swMoveFreezeBarTo_e (4 constants, from SwConst)."""
    swMoveFreezeBarToEnd = 1
    swMoveFreezeBarToBeforeFeature = 2
    swMoveFreezeBarToAfterFeature = 3
    swMoveFreezeBarToTop = 4

class swMoveLocation_e(IntEnum):
    """swMoveLocation_e (5 constants, from SwConst)."""
    swMoveAfter = 3
    swMoveBefore = 2
    swMoveToEnd = 1
    swMoveToTop = 4
    swMoveToFolder = 5

class swMoveRollbackBarTo_e(IntEnum):
    """swMoveRollbackBarTo_e (4 constants, from SwConst)."""
    swMoveRollbackBarToEnd = 1
    swMoveRollbackBarToPreviousPosition = 2
    swMoveRollbackBarToBeforeFeature = 3
    swMoveRollbackBarToAfterFeature = 4

class swMoveableDatumDirection_e(IntEnum):
    """swMoveableDatumDirection_e (6 constants, from SwConst)."""
    swMoveableDatumDirectionLeft = 0
    swMoveableDatumDirectionRight = 1
    swMoveableDatumDirectionUp = 2
    swMoveableDatumDirectionDown = 3
    swMoveableDatumDirectionFreeDrag = 4
    swMoveableDatumDirectionBySelection = 5

class swMoveableDatumStyle_e(IntEnum):
    """swMoveableDatumStyle_e (3 constants, from SwConst)."""
    swMoveableDatumStyle_NotMoveable = 0
    swMoveableDatumStyle_Horizontal = 1
    swMoveableDatumStyle_Rotational = 2

class swNameType_e(IntEnum):
    """swNameType_e (2 constants, from SwConst)."""
    swBodyName = 0
    swFeatureName = 1

class swNonInterferingComponentDisplay_e(IntEnum):
    """swNonInterferingComponentDisplay_e (4 constants, from SwConst)."""
    swNonInterferingComponentDisplay_Wireframe = 0
    swNonInterferingComponentDisplay_Hidden = 1
    swNonInterferingComponentDisplay_Transparent = 2
    swNonInterferingComponentDisplay_Current = 3

class swNormalCutErrors_e(IntEnum):
    """swNormalCutErrors_e (2 constants, from SwConst)."""
    swAddNormalCutGroup_Success = 0
    swAddNormalCutGroup_Failed = 1

class swNormalCutParameters_e(IntEnum):
    """swNormalCutParameters_e (2 constants, from SwConst)."""
    swNormalCutExtent = 0
    swNormalCutOffsetPlane = 1

class swNotifyEntityType_e(IntEnum):
    """swNotifyEntityType_e (8 constants, from SwConst)."""
    swNotifyConfiguration = 1
    swNotifyComponent = 2
    swNotifyFeature = 3
    swNotifyDerivedConfiguration = 4
    swNotifyDrawingSheet = 5
    swNotifyDrawingView = 6
    swNotifyBlockDef = 7
    swNotifyComponentInternal = 8

class swNumberboxUnitType_e(IntEnum):
    """swNumberboxUnitType_e (11 constants, from SwConst)."""
    swNumberBox_UnitlessInteger = 1
    swNumberBox_UnitlessDouble = 2
    swNumberBox_Length = 3
    swNumberBox_Angle = 4
    swNumberBox_Density = 5
    swNumberBox_Stress = 6
    swNumberBox_Force = 7
    swNumberBox_Gravity = 8
    swNumberBox_Time = 9
    swNumberBox_Frequency = 10
    swNumberBox_Percent = 11

class swNumberedListStartType_e(IntEnum):
    """swNumberedListStartType_e (3 constants, from SwConst)."""
    swStartNumberingInvalid = -1
    swStartNumberingFromTop = 0
    swStartNumberingFromBottom = 1

class swNumberedListType_e(IntEnum):
    """swNumberedListType_e (6 constants, from SwConst)."""
    swNumberedListTypeInvalid = 0
    swNumberedListType1 = 1
    swNumberedListType2 = 2
    swNumberedListType3 = 3
    swNumberedListType4 = 4
    swNumberedListType5 = 5

class swNumberingFormat_e(IntEnum):
    """swNumberingFormat_e (4 constants, from SwConst)."""
    swNumberingFormatInvalid = -1
    swNumberingFormat1 = 0
    swNumberingFormat2 = 1
    swNumberingFormat3 = 2

class swNumberingType_e(IntEnum):
    """swNumberingType_e (4 constants, from SwConst)."""
    swNumberingType_None = 0
    swNumberingType_Detailed = 1
    swNumberingType_Flat = 2
    swIndentedBOMNotSet = 3

class swObjectEquality(IntEnum):
    """swObjectEquality (3 constants, from SwConst)."""
    swObjectNotSame = 0
    swObjectSame = 1
    swObjectUnsupported = 2

class swOffsetPlanarWireBodyOptions_e(IntEnum):
    """swOffsetPlanarWireBodyOptions_e (3 constants, from SwConst)."""
    swOffsetPlanarWireBodyOptions_GapFillRound = 0
    swOffsetPlanarWireBodyOptions_GapFillExtend = 1
    swOffsetPlanarWireBodyOptions_GapFillTangent = 2

class swOleObjectOptions_e(IntEnum):
    """swOleObjectOptions_e (2 constants, from SwConst)."""
    swOleObjectOptions_GetAll = 0
    swOleObjectOptions_GetOnCurrentSheet = 1

class swOnSurfacePlaneProjectType_e(IntEnum):
    """swOnSurfacePlaneProjectType_e (2 constants, from SwConst)."""
    swOnSurfacePlaneProjecttoNearestLocation = 0
    swOnSurfacePlaneProjectAlongSketchNormal = 1

class swOpenDocOptions_e(IntEnum):
    """swOpenDocOptions_e (14 constants, from SwConst)."""
    swOpenDocOptions_Silent = 1
    swOpenDocOptions_ReadOnly = 2
    swOpenDocOptions_ViewOnly = 4
    swOpenDocOptions_RapidDraft = 8
    swOpenDocOptions_LoadModel = 16
    swOpenDocOptions_AutoMissingConfig = 32
    swOpenDocOptions_OverrideDefaultLoadLightweight = 64
    swOpenDocOptions_LoadLightweight = 128
    swOpenDocOptions_DontLoadHiddenComponents = 256
    swOpenDocOptions_LoadExternalReferencesInMemory = 512
    swOpenDocOptions_OpenDetailingMode = 1024
    swOpenDocOptions_LDR_EditAssembly = 2048
    swOpenDocOptions_SpeedPak = 4096
    swOpenDocOptions_AdvancedConfig = 8192

class swOrdDimEndSymbol_e(IntEnum):
    """swOrdDimEndSymbol_e (4 constants, from SwConst)."""
    swOrdDimEndSymbol_None = 0
    swOrdDimEndSymbol_Dowel = 1
    swOrdDimEndSymbol_UpwardRight = 2
    swOrdDimEndSymbol_DownwardLeft = 3

class swOutOfDateStatus_e(IntEnum):
    """swOutOfDateStatus_e (3 constants, from SwConst)."""
    swUnknownState = 0
    swModelUpToDate = 1
    swModelOutOfDate = 2

class swPLYQuality_e(IntEnum):
    """swPLYQuality_e (3 constants, from SwConst)."""
    swPLYQuality_Coarse = 1
    swPLYQuality_Fine = 2
    swPLYQuality_Custom = 3

class swPMContainer_e(IntEnum):
    """swPMContainer_e (5 constants, from SwConst)."""
    swPMInTabsWithFM = 0
    swPMPinnedAboveFM = 1
    swPMPinnedNextToFM = 2
    swPMFloating = 3
    swPMPinnedLowerRight = 4

class swPMIDatumAnchorStyle_e(IntEnum):
    """swPMIDatumAnchorStyle_e (4 constants, from SwConst)."""
    swPMIDatumAnchorStyle_FilledTriangle = 0
    swPMIDatumAnchorStyle_FilledTriangleWithShoulder = 1
    swPMIDatumAnchorStyle_EmptyTriangle = 2
    swPMIDatumAnchorStyle_EmptyTriangleWithShoulder = 3

class swPMIDatumShape_e(IntEnum):
    """swPMIDatumShape_e (2 constants, from SwConst)."""
    swPMIDatumShape_Square = 0
    swPMIDatumShape_Round = 1

class swPMIDatumTargetAreaStyle_e(IntEnum):
    """swPMIDatumTargetAreaStyle_e (5 constants, from SwConst)."""
    swPMIDatumTargetAreaStyle_None = 0
    swPMIDatumTargetAreaStyle_Unknown = 1
    swPMIDatumTargetAreaStyle_X = 2
    swPMIDatumTargetAreaStyle_Circular = 3
    swPMIDatumTargetAreaStyle_Rectangular = 4

class swPMIDatumTargetMovableStyle_e(IntEnum):
    """swPMIDatumTargetMovableStyle_e (4 constants, from SwConst)."""
    swPMIDatumTargetMovableStyle_None = 0
    swPMIDatumTargetMovableStyle_Unknown = 1
    swPMIDatumTargetMovableStyle_Horizontal = 2
    swPMIDatumTargetMovableStyle_Rotational = 3

class swPMIDatumTargetSymbolStyle_e(IntEnum):
    """swPMIDatumTargetSymbolStyle_e (4 constants, from SwConst)."""
    swPMIDatumTargetSymbolStyle_None = 0
    swPMIDatumTargetSymbolStyle_Unknown = 1
    swPMIDatumTargetSymbolStyle_Symbol = 2
    swPMIDatumTargetSymbolStyle_AreaOutside = 3

class swPMIDatumType_e(IntEnum):
    """swPMIDatumType_e (2 constants, from SwConst)."""
    swPMIDatumType_DatumFeature = 0
    swPMIDatumType_DatumTarget = 1

class swPMILeaderLocation_e(IntEnum):
    """swPMILeaderLocation_e (4 constants, from SwConst)."""
    swPMILeaderLocation_None = 0
    swPMILeaderLocation_Left = 1
    swPMILeaderLocation_Right = 2
    swPMILeaderLocation_Nearest = 3

class swPMILeaderModifier_e(IntEnum):
    """swPMILeaderModifier_e (5 constants, from SwConst)."""
    swPMILeaderModifier_None = 0
    swPMILeaderModifier_AllAround = 1
    swPMILeaderModifier_AllAroundThisSide = 2
    swPMILeaderModifier_AllOver = 3
    swPMILeaderModifier_AllOverThisSide = 4

class swPMILeaderStyle_e(IntEnum):
    """swPMILeaderStyle_e (7 constants, from SwConst)."""
    swPMILeaderStyle_None = 0
    swPMILeaderStyle_Straight = 1
    swPMILeaderStyle_Bent = 2
    swPMILeaderStyle_Perpendicular = 3
    swPMILeaderStyle_Outside = 4
    swPMILeaderStyle_Inside = 5
    swPMILeaderStyle_Smart = 6

class swPMILeaderType_e(IntEnum):
    """swPMILeaderType_e (3 constants, from SwConst)."""
    swPMILeaderType_NoLeader = 0
    swPMILeaderType_Leader = 1
    swPMILeaderType_MultiJog = 2

class swPMITolPerUnitAreaType_e(IntEnum):
    """swPMITolPerUnitAreaType_e (5 constants, from SwConst)."""
    swPMITolPerUnitType_None = 0
    swPMITolPerUnitType_Unknown = 1
    swPMITolPerUnitType_Circular = 2
    swPMITolPerUnitType_Rectangular = 3
    swPMITolPerUnitType_Square = 4

class swPMIType_e(IntEnum):
    """swPMIType_e (5 constants, from SwConst)."""
    swPMIType_None = 0
    swPMIType_Dimension = 1
    swPMIType_Datum = 2
    swPMIType_GTol = 3
    swPMIType_Unknown = 4

class swPMIUnit_e(IntEnum):
    """swPMIUnit_e (14 constants, from SwConst)."""
    swPMIUnit_None = 0
    swPMIUnit_ANGSTROM = 1
    swPMIUnit_CM = 2
    swPMIUnit_FEET = 3
    swPMIUnit_FEETINCHES = 4
    swPMIUnit_INCHES = 5
    swPMIUnit_METER = 6
    swPMIUnit_MICRON = 7
    swPMIUnit_MIL = 8
    swPMIUnit_MM = 9
    swPMIUnit_NANOMETER = 10
    swPMIUnit_UIN = 11
    swPMIUnit_DEGREE = 12
    swPMIUnit_RADIAN = 13

class swPackAndGoDocumentStatus_e(IntEnum):
    """swPackAndGoDocumentStatus_e (3 constants, from SwConst)."""
    swPackAndGoDocumentStatus_Normal = 0
    swPackAndGoDocumentStatus_Virtual = 1
    swPackAndGoDocumentStatus_UnKnown = 2

class swPackAndGoFolderOptions_e(IntEnum):
    """swPackAndGoFolderOptions_e (3 constants, from SwConst)."""
    swPackAndGoFolderOptions_SingleFolder = 0
    swPackAndGoFolderOptions_MinimalFolders = 1
    swPackAndGoFolderOptions_FullStructure = 2

class swPackAndGoSaveStatus_e(IntEnum):
    """swPackAndGoSaveStatus_e (5 constants, from SwConst)."""
    swPackAndGoSaveStatus_Succeed = 0
    swPackAndGoSaveStatus_UserInputNotCorrect = 1
    swPackAndGoSaveStatus_FileAlreadyExist = 2
    swPackAndGoSaveStatus_SaveToEmpty = 3
    swPackAndGoSaveStatus_SaveError = 4

class swPageSetupDrawingColor_e(IntEnum):
    """swPageSetupDrawingColor_e (3 constants, from SwConst)."""
    swPageSetup_AutomaticDrawingColor = 1
    swPageSetup_ColorGrey = 2
    swPageSetup_BlackAndWhite = 3

class swPageSetupInUse_e(IntEnum):
    """swPageSetupInUse_e (3 constants, from SwConst)."""
    swPageSetupInUse_Application = 1
    swPageSetupInUse_Document = 2
    swPageSetupInUse_DrawingSheet = 3

class swPageSetupOrientation_e(IntEnum):
    """swPageSetupOrientation_e (2 constants, from SwConst)."""
    swPageSetupOrient_Portrait = 1
    swPageSetupOrient_Landscape = 2

class swParabolaPts_e(IntEnum):
    """swParabolaPts_e (4 constants, from SwConst)."""
    swParabolaStartPt = 0
    swParabolaEndPt = 1
    swParabolaFocusPt = 2
    swParabolaApexPt = 3

class swParagraphType_e(IntEnum):
    """swParagraphType_e (3 constants, from SwConst)."""
    swParagraphNone = -1
    swParagraphBullet = 0
    swParagraphNumbered = 1

class swParamType_e(IntEnum):
    """swParamType_e (4 constants, from SwConst)."""
    swParamTypeDouble = 0
    swParamTypeString = 1
    swParamTypeInteger = 2
    swParamTypeDVector = 3

class swParameterizationPropertyType_e(IntEnum):
    """swParameterizationPropertyType_e (6 constants, from SwConst)."""
    swParameterizationPropertyType_Periodic = 13701
    swParameterizationPropertyType_AllDerivativesContinuous = 13737
    swParameterizationPropertyType_AllDerivativesNotContinuous = 13738
    swParameterizationPropertyType_Linear = 13739
    swParameterizationPropertyType_Circular = 13740
    swParameterizationPropertyType_BoundsCoincident = 13746

class swParasolidOutputVersion_e(IntEnum):
    """swParasolidOutputVersion_e (34 constants, from SwConst)."""
    swParasolidOutputVersion_latest = 0
    swParasolidOutputVersion_80 = 1
    swParasolidOutputVersion_90 = 2
    swParasolidOutputVersion_91 = 3
    swParasolidOutputVersion_100 = 4
    swParasolidOutputVersion_110 = 5
    swParasolidOutputVersion_111 = 6
    swParasolidOutputVersion_120 = 7
    swParasolidOutputVersion_121 = 8
    swParasolidOutputVersion_130 = 9
    swParasolidOutputVersion_140 = 10
    swParasolidOutputVersion_150 = 11
    swParasolidOutputVersion_151 = 12
    swParasolidOutputVersion_160 = 13
    swParasolidOutputVersion_161 = 14
    swParasolidOutputVersion_171 = 15
    swParasolidOutputVersion_181 = 16
    swParasolidOutputVersion_191 = 17
    swParasolidOutputVersion_200 = 18
    swParasolidOutputVersion_210 = 19
    swParasolidOutputVersion_220 = 20
    swParasolidOutputVersion_230 = 21
    swParasolidOutputVersion_240 = 22
    swParasolidOutputVersion_250 = 23
    swParasolidOutputVersion_260 = 24
    swParasolidOutputVersion_270 = 25
    swParasolidOutputVersion_280 = 26
    swParasolidOutputVersion_290 = 27
    swParasolidOutputVersion_300 = 28
    swParasolidOutputVersion_310 = 29
    swParasolidOutputVersion_320 = 30
    swParasolidOutputVersion_330 = 31
    swParasolidOutputVersion_341 = 32
    swParasolidOutputVersion_351 = 33

class swPartConfigurationGroupingOption_e(IntEnum):
    """swPartConfigurationGroupingOption_e (3 constants, from SwConst)."""
    swDisplay_ConfigurationOfSamePart_AsSeparateItem = 1
    swDisplay_AllConfigurationOfSamePart_AsOneItem = 2
    swDisplay_ConfigurationWithSameName_AsOneItem = 3

class swPartDimXpertToleranceMethod_e(IntEnum):
    """swPartDimXpertToleranceMethod_e (3 constants, from SwConst)."""
    swPartDimXpertToleranceMethod_BlockTolerance = 0
    swPartDimXpertToleranceMethod_GeneralTolerance = 1
    swPartDimXpertToleranceMethod_GeneralBlockTolerance = 2

class swPartNotify_e(IntEnum):
    """swPartNotify_e (85 constants, from SwConst)."""
    swPartRegenNotify = 1
    swPartDestroyNotify = 2
    swPartRegenPostNotify = 3
    swPartViewNewNotify = 4
    swPartNewSelectionNotify = 5
    swPartFileSaveNotify = 6
    swPartFileSaveAsNotify = 7
    swPartLoadFromStorageNotify = 8
    swPartSaveToStorageNotify = 9
    swPartConfigChangeNotify = 10
    swPartConfigChangePostNotify = 11
    swPartAutoSaveNotify = 12
    swPartAutoSaveToStorageNotify = 13
    swPartViewNewNotify2 = 14
    swPartLightingDialogCreateNotify = 15
    swPartAddItemNotify = 16
    swPartRenameItemNotify = 17
    swPartDeleteItemNotify = 18
    swPartModifyNotify = 19
    swPartFileReloadNotify = 20
    swPartAddCustomPropertyNotify = 21
    swPartChangeCustomPropertyNotify = 22
    swPartDeleteCustomPropertyNotify = 23
    swPartFeatureEditPreNotify = 24
    swPartFeatureSketchEditPreNotify = 25
    swPartFileSaveAsNotify2 = 26
    swPartDeleteSelectionPreNotify = 27
    swPartFileReloadPreNotify = 28
    swPartBodyVisibleChangeNotify = 29
    swPartRegenPostNotify2 = 30
    swPartFileSavePostNotify = 31
    swPartLoadFromStorageStoreNotify = 32
    swPartSaveToStorageStoreNotify = 33
    swPartFeatureManagerTreeRebuildNotify = 34
    swPartFileDropPostNotify = 35
    swPartDynamicHighlightNotify = 36
    swPartDimensionChangeNotify = 37
    swPartFileReloadCancelNotify = 38
    swPartFileSavePostCancelNotify = 39
    swPartSketchSolveNotify = 40
    swPartDeleteItemPreNotify = 41
    swPartClearSelectionsNotify = 42
    swPartEquationEditorPreNotify = 43
    swPartEquationEditorPostNotify = 44
    swPartOpenDesignTableNotify = 45
    swPartCloseDesignTableNotify = 46
    swPartPromptBodiesToKeepNotify = 47
    swPartAddDvePagePreNotify = 48
    swPartUnitsChangeNotify = 49
    swPartDestroyNotify2 = 50
    swPartConfigurationChangeNotify = 51
    swPartSuppressionStateChangeNotify = 52
    swPartActiveViewChangeNotify = 53
    swPartFeatureManagerFilterStringChangeNotify = 54
    swPartFlipLoopNotify = 55
    swPartFileDropPreNotify = 56
    swPartSensorAlertPreNotify = 57
    swPartUndoPostNotify = 58
    swPartUserSelectionPreNotify = 59
    swPartActiveDisplayStateChangePreNotify = 60
    swPartActiveDisplayStateChangePostNotify = 61
    swPartRedoPostNotify = 62
    swPartRedoPreNotify = 63
    swPartUndoPreNotify = 64
    swPartWeldmentCutListUpdatePostNotify = 65
    swPartAutoSaveToStorageStoreNotify = 66
    swPartDragStateChangeNotify = 67
    swPartInsertTableNotify = 68
    swPartModifyTableNotify = 69
    swPartUserSelectionPostNotify = 70
    swPartCommandManagerTabActivatedPreNotify = 71
    swPartPreRenameItemNotify = 72
    swPartRenamedDocumentNotify = 73
    swPartFeatureManagerTabActivatedPreNotify = 74
    swPartFeatureManagerTabActivatedNotify = 75
    swPartPublishTo3DPDFNotify = 76
    swPartConvertToBodiesPreNotify = 77
    swPartConvertToBodiesPostNotify = 78
    swPartRenameDisplayTitleNotify = 79
    swPartActiveAnnotationViewChangeNotify = 80
    swPartDisplayPaneExpandNotify = 81
    swPartDisplayPaneCollapseNotify = 82
    swPartSolidBodyFolderReorderNotify = 83
    swPartAddDependencyNotify = 84
    swPartDeleteDependencyNotify = 85

class swPartingLineFeatureStatus_e(IntEnum):
    """swPartingLineFeatureStatus_e (4 constants, from SwConst)."""
    STATUS_MOLD_REDUNDANT_EDGES = 1
    STATUS_MOLD_PARTINGLINE_EDGES_OPEN = 2
    STATUS_MOLD_PARTINGLINE_SEPARABLE = 3
    STATUS_MOLD_PARTINGLINE_NON_SEPARABLE = 4

class swPartingSurfaceMoldParmType_e(IntEnum):
    """swPartingSurfaceMoldParmType_e (3 constants, from SwConst)."""
    swPartingSurfaceMoldParmTangent = 0
    swPartingSurfaceMoldParmNormal = 1
    swPartingSurfaceMoldParmPerpendicular = 4

class swPartingSurfaceSmoothingType_e(IntEnum):
    """swPartingSurfaceSmoothingType_e (2 constants, from SwConst)."""
    swPartingSurfaceSharp = 1
    swPartingSurfaceSmooth = 2

class swPartnerEntitlementStatus_e(IntEnum):
    """swPartnerEntitlementStatus_e (8 constants, from SwConst)."""
    swPESuccess = 0
    swPEFail = 1
    swPEAddinNameMismatch = 2
    swPEAddinGUIDMismatch = 4
    swPEVersionMismatch = 8
    swPELicenseExpired = 16
    swPETierMismatch = 32
    swPELicenseError = 64

class swPatternElementSelection_e(IntEnum):
    """swPatternElementSelection_e (3 constants, from SwConst)."""
    swErrorInPatternElementSelection = 0
    swFeatureFaces = 1
    swBodiesToPattern = 2

class swPatternEndCondition_e(IntEnum):
    """swPatternEndCondition_e (2 constants, from SwConst)."""
    swPatternEndCondition_SpacingAndInstances = 0
    swPatternEndCondition_UpToReference = 1

class swPatternFeatureImportExportError_e(IntEnum):
    """swPatternFeatureImportExportError_e (21 constants, from SwConst)."""
    swPatternFeatureImportExportError_Succeed = 0
    swPatternFeatureImportExportError_Failed = 1
    swPatternFeatureImportExportError_UnequalNumOfCellsInColumn = 2
    swPatternFeatureImportExportError_UnequalNumOfCellsInRow = 3
    swPatternFeatureImportExportError_EmptyRowsOrColumns = 4
    swPatternFeatureImportExportError_ColumnARows1And2Error = 5
    swPatternFeatureImportExportError_InstNumStartsFromNonZero = 6
    swPatternFeatureImportExportError_ColumnBRows1And2Error = 7
    swPatternFeatureImportExportError_ImproperValuesForColumnB = 8
    swPatternFeatureImportExportError_FeatureDoesNotExist = 9
    swPatternFeatureImportExportError_DuplicateDimensions = 10
    swPatternFeatureImportExportError_OutOfRangeDimensionValue = 11
    swPatternFeatureImportExportError_DimensionNameDoesNotExist = 12
    swPatternFeatureImportExportError_FeatureOrDimDoesNotExist = 13
    swPatternFeatureImportExportError_NoValidDimensionToImport = 14
    swPatternFeatureImportExportError_DimValueFormatIncorrect = 15
    swPatternFeatureImportExportError_FailedToRetrieveModelDocument = 16
    swPatternFeatureImportExportError_FileExistsAndOverwriteIsFalse = 17
    swPatternFeatureImportExportError_ReadOnlyFile = 18
    swPatternFeatureImportExportError_AccessDeniedOrInvalidPath = 19
    swPatternFeatureImportExportError_FailedToRetrieveExcelApp = 20

class swPatternLayoutSpacingType_e(IntEnum):
    """swPatternLayoutSpacingType_e (2 constants, from SwConst)."""
    swPatternLayoutTargetSpacing = 0
    swPatternLayoutInstances = 1

class swPatternLayoutType_e(IntEnum):
    """swPatternLayoutType_e (4 constants, from SwConst)."""
    swPatternLayoutCircular = 0
    swPatternLayoutSquare = 1
    swPatternLayoutPolygon = 2
    swPatternLayoutPerforation = 3

class swPatternReferenceTypes_e(IntEnum):
    """swPatternReferenceTypes_e (4 constants, from SwConst)."""
    swPatternReferenceTypeAxis = 0
    swPatternReferenceTypeEdge = 1
    swPatternReferenceTypeRefDim = 2
    swPatternReferenceTypeFace = 3

class swPerformanceFeedback_e(IntEnum):
    """swPerformanceFeedback_e (4 constants, from SwConst)."""
    swPerformanceFeedback_No = 0
    swPerformanceFeedback_Yes = 1
    swPerformanceFeedback_RemindLater = 2
    swPerformanceFeedback_RemindNow = 3

class swPersistReferencedObjectStates_e(IntEnum):
    """swPersistReferencedObjectStates_e (4 constants, from SwConst)."""
    swPersistReferencedObject_Ok = 0
    swPersistReferencedObject_Invalid = 1
    swPersistReferencedObject_Suppressed = 2
    swPersistReferencedObject_Deleted = 4

class swPipingPenetrationStatus_e(IntEnum):
    """swPipingPenetrationStatus_e (10 constants, from SwConst)."""
    swPenetrationSucceeded = 0
    swPenetrationFailed = 1
    swPenetrationFailedPipeTooWide = 2
    swPenetrationFailedDllNotLoaded = 3
    swPenetrationFailedNoSelection = 4
    swPenetrationFailedNotRouting = 5
    swPenetrationFailedBadSelection = 6
    swPenetrationFailedBadFitting = 7
    swPenetrationFailedAlreadyPenetrating = 8
    swPenetrationFailedMultiBody = 9

class swPointInferenceBrokerOption_e(IntEnum):
    """swPointInferenceBrokerOption_e (1 constants, from SwConst)."""
    swPointInferenceBrokerOption_IncludeHidden = 1

class swPointStyle_e(IntEnum):
    """swPointStyle_e (4 constants, from SwConst)."""
    swPointStyle_X = 1
    swPointStyle_Plus = 2
    swPointStyle_XPlus = 3
    swPointStyle_Circle = 4

class swPointToPointAutoRouteConversionMode_e(IntEnum):
    """swPointToPointAutoRouteConversionMode_e (2 constants, from SWRoutingLib)."""
    swFlexibleMode = 1
    swOrthogonalMode = 2

class swPointToPointAutoRouteErrorType_e(IntEnum):
    """swPointToPointAutoRouteErrorType_e (4 constants, from SWRoutingLib)."""
    swRouteTypeAndConversionModeMismatch = 1
    swCouldNotCreateRoute = 2
    swNoRouteFound = 3
    swPointToPointAutoRouteNoError = 4

class swPresentationOpts_e(IntEnum):
    """swPresentationOpts_e (32 constants, from SwConst)."""
    swPresentationOpts_None = 0
    swPresentationOpts_Pres = 1
    swPresentationOpts_U3D = 2
    swPresentationOpts_Animations = 4
    swPresentationOpts_Explodes = 8
    swPresentationOpts_CameraMovement = 16
    swPresentationOpts_ActiveView = 32
    swPresentationOpts_TopView = 64
    swPresentationOpts_BottomView = 128
    swPresentationOpts_LeftView = 256
    swPresentationOpts_RightView = 512
    swPresentationOpts_FrontView = 1024
    swPresentationOpts_BackView = 2048
    swPresentationOpts_NormalView = 4096
    swPresentationOpts_IsometricView = 8192
    swPresentationOpts_TrimetricView = 16384
    swPresentationOpts_DimetricView = 32768
    swPresentationOpts_OpenPDF = 65536
    swPresentationOpts_ExcludeFromAnnoView = 131072
    swPresentationOpts_CreateAttachSTEP242 = 262144
    swPresentationOpts_LowAccuracy = 524288
    swPresentationOpts_HighAccuracy = 1048576
    swPresentationOpts_MedAccuracy = 2097152
    swPresentationOpts_MaxAccuracy = 4194304
    swPresentationOpts_CompressTesselation = 8388608
    swPresentationOpts_DisablePrinting3DPDF = 16777216
    swPresentationOpts_DisableEditing3DPDF = 33554432
    swPresentationOpts_DisableCopying3DPDF = 67108864
    swPresentationOpts_ShowOnlyGraphicalData = 134217728
    swPresentationOpts_PDFPreview = 268435456
    swPresentationOpts_SingleHTML = 536870912
    swPresentationOpts_ChkOpenPassword3DPDF = 1073741824

class swPrimaryMemberPointLengthEndCondition_e(IntEnum):
    """swPrimaryMemberPointLengthEndCondition_e (4 constants, from SwConst)."""
    swPrimaryMemberPointLengthEndCondition_Length = 0
    swPrimaryMemberPointLengthEndCondition_Point = 1
    swPrimaryMemberPointLengthEndCondition_UpToPoint = 2
    swPrimaryMemberPointLengthEndCondition_UpToPlane = 3

class swPrintProperties_e(IntEnum):
    """swPrintProperties_e (4 constants, from SwConst)."""
    swPrintPaperSize = 0
    swPrintOrientation = 1
    swPrintPaperLength = 2
    swPrintPaperWidth = 3

class swPrintSelectionScaleFactor_e(IntEnum):
    """swPrintSelectionScaleFactor_e (4 constants, from SwConst)."""
    swPrintAll = 0
    swPrintCurrentSheet = 1
    swPrintScreenImage = 2
    swPrintSelection = 3

class swPrompForFilenameCause_e(IntEnum):
    """swPrompForFilenameCause_e (27 constants, from SwConst)."""
    swUnused = 0
    swGeneric = 1
    swMirrorComponent = 2
    swWeldBead = 3
    swDerivedPart = 4
    swSplitAssembly = 5
    swSplitPart = 6
    swInsertEnvelopeFromFile = 7
    swMirrorComponentBrowse = 8
    swCreateNamedViewFromFile = 9
    swComponentPropsReplace = 10
    swOpenAssociatedDrawing = 11
    swFileReloadReplace = 12
    swDrawingAddViewFromFile = 13
    swDrawingInsert3ViewFromFile = 14
    swAddComponent = 15
    swStartRouteAssembly = 16
    swSaveRoutePart = 17
    swSaveVirtualComponentExternally = 18
    swEditReadOnlyComponent = 19
    swInsertBlock = 20
    swSketchBlock = 21
    swSaveDefeaturedModel = 22
    swFormNewSubAssembly = 23
    swAddVirtualComponent = 24
    swMakeComponentIndependent = 25
    swPromptForFilename_Cancelled = 26

class swPromptAlwaysNever_e(IntEnum):
    """swPromptAlwaysNever_e (3 constants, from SwConst)."""
    swResponsePrompt = 0
    swResponseAlways = 1
    swResponseNever = 2

class swPropMgrPageComboBoxStyle_e(IntEnum):
    """swPropMgrPageComboBoxStyle_e (4 constants, from SwConst)."""
    swPropMgrPageComboBoxStyle_Sorted = 1
    swPropMgrPageComboBoxStyle_EditableText = 2
    swPropMgrPageComboBoxStyle_EditBoxReadOnly = 4
    swPropMgrPageComboBoxStyle_AvoidSelectionText = 8

class swPropMgrPageControlOnResizeOptions_e(IntEnum):
    """swPropMgrPageControlOnResizeOptions_e (2 constants, from SwConst)."""
    swControlOptionsOnResize_LockLeft = 1
    swControlOptionsOnResize_LockRight = 2

class swPropMgrPageLabelStyle_e(IntEnum):
    """swPropMgrPageLabelStyle_e (4 constants, from SwConst)."""
    swPropMgrPageLabelStyle_LeftText = 1
    swPropMgrPageLabelStyle_CenterText = 2
    swPropMgrPageLabelStyle_RightText = 4
    swPropMgrPageLabelStyle_Sunken = 8

class swPropMgrPageLabelUnderlineStyle_e(IntEnum):
    """swPropMgrPageLabelUnderlineStyle_e (3 constants, from SwConst)."""
    swPropMgrPageLabel_NoUnderline = 0
    swPropMgrPageLabel_SolidUnderline = 1
    swPropMgrPageLabel_DashedUnderline = 2

class swPropMgrPageListBoxStyle_e(IntEnum):
    """swPropMgrPageListBoxStyle_e (3 constants, from SwConst)."""
    swPropMgrPageListBoxStyle_Sorted = 1
    swPropMgrPageListBoxStyle_NoIntegralHeight = 2
    swPropMgrPageListBoxStyle_MultipleItemSelect = 4

class swPropMgrPageNumberBoxStyle_e(IntEnum):
    """swPropMgrPageNumberBoxStyle_e (7 constants, from SwConst)."""
    swPropMgrPageNumberBoxStyle_ComboEditBox = 1
    swPropMgrPageNumberBoxStyle_EditBoxReadOnly = 2
    swPropMgrPageNumberBoxStyle_AvoidSelectionText = 4
    swPropMgrPageNumberBoxStyle_NoScrollArrows = 8
    swPropMgrPageNumberBoxStyle_Slider = 16
    swPropMgrPageNumberBoxStyle_Thumbwheel = 32
    swPropMgrPageNumberBoxStyle_SuppressNotifyWhileTracking = 64

class swPropMgrPageOptionStyle_e(IntEnum):
    """swPropMgrPageOptionStyle_e (1 constants, from SwConst)."""
    swPropMgrPageOptionStyle_FirstInGroup = 1

class swPropMgrPageSelectionBoxStyle_e(IntEnum):
    """swPropMgrPageSelectionBoxStyle_e (4 constants, from SwConst)."""
    swPropMgrPageSelectionBoxStyle_HScroll = 1
    swPropMgrPageSelectionBoxStyle_UpAndDownButtons = 2
    swPropMgrPageSelectionBoxStyle_MultipleItemSelect = 4
    swPropMgrPageSelectionBoxStyle_WantListboxSelectionChanged = 8

class swPropMgrPageSliderStyle_e(IntEnum):
    """swPropMgrPageSliderStyle_e (5 constants, from SwConst)."""
    swPropMgrPageSliderStyle_Vertical = 1
    swPropMgrPageSliderStyle_AutoTicks = 2
    swPropMgrPageSliderStyle_BottomLeftTicks = 4
    swPropMgrPageSliderStyle_TopRightTicks = 8
    swPropMgrPageSliderStyle_NotifyWhileTracking = 16

class swPropMgrPageTextBoxStyle_e(IntEnum):
    """swPropMgrPageTextBoxStyle_e (4 constants, from SwConst)."""
    swPropMgrPageTextBoxStyle_NotifyOnlyWhenFocusLost = 1
    swPropMgrPageTextBoxStyle_ReadOnly = 2
    swPropMgrPageTextBoxStyle_NoBorder = 4
    swPropMgrPageTextBoxStyle_Multiline = 8

class swPropSheetType_e(IntEnum):
    """swPropSheetType_e (7 constants, from SwConst)."""
    swPropSheetNotValid = 0
    swPropSheetLighting = 1
    swPropSheetToolsOptions = 2
    swPropSheetAmbientLight = 3
    swPropSheetDirectionalLight = 4
    swPropSheetPositionLight = 5
    swPropSheetSpotLight = 6

class swPropertyManagerButtonTypes_e(IntEnum):
    """swPropertyManagerButtonTypes_e (5 constants, from SwConst)."""
    swPropertyManager_OkayButton = 1
    swPropertyManager_CancelButton = 2
    swPropertyManager_HelpButton = 4
    swPropertyManager_PreviewButton = 8
    swPropertyManager_PushpinButton = 16

class swPropertyManagerCheckboxState_e(IntEnum):
    """swPropertyManagerCheckboxState_e (3 constants, from SwConst)."""
    Unchecked = 0
    Checked = 1
    Indeterminate = 2

class swPropertyManagerColorScheme_e(IntEnum):
    """swPropertyManagerColorScheme_e (8 constants, from SwConst)."""
    swPropertyManagerColorScheme_Blue = 1
    swPropertyManagerColorScheme_Gray = 2
    swPropertyManagerColorScheme_Mustard = 3
    swPropertyManagerColorScheme_Olive = 4
    swPropertyManagerColorScheme_Sand = 5
    swPropertyManagerColorScheme_SeaGreen = 6
    swPropertyManagerColorScheme_Default = 7
    swPropertyManagerColorScheme_Windows = 8

class swPropertyManagerPageBitmapButtons_e(IntEnum):
    """swPropertyManagerPageBitmapButtons_e (38 constants, from SwConst)."""
    swBitmapButtonImage_alongz = 1
    swBitmapButtonImage_angle = 2
    swBitmapButtonImage_auto_bal_circular = 3
    swBitmapButtonImage_auto_bal_left = 4
    swBitmapButtonImage_auto_bal_right = 5
    swBitmapButtonImage_auto_bal_square = 6
    swBitmapButtonImage_auto_bal_top = 7
    swBitmapButtonImage_diameter = 8
    swBitmapButtonImage_distance1 = 9
    swBitmapButtonImage_distance2 = 10
    swBitmapButtonImage_draft = 11
    swBitmapButtonImage_dve_but_cmark_bolt = 12
    swBitmapButtonImage_dve_but_cmark_linear = 13
    swBitmapButtonImage_dve_but_cmark_single = 14
    swBitmapButtonImage_leader_ang_above = 15
    swBitmapButtonImage_leader_ang_beside = 16
    swBitmapButtonImage_leader_hor_above = 17
    swBitmapButtonImage_leader_hor_beside = 18
    swBitmapButtonImage_leader_left = 19
    swBitmapButtonImage_leader_no = 20
    swBitmapButtonImage_leader_right = 21
    swBitmapButtonImage_leader_yes = 22
    swBitmapButtonImage_parallel = 23
    swBitmapButtonImage_perpendicular = 24
    swBitmapButtonImage_reverse_direction = 25
    swBitmapButtonImage_revision_circle = 26
    swBitmapButtonImage_revision_hexagon = 27
    swBitmapButtonImage_revision_square = 28
    swBitmapButtonImage_revision_triangle = 29
    swBitmapButtonImage_stackleft = 30
    swBitmapButtonImage_stackright = 31
    swBitmapButtonImage_stackup = 32
    swBitmapButtonImage_stack = 33
    swBitmapButtonImage_favorite_add = 34
    swBitmapButtonImage_favorite_delete = 35
    swBitmapButtonImage_favorite_save = 36
    swBitmapButtonImage_favorite_load = 37
    swBitmapButtonImage_dimension_set_default_attributes = 38

class swPropertyManagerPageButtons_e(IntEnum):
    """swPropertyManagerPageButtons_e (10 constants, from SwConst)."""
    swPropertyManagerPageButton_Ok = 1
    swPropertyManagerPageButton_Cancel = 2
    swPropertyManagerPageButton_Help = 3
    swPropertyManagerPageButton_Next = 4
    swPropertyManagerPageButton_Back = 5
    swPropertyManagerPageButton_Undo = 6
    swPropertyManagerPageButton_Preview = 7
    swPropertyManagerPageButton_Pushpin = 8
    swPropertyManagerPageButton_Redo = 9
    swPropertyManagerPageButton_WhatsNew = 10

class swPropertyManagerPageCloseReasons_e(IntEnum):
    """swPropertyManagerPageCloseReasons_e (8 constants, from SwConst)."""
    swPropertyManagerPageClose_UnknownReason = 0
    swPropertyManagerPageClose_Okay = 1
    swPropertyManagerPageClose_Cancel = 2
    swPropertyManagerPageClose_ParentClosed = 3
    swPropertyManagerPageClose_Closed = 4
    swPropertyManagerPageClose_UserEscape = 5
    swPropertyManagerPageClose_Apply = 6
    swPropertyManagerPageClose_Preview = 7

class swPropertyManagerPageControlLeftAlign_e(IntEnum):
    """swPropertyManagerPageControlLeftAlign_e (3 constants, from SwConst)."""
    swControlAlign_LeftEdge = 1
    swControlAlign_Indent = 2
    swControlAlign_DoubleIndent = 3

class swPropertyManagerPageControlType_e(IntEnum):
    """swPropertyManagerPageControlType_e (15 constants, from SwConst)."""
    swControlType_Label = 1
    swControlType_Checkbox = 2
    swControlType_Button = 3
    swControlType_Option = 4
    swControlType_Textbox = 5
    swControlType_Listbox = 6
    swControlType_Combobox = 7
    swControlType_Numberbox = 8
    swControlType_Selectionbox = 9
    swControlType_ActiveX = 10
    swControlType_BitmapButton = 11
    swControlType_CheckableBitmapButton = 12
    swControlType_Slider = 13
    swControlType_Bitmap = 14
    swControlType_WindowFromHandle = 15

class swPropertyManagerPageCursors_e(IntEnum):
    """swPropertyManagerPageCursors_e (3 constants, from SwConst)."""
    swPropertyManagerPageCursors_None = 0
    swPropertyManagerPageCursors_Okay = 1
    swPropertyManagerPageCursors_Advance = 2

class swPropertyManagerPageMessageExpanded(IntEnum):
    """swPropertyManagerPageMessageExpanded (3 constants, from SwConst)."""
    swMessageBoxMaintainExpandState = 0
    swMessageBoxExpand = 1
    swMessageBoxCompress = 2

class swPropertyManagerPageMessageVisibility(IntEnum):
    """swPropertyManagerPageMessageVisibility (4 constants, from SwConst)."""
    swNoMessageBox = 1
    swMessageBoxHidden = 2
    swMessageBoxVisible = 3
    swImportantMessageBox = 4

class swPropertyManagerPageOptions_e(IntEnum):
    """swPropertyManagerPageOptions_e (19 constants, from SwConst)."""
    swPropertyManagerOptions_OkayButton = 1
    swPropertyManagerOptions_CancelButton = 2
    swPropertyManagerOptions_LockedPage = 4
    swPropertyManagerOptions_CloseDialogButton = 8
    swPropertyManagerOptions_MultiplePages = 16
    swPropertyManagerOptions_PushpinButton = 32
    swPropertyManagerOptions_AllowHorizontalResize = 64
    swPropertyManagerOptions_PreviewButton = 128
    swPropertyManagerOptions_DisableSelection = 256
    swPropertyManagerOptions_WhatsNew = 512
    swPropertyManagerOptions_AbortCommands = 1024
    swPropertyManagerOptions_UndoButton = 2048
    swPropertyManagerOptions_CanEscapeCancel = 4096
    swPropertyManagerOptions_HandleKeystrokes = 8192
    swPropertyManagerOptions_RedoButton = 16384
    swPropertyManagerOptions_DisablePageBuildDuringHandlers = 32768
    swPropertyManagerOptions_GrayOutDisabledSelectionListboxes = 65536
    swPropertyManagerOptions_SupportsChainSelection = 131072
    swPropertyManagerOptions_SupportsIsolate = 262144

class swPropertyManagerPageShowOptions_e(IntEnum):
    """swPropertyManagerPageShowOptions_e (1 constants, from SwConst)."""
    swPropertyManagerShowOptions_StackPage = 1

class swPropertyManagerPageStatus_e(IntEnum):
    """swPropertyManagerPageStatus_e (4 constants, from SwConst)."""
    swPropertyManagerPage_Okay = 0
    swPropertyManagerPage_UnsupportedHandler = 1
    swPropertyManagerPage_CreationFailure = -1
    swPropertyManagerPage_NoDocument = -2

class swPropertyManagerStatus_e(IntEnum):
    """swPropertyManagerStatus_e (3 constants, from SwConst)."""
    swPropertyManagerStatus_Okay = 0
    swPropertyManagerStatus_Failed = -1
    swPropertyManagerStatus_Disconnected = -2

class swPropertySheetNotify_e(IntEnum):
    """swPropertySheetNotify_e (5 constants, from SwConst)."""
    swPropertySheetDestroyNotify = 1
    swPropertySheetHelpNotify = 2
    swPropertySheetOnOKNotify = 3
    swPropertySheetOnCancelNotify = 4
    swPropertySheetCreateControlNotify = 5

class swPublishStepOpts_e(IntEnum):
    """swPublishStepOpts_e (3 constants, from SwConst)."""
    swPublishStepOpts_None = 0
    swPublishStepOpts_SplitFacesSTEP242 = 1
    swPublishStepOpts_FaceEdgeSTEP242 = 2

class swPublishTo3DPDFError_e(IntEnum):
    """swPublishTo3DPDFError_e (7 constants, from SwConst)."""
    swPublishTo3DPDF_Success = 0
    swPublishTo3DPDF_InvalidPath = 1
    swPublishTo3DPDF_InvalidTheme = 2
    swPublishTo3DPDF_UnknownError = 3
    swPublishTo3DPDF_MBDLicenseNotAvailable = 4
    swPublishTo3DPDF_NothingToPublish = 5
    swPublishTo3DPDF_Step242EditionError = 6

class swPunchTableTagStyle_e(IntEnum):
    """swPunchTableTagStyle_e (2 constants, from SwConst)."""
    swPunchTable_AlphaNumericTags = 1
    swPunchTable_NumericTags = 2

class swQuadant_e(IntEnum):
    """swQuadant_e (5 constants, from SwConst)."""
    swQuadUnknown = 0
    swQuadPosQ1 = 1
    swQuadNegQ1 = 2
    swQuadPosQ2 = 3
    swQuadNegQ2 = 4

class swQuickTipMode_e(IntEnum):
    """swQuickTipMode_e (24 constants, from SwConst)."""
    swQuickTipNoMode = 0
    swQuickTipEmptySWFrameMode = 1
    swQuickTipEmptyPartMode = 2
    swQuickTipSketchingMode = 4
    swQuickTipClosedProfileCompletedMode = 8
    swQuickTipSketchDoneMode = 16
    swQuickTipFirstFeatureDoneMode = 32
    swQuickTipEmptyAssemblyMode = 64
    swQuickTipAssemblyOneCompMode = 128
    swQuickTipAssemblyMultiCompMode = 256
    swQuickTipAssemblyMatedMode = 512
    swQuickTipAssemblySimulatingMode = 1024
    swQuickTipEmptyDrawingMode = 2048
    swQuickTipDrawingOneViewMode = 4096
    swQuickTipPMBaseFeatureDialogMode = 8192
    swQuickTipPMYellowErrorMessageMode = 16384
    swQuickTipPMMateDialogMode = 32768
    swQuickTipSheetMetalMode = 65536
    swQuickTipSketching3DMode = 131072
    swQuickTipDrawingEditSheetMode = 262144
    swQuickTipPMInsertModelViewMode = 524288
    swQuickTipPMInsertProjectedViewMode = 1048576
    swQuickTipPMInsertComponentMode = 2097152
    swQuickTipPMYellowGuidelinesMode = 4194304

class swQuickTipPointAt_e(IntEnum):
    """swQuickTipPointAt_e (37 constants, from SwConst)."""
    swQTPA_NONE = 0
    swQTPA_FilletFeature = 1
    swQTPA_RefPlanes = 3
    swQTPA_SheetMetalFeature = 18
    swQTPA_MateGroupFeature = 33
    swQTPA_MateFeature = 105
    swQTPA_ExtrudedCut = 52
    swQTPA_ExtrudedBoss = 53
    swQTPA_BaseExtrudeFeature = 54
    swQTPA_RevolvedCut = 57
    swQTPA_RevolvedBoss = 57
    swQTPA_BaseRevolvedFeature = 57
    swQTPA_FirstBodyFeature = 998
    swQTPA_LastBodyFeature = 999
    swQTPA_SketchFeature = 78
    swQTPA_Origin = 79
    swTPA_SheetFeature = 88
    swTPA_SheetFormat = 97
    swTPA_DwgViewFeature = 43
    swTPA_FeatureMgrTree = 100
    swTPA_SketchingDorito = 1000
    swTPA_OnScreenCancel = 1001
    swQTPA_Triad = 1002
    swQTPA_RollbackBar = 1003
    swQTPA_SheetMetalFlattenedFeature = 1004
    swQTPA_SheetMetalProcessedFeature = 1005
    swQTPA_AssemblyComponentFeature = 1006
    swQTPA_ArrowManipulator = 1007
    swQTPA_PropertyManager = 1008
    swQTPA_AssemblyComponentNonFixed = 1009
    swQTPA_MateOperationBar = 1010
    swQTPA_QTStatusBarButton = 1011
    swQTPA_Nothing_FloatTRGraphics = 1012
    swQTPA_ConstraintStatusBarButton = 1013
    swQTPA_ChangedFilesStatusBarButton = 1014
    swQTPA_PM_MSG_DIVIDER = 5085
    swQTPA_UpperAppFrame = 387099

class swRackPinionMateDistanceOptions_e(IntEnum):
    """swRackPinionMateDistanceOptions_e (2 constants, from SwConst)."""
    swPinionPitchDiameter = 0
    swRackTravelPerRevolution = 1

class swRackPinionMateEntityType_e(IntEnum):
    """swRackPinionMateEntityType_e (2 constants, from SwConst)."""
    swRackPinionMateEntityType_Rack = 0
    swRackPinionMateEntityType_Pinion = 1

class swRayPtsOpts_e(IntEnum):
    """swRayPtsOpts_e (4 constants, from SwConst)."""
    swRayPtsOptsNORMALS = 1
    swRayPtsOptsTOPOLS = 2
    swRayPtsOptsENTRY_EXIT = 4
    swRayPtsOptsUNBLOCK = 8

class swRayPtsResults_e(IntEnum):
    """swRayPtsResults_e (7 constants, from SwConst)."""
    swRayPtsResultsUnknown = 0
    swRayPtsResultsFACE = 1
    swRayPtsResultsSILHOUETTE = 2
    swRayPtsResultsEDGE = 4
    swRayPtsResultsVERTEX = 8
    swRayPtsResultsENTER = 16
    swRayPtsResultsEXIT = 32

class swRayTraceRenderImageFormat_e(IntEnum):
    """swRayTraceRenderImageFormat_e (18 constants, from SwConst)."""
    swImageFormat_FlexiblePrecision = 0
    swImageFormat_Targa = 1
    swImageFormat_WindowsBmp = 2
    swImageFormat_HDR = 3
    swImageFormat_JPEG2000 = 4
    swImageFormat_JPEG2000_16bit = 5
    swImageFormat_JPEG2000_16bit_Lossless = 6
    swImageFormat_JPEG = 7
    swImageFormat_PNG = 8
    swImageFormat_PNG_16bit = 9
    swImageFormat_SGI_RGB = 10
    swImageFormat_TIF = 11
    swImageFormat_TIF_16bit = 12
    swImageFormat_TIF_16bit_uncompr = 13
    swImageFormat_OpenEXR = 14
    swImageFormat_OpenEXR_32bit = 15
    swImageFormat_OpenEXR_TILED16bit = 16
    swImageFormat_OpenEXR_TILED32bit = 17

class swRayTraceRenderQuality_e(IntEnum):
    """swRayTraceRenderQuality_e (4 constants, from SwConst)."""
    swRenderQuality_Good = 0
    swRenderQuality_Better = 1
    swRenderQuality_Best = 2
    swRenderQuality_Maximum = 3

class swRayTraceRenderType_e(IntEnum):
    """swRayTraceRenderType_e (1 constants, from SwConst)."""
    swPhotoView = 1

class swRayTraceRenderingType_e(IntEnum):
    """swRayTraceRenderingType_e (2 constants, from SwConst)."""
    swRayTraceCartoon = 0
    swRayTraceContour = 1

class swRebuildOnActivation_e(IntEnum):
    """swRebuildOnActivation_e (3 constants, from SwConst)."""
    swUserDecision = 0
    swDontRebuildActiveDoc = 1
    swRebuildActiveDoc = 2

class swRebuildOptions_e(IntEnum):
    """swRebuildOptions_e (5 constants, from SwConst)."""
    swRebuildAll = 1
    swForceRebuildAll = 2
    swUpdateMates = 4
    swCurrentSheetDisp = 8
    swUpdateDirtyOnly = 16

class swRefAxisType_e(IntEnum):
    """swRefAxisType_e (5 constants, from SwConst)."""
    swAxisTypeOneLine = 0
    swAxisTypeTwoPlanes = 1
    swAxisTypeTwoPoints = 2
    swAxisTypeCylOrConeFace = 3
    swAxisTypePtAndPlane = 4

class swRefGeometryError_e(IntEnum):
    """swRefGeometryError_e (4 constants, from SwConst)."""
    swEdgeNotFound = -1
    swValidEdge = 0
    swNonlinearEdgeSelection = 1
    swInvalidEdgeSelection = 2

class swRefPlaneReferenceConstraints_e(IntEnum):
    """swRefPlaneReferenceConstraints_e (14 constants, from SwConst)."""
    swRefPlaneReferenceConstraint_Parallel = 1
    swRefPlaneReferenceConstraint_Perpendicular = 2
    swRefPlaneReferenceConstraint_Coincident = 4
    swRefPlaneReferenceConstraint_Distance = 8
    swRefPlaneReferenceConstraint_Angle = 16
    swRefPlaneReferenceConstraint_Tangent = 32
    swRefPlaneReferenceConstraint_Project = 64
    swRefPlaneReferenceConstraint_MidPlane = 128
    swRefPlaneReferenceConstraint_OptionFlip = 256
    swRefPlaneReferenceConstraint_OptionOriginOnCurve = 512
    swRefPlaneReferenceConstraint_OptionProjectToNearestLocation = 1024
    swRefPlaneReferenceConstraint_OptionProjectAlongSketchNormal = 2048
    swRefPlaneReferenceConstraint_ParallelToScreen = 4096
    swRefPlaneReferenceConstraint_OptionReferenceFlip = 8192

class swRefPlaneReferenceIndex_e(IntEnum):
    """swRefPlaneReferenceIndex_e (3 constants, from SwConst)."""
    swRefPlaneReference_First = 0
    swRefPlaneReference_Second = 1
    swRefPlaneReference_Third = 2

class swRefPlaneType_e(IntEnum):
    """swRefPlaneType_e (12 constants, from SwConst)."""
    swRefPlaneInvalid = 0
    swRefPlaneUndefined = 1
    swRefPlaneLinePoint = 2
    swRefPlaneThreePoint = 3
    swRefPlaneLineLine = 4
    swRefPlaneDistance = 5
    swRefPlaneParallel = 6
    swRefPlaneAngle = 7
    swRefPlaneNormal = 8
    swRefPlaneOnSurface = 9
    swRefPlaneSWStandard = 10
    swRefPlaneConstraintBase = 11

class swRefPointAlongCurveType_e(IntEnum):
    """swRefPointAlongCurveType_e (3 constants, from SwConst)."""
    swRefPointAlongCurveDistance = 0
    swRefPointAlongCurvePercentage = 1
    swRefPointAlongCurveEvenlyDistributed = 2

class swRefPointType_e(IntEnum):
    """swRefPointType_e (8 constants, from SwConst)."""
    swRefPointInvalid = 0
    swRefPointUndefined = 1
    swRefPointAlongCurve = 2
    swRefPointCenterEdge = 3
    swRefPointFaceCenter = 4
    swRefPointFaceVertexProjection = 5
    swRefPointIntersection = 6
    swRefPointSketchPoint = 7

class swReferencedFileStatus_e(IntEnum):
    """swReferencedFileStatus_e (2 constants, from SwConst)."""
    swReferencedFileStatus_FileOk = 0
    swReferencedFileStatus_InternalIdMismatch = 1

class swRegionType_e(IntEnum):
    """swRegionType_e (2 constants, from SwConst)."""
    swRegionTypeMargins = 0
    swRegionTypeSheet = 1

class swRelativeViewCreationDirection_e(IntEnum):
    """swRelativeViewCreationDirection_e (7 constants, from SwConst)."""
    swRelativeViewCreationDirection_FRONT = 0
    swRelativeViewCreationDirection_RIGHT = 1
    swRelativeViewCreationDirection_TOP = 2
    swRelativeViewCreationDirection_BACK = 3
    swRelativeViewCreationDirection_LEFT = 4
    swRelativeViewCreationDirection_BOTTOM = 5
    swRelativeViewCreationDirection_AUXILIARY = 6

class swReliefTearTypes_e(IntEnum):
    """swReliefTearTypes_e (2 constants, from SwConst)."""
    swReliefTearTypeRip = 1
    swReliefTearTypeExtend = 2

class swReloadTemplateResult_e(IntEnum):
    """swReloadTemplateResult_e (5 constants, from SwConst)."""
    swReloadTemplate_Success = 0
    swReloadTemplate_UnknownError = 1
    swReloadTemplate_FileNotFound = 2
    swReloadTemplate_CustomSheet = 3
    swReloadTemplate_ViewOnly = 4

class swRemainingDofs_e(IntEnum):
    """swRemainingDofs_e (5 constants, from SwConst)."""
    swRemainingDofs_Restricted = 0
    swRemainingDofs_Unrestricted = 1
    swRemainingDofs_Unavailable = 2
    swRemainingDofs_Failed = 3
    swRemainingDofs_RootComponent = 4

class swRemoveCommandGroupErrors(IntEnum):
    """swRemoveCommandGroupErrors (2 constants, from SwConst)."""
    swRemoveCommandGroup_Failed = 0
    swRemoveCommandGroup_Success = 1

class swRenameDocumentError_e(IntEnum):
    """swRenameDocumentError_e (20 constants, from SwConst)."""
    swRenameDocumentError_None = 0
    swRenameDocumentError_UnspecifiedInternalError = 1
    swRenameDocumentError_InvalidSelection = 2
    swRenameDocumentError_InvalidForDrawings = 3
    swRenameDocumentError_NoModelLoaded = 4
    swRenameDocumentError_ComponentNotResolved = 5
    swRenameDocumentError_LightWeightComponent = 6
    swRenameDocumentError_RoutingComponent = 7
    swRenameDocumentError_FileAlreadyExists = 8
    swRenameDocumentError_InvalidCharactersInName = 9
    swRenameDocumentError_InvalidVirtualComponent = 10
    swRenameDocumentError_NameTooLong = 11
    swRenameDocumentError_DocumentNameInUse = 12
    swRenameDocumentError_PendingNameAlreadyInUse = 13
    swRenameDocumentError_ReadOnlyDocument = 14
    swRenameDocumentError_DocumentNotSaved = 15
    swRenameDocumentError_VirtualComponent = 16
    swRenameDocumentError_NotAllowedWithPDM = 17
    swRenameDocumentError_ToolboxComponent = 18
    swRenameDocumentError_PatternedComponent = 19

class swRenameOptions_e(IntEnum):
    """swRenameOptions_e (2 constants, from SwConst)."""
    swRenameOption_Yes = 1
    swRenameOption_No = 2

class swRenamedDocumentFinalAction_e(IntEnum):
    """swRenamedDocumentFinalAction_e (3 constants, from SwConst)."""
    swRenamedDocumentFinalAction_Default = 0
    swRenamedDocumentFinalAction_Ok = 1
    swRenamedDocumentFinalAction_Cancel = 2

class swRenderMaterialBumpMap_e(IntEnum):
    """swRenderMaterialBumpMap_e (10 constants, from SwConst)."""
    swRenderMaterialBumpMapNone = 0
    swRenderMaterialBumpMapFrom_File = 1
    swRenderMaterialBumpMapCasting = 2
    swRenderMaterialBumpMapRough = 3
    swRenderMaterialBumpMapTread_Plate = 4
    swRenderMaterialBumpMapDimpled = 5
    swRenderMaterialBumpMapKnurled = 6
    swRenderMaterialBumpMapChips = 7
    swRenderMaterialBumpMapCircular = 8
    swRenderMaterialBumpMapRough_Smooth = 9

class swRenderMaterialColorForms_e(IntEnum):
    """swRenderMaterialColorForms_e (5 constants, from SwConst)."""
    swRenderMaterialColorFormsColor_Undefined = -1
    swRenderMaterialColorFormsImage = 0
    swRenderMaterialColorFormsOne_Color = 1
    swRenderMaterialColorFormsTwo_Colors = 2
    swRenderMaterialColorFormsThree_Colors = 3

class swRenderMaterialIlluminationTypes_e(IntEnum):
    """swRenderMaterialIlluminationTypes_e (21 constants, from SwConst)."""
    swRenderMaterialIlluminationTypes_illumination_undefined = -1
    swRenderMaterialIlluminationType_use_underlying_material = 0
    swRenderMaterialIlluminationTypes_constant = 1
    swRenderMaterialIlluminationType_matte = 2
    swRenderMaterialIlluminationTypes_plastic = 3
    swRenderMaterialIlluminationTypes_metal = 4
    swRenderMaterialIlluminationTypes_satin_finish = 5
    swRenderMaterialIlluminationTypes_mirror = 6
    swRenderMaterialIlluminationTypes_conductor = 7
    swRenderMaterialIlluminationTypes_translucent = 8
    swRenderMaterialIlluminationTypes_translucent_plastic = 9
    swRenderMaterialIlluminationTypes_anisotropic = 10
    swRenderMaterialIlluminationTypes_circular_anisotropic = 11
    swRenderMaterialIlluminationTypes_woven_anisotropic = 12
    swRenderMaterialIlluminationTypes_multilayer_paint = 13
    swRenderMaterialIlluminationTypes_glass = 14
    swRenderMaterialIlluminationTypes_dielectric = 15
    swRenderMaterialIlluminationTypes_dielectric_advanced = 16
    swRenderMaterialIlluminationTypes_cut_hole_with_decal = 17
    swRenderMaterialIlluminationTypes_studio_plastic = 18
    swRenderMaterialIlluminationTypes_car_paint = 19

class swRendererType_e(IntEnum):
    """swRendererType_e (2 constants, from SwConst)."""
    swRendererType_Solidworks_Screen = 0
    swRendererType_Photoworks_Buffer = 1

class swReorderComponentsWhere_e(IntEnum):
    """swReorderComponentsWhere_e (4 constants, from SwConst)."""
    swReorderComponents_After = 1
    swReorderComponents_Before = 2
    swReorderComponents_LastInFolder = 3
    swReorderComponents_FirstInFolder = 4

class swRepaintTypes_e(IntEnum):
    """swRepaintTypes_e (11 constants, from SwConst)."""
    swStandardUpdate = 0
    swLightUpdate = 1
    swMaterialUpdate = 2
    swSectionedUpdate = 3
    swExplodedUpdate = 4
    swInsertSketchUpdate = 5
    swViewDisplayUpdate = 6
    swDamageRepairUpdate = 7
    swSelectionUpdate = 8
    swSectionedExitUpdate = 9
    swScrollViewUpdate = 10

class swRepairSketchOption_e(IntEnum):
    """swRepairSketchOption_e (5 constants, from SwConst)."""
    swRepairSketchCleanup = 0
    swRepairSketchZeroSegment = 1
    swRepairSketchMergeSegment = 2
    swRepairSketchCloseGaps = 4
    swRepairSketchBreakIntersection = 8

class swReplaceComponentError_e(IntEnum):
    """swReplaceComponentError_e (8 constants, from SwConst)."""
    swReplaceComponent_Undefined = 0
    swReplaceComponent_Success = 1
    swReplaceComponent_EmptyName = 2
    swReplaceComponent_InvalidFileName = 3
    swReplaceComponent_SameModelDifferentPath = 4
    swReplaceComponent_SameFile = 5
    swReplaceComponent_NotTopLevelComponent = 6
    swReplaceComponent_UnknownError = 7

class swReplaceComponentsConfiguration_e(IntEnum):
    """swReplaceComponentsConfiguration_e (2 constants, from SwConst)."""
    swReplaceComponentsConfiguration_MatchName = 0
    swReplaceComponentsConfiguration_ManuallySelect = 1

class swReverseEndPointTangentResult_e(IntEnum):
    """swReverseEndPointTangentResult_e (3 constants, from SwConst)."""
    swReverseEndPointTangent_Success = 0
    swReverseEndPointTangent_InvalidSelection = 1
    swReverseEndPointTangent_ConstraintConflict = 2

class swRevisionCloudShape_e(IntEnum):
    """swRevisionCloudShape_e (4 constants, from SwConst)."""
    swRevisionCloudShape_Freehand = 0
    swRevisionCloudShape_Ellipse = 1
    swRevisionCloudShape_Rectangle = 2
    swRevisionCloudShape_Polygon = 3

class swRevisionTableMultipleSheetStyle_e(IntEnum):
    """swRevisionTableMultipleSheetStyle_e (3 constants, from SwConst)."""
    swRevisionTable_SeeSheet1 = 1
    swRevisionTable_LinkedToSheet1 = 2
    swRevisionTable_Independent = 3

class swRevisionTableSymbolShape_e(IntEnum):
    """swRevisionTableSymbolShape_e (4 constants, from SwConst)."""
    swRevisionTable_CircleSymbol = 1
    swRevisionTable_SquareSymbol = 2
    swRevisionTable_TriangleSymbol = 3
    swRevisionTable_HexagonSymbol = 4

class swRevisionTableTagStyle_e(IntEnum):
    """swRevisionTableTagStyle_e (2 constants, from SwConst)."""
    swRevisionTable_AlphabeticTags = 1
    swRevisionTable_NumericTags = 2

class swRevolveOptions_e(IntEnum):
    """swRevolveOptions_e (2 constants, from SwConst)."""
    swRevolveOptionsNone = 0
    swAutoCloseSketch = 1

class swRevolveType_e(IntEnum):
    """swRevolveType_e (6 constants, from SwConst)."""
    swRevolveTypeOneDirection = 0
    swRevolveTypeMidPlane = 1
    swRevolveTypeTwoDirection = 2
    swRevolveTypeOneDirection360Degrees = 3
    swRevolveTypeMidPlane360Degrees = 4
    swRevolveTypeTwoDirection360Degrees = 5

class swRibExtrusionDirection_e(IntEnum):
    """swRibExtrusionDirection_e (2 constants, from SwConst)."""
    swRibParallelToSketch = 0
    swRibNormalToSketch = 1

class swRibType_e(IntEnum):
    """swRibType_e (2 constants, from SwConst)."""
    swRibLinear = 0
    swRibNatural = 1

class swRotationAxisIndex_e(IntEnum):
    """swRotationAxisIndex_e (4 constants, from SwConst)."""
    swRotationAxisIndex_Unknown = -1
    swRotationAxisIndex_XYRing = 0
    swRotationAxisIndex_YZRing = 1
    swRotationAxisIndex_ZXRing = 2

class swRouteComponentTypeID_e(IntEnum):
    """swRouteComponentTypeID_e (34 constants, from SWRoutingLib)."""
    swRouteCompType_Unknown = 0
    swRouteCompType_Pipe = 1
    swRouteCompType_EndConnector = 2
    swRouteCompType_Flange = 3
    swRouteCompType_OLet = 4
    swRouteCompType_Tee = 5
    swRouteCompType_ReducingTee = 6
    swRouteCompType_Elbow = 7
    swRouteCompType_Reducer = 8
    swRouteCompType_EccentricReducer = 9
    swRouteCompType_Union = 10
    swRouteCompType_Adapter = 11
    swRouteCompType_Cross = 12
    swRouteCompType_ReducingCross = 13
    swRouteCompType_Clip = 14
    swRouteCompType_Support = 15
    swRouteCompType_Equipment = 16
    swRouteCompType_TeeAdapter = 17
    swRouteCompType_HybridComponents = 18
    swRouteCompType_FittingOther = 19
    swRouteCompType_Hanger = 20
    swRouteCompType_ConduitAdapter = 21
    swRouteCompType_Gasket = 22
    swRouteCompType_Valve = 23
    swRouteCompType_RibbonCable = 24
    swRouteCompType_Tube = 25
    swRouteCompType_Conduit = 26
    swRouteCompType_Splice = 27
    swRouteCompType_ConduitElbow = 28
    swRouteCompType_AssemblyFittings = 29
    swRouteCompType_CableTray = 30
    swRouteCompType_DuctingTrunking = 31
    swRouteCompType_FlexCableConnector = 32
    swRouteCompType_Nipple = 33

class swRouteType_e(IntEnum):
    """swRouteType_e (1 constants, from SWRoutingLib)."""
    swRouteType_Electrical = 2

class swRoutingComponentGroupingOption_e(IntEnum):
    """swRoutingComponentGroupingOption_e (4 constants, from SwConst)."""
    swShowOnlyRoutingComponentsInBOM = 1
    swGroupPipesOrTubesWithTheSameDiameterAndSchedule = 2
    swDisplayUnitsInBOM = 4
    swRoutingGroupSpoolComponents = 8

class swRoutingExportDataError_e(IntEnum):
    """swRoutingExportDataError_e (6 constants, from SWRoutingLib)."""
    swRoutingExportDataError_Success = 0
    swRoutingExportDataError_UnknownError = 1
    swRoutingExportDataError_IncorrectFilePath = 2
    swRoutingExportDataError_AssemblyTypeMismatch = 3
    swRoutingExportDataError_WrongUnit = 4
    swRoutingExportDataError_WrongType = 5

class swRoutingExportPipeDataError_e(IntEnum):
    """swRoutingExportPipeDataError_e (5 constants, from SWRoutingLib)."""
    swRoutingExportPipeDataError_Success = 0
    swRoutingExportPipeDataError_UnknownError = 1
    swRoutingExportPipeDataError_IncorrectFilePath = 2
    swRoutingExportPipeDataError_AssemblyTypeMismatch = 3
    swRoutingExportPipeDataError_WrongUnit = 4

class swRoutingFlattenConnectorOptions_e(IntEnum):
    """swRoutingFlattenConnectorOptions_e (2 constants, from SwConst)."""
    swDisplay3DConnectors_e = 1
    SwUseDrawingConnectorBlocks_e = 2

class swRoutingFlattenSegmentOrientation_e(IntEnum):
    """swRoutingFlattenSegmentOrientation_e (2 constants, from SwConst)."""
    swVertical_e = 1
    SwHorizontal_e = 2

class swRoutingFlattenTypes_e(IntEnum):
    """swRoutingFlattenTypes_e (2 constants, from SwConst)."""
    swAnnotation_e = 1
    SwManufacture_e = 2

class swRoutingSearchType_e(IntEnum):
    """swRoutingSearchType_e (8 constants, from SwConst)."""
    swRoutingConnectorSearch = 0
    swRoutingComponentSearch = 1
    swRoutingWireSearch = 2
    swRoutingCableSearch = 3
    swRoutingSignalSearch = 4
    swRoutingPipeSearch = 5
    swRoutingPipeSegmentSearch = 6
    swRoutingFittingSearch = 7

class swRuledSurfaceType_e(IntEnum):
    """swRuledSurfaceType_e (5 constants, from SwConst)."""
    swRuledSurfaceType_TangentToSurface = 1
    swRuledSurfaceType_NormalToSurface = 2
    swRuledSurfaceType_TaperedToVector = 3
    swRuledSurfaceType_PerpendicularToVector = 4
    swRuledSurfaceType_Sweep = 5

class swRunMacroError_e(IntEnum):
    """swRunMacroError_e (28 constants, from SwConst)."""
    swRunMacroError_InvalidArg = 1
    swRunMacroError_MacrosAreDisabled = 2
    swRunMacroError_NotInDesignMode = 3
    swRunMacroError_OnlyCodeModules = 4
    swRunMacroError_OutOfMemory = 5
    swRunMacroError_InvalidProcname = 6
    swRunMacroError_InvalidPropertyType = 7
    swRunMacroError_SuborfuncExpected = 8
    swRunMacroError_BadParmCount = 9
    swRunMacroError_BadVarType = 10
    swRunMacroError_UserInterrupt = 11
    swRunMacroError_Exception = 12
    swRunMacroError_Overflow = 13
    swRunMacroError_TypeMismatch = 14
    swRunMacroError_ParmNotOptional = 15
    swRunMacroError_UnknownLcid = 16
    swRunMacroError_Busy = 17
    swRunMacroError_ConnectionTerminated = 18
    swRunMacroError_CallRejected = 19
    swRunMacroError_CallFailed = 20
    swRunMacroError_Zombied = 21
    swRunMacroError_Invalidindex = 22
    swRunMacroError_NoPermission = 23
    swRunMacroError_Reverted = 24
    swRunMacroError_TooManyOpenFiles = 25
    swRunMacroError_DiskError = 26
    swRunMacroError_CantSave = 27
    swRunMacroError_OpenFileFailed = 28

class swRunMacroOption_e(IntEnum):
    """swRunMacroOption_e (2 constants, from SwConst)."""
    swRunMacroDefault = 0
    swRunMacroUnloadAfterRun = 1

class swSFLaySym_e(IntEnum):
    """swSFLaySym_e (8 constants, from SwConst)."""
    swSFNone = 0
    swSFCircular = 1
    swSFCross = 2
    swSFMultiDir = 3
    swSFParallel = 4
    swSFPerp = 5
    swSFRadial = 6
    swSFParticulate = 7

class swSFProfileDirection_e(IntEnum):
    """swSFProfileDirection_e (5 constants, from SwConst)."""
    swSFProfileDirectionNone = 0
    swSFProfileDirectionPerp = 1
    swSFProfileDirectionParallel = 2
    swSFProfileDirectionCircular = 3
    swSFProfileDirectionDefinedAngle = 4

class swSFSymType_e(IntEnum):
    """swSFSymType_e (10 constants, from SwConst)."""
    swSFBasic = 0
    swSFMachining_Req = 1
    swSFDont_Machine = 2
    swSFJIS_Surface_Texture_1 = 3
    swSFJIS_Surface_Texture_2 = 4
    swSFJIS_Surface_Texture_3 = 5
    swSFJIS_Surface_Texture_4 = 6
    swSFJIS_No_Machining = 7
    swSFJIS_Basic = 8
    swSFJIS_Machining_Req = 9

class swSMBendState_e(IntEnum):
    """swSMBendState_e (4 constants, from SwConst)."""
    swSMBendStateNone = 0
    swSMBendStateSharps = 1
    swSMBendStateFlattened = 2
    swSMBendStateFolded = 3

class swSMCommandStatus_e(IntEnum):
    """swSMCommandStatus_e (5 constants, from SwConst)."""
    swSMErrorNone = 0
    swSMErrorUnknown = 1
    swSMErrorNotAPart = 2
    swSMErrorNotASheetMetalPart = 3
    swSMErrorInvalidBendState = 4

class swSMGExportProfiles_e(IntEnum):
    """swSMGExportProfiles_e (3 constants, from SwConst)."""
    swSMGExportProfiles_Custom = 0
    swSMGExportProfiles_swDefault = 1
    swSMGExportProfiles_swWithSurfaceParts = 2

class swSMGRefineRelativeType_e(IntEnum):
    """swSMGRefineRelativeType_e (2 constants, from SwConst)."""
    swSMGRefineRelativeType_ChordalError = 0
    swSMGRefineRelativeType_NormalDeviation = 1

class swSMGRefinementType_e(IntEnum):
    """swSMGRefinementType_e (2 constants, from SwConst)."""
    swSMGRefinementType_Relative = 0
    swSMGRefinementType_Absolute = 1

class swSMNormalCutError_e(IntEnum):
    """swSMNormalCutError_e (5 constants, from SwConst)."""
    swSMNormalCutError_NoError = 0
    swSMNormalCutError_FaceAlreadyExists = 1
    swSMNormalCutError_InvalidFace = 2
    swSMNormalCutError_FaceNotPresent = 3
    swSMNormalCutError_InvalidFaceArray = 4

class swSTLQuality_e(IntEnum):
    """swSTLQuality_e (3 constants, from SwConst)."""
    swSTLQuality_Coarse = 1
    swSTLQuality_Fine = 2
    swSTLQuality_Custom = 3

class swSafeArrayType_e(IntEnum):
    """swSafeArrayType_e (11 constants, from SwConst)."""
    swWordArray = 2
    swLongArray = 3
    swDoubleArray = 5
    swBstrArray = 8
    swDispatchArray = 9
    swBooleanArray = 11
    swUnknownArray = 13
    swByteArray = 16
    swUnsignedByteArray = 17
    swLongLongArray = 20
    swUnsignedLongLongArray = 21

class swSameAs_Status_e(IntEnum):
    """swSameAs_Status_e (3 constants, from SwConst)."""
    swSameAs_NotImplemented = -1
    swSameAs_Same = 1
    swSameAs_Different = 0

class swSaveAVIImageSize_e(IntEnum):
    """swSaveAVIImageSize_e (8 constants, from SwMotionStudy)."""
    swImage_Custom = 0
    swImage_Screen = 1
    swImage_160x120 = 2
    swImage_320x200 = 3
    swImage_320x240 = 4
    swImage_512x384 = 5
    swImage_640x480 = 6
    swImage_800x600 = 7

class swSaveAsOptions_e(IntEnum):
    """swSaveAsOptions_e (13 constants, from SwConst)."""
    swSaveAsOptions_Silent = 1
    swSaveAsOptions_Copy = 2
    swSaveAsOptions_SaveReferenced = 4
    swSaveAsOptions_AvoidRebuildOnSave = 8
    swSaveAsOptions_UpdateInactiveViews = 16
    swSaveAsOptions_OverrideSaveEmodel = 32
    swSaveAsOptions_SaveEmodelData = 64
    swSaveAsOptions_DetachedDrawing = 128
    swSaveAsOptions_IgnoreBiography = 256
    swSaveAsOptions_CopyAndOpen = 512
    swSaveAsOptions_IncludeVirtualSubAsmComps = 1024
    swSaveAsOptions_ExportTo2DPdfFromInspection = 2048
    swSaveAsOptions_PropagateVisualProperties = 4096

class swSaveAsVersion_e(IntEnum):
    """swSaveAsVersion_e (5 constants, from SwConst)."""
    swSaveAsCurrentVersion = 0
    swSaveAsSW98plus = 1
    swSaveAsFormatProE = 2
    swSaveAsStandardDrawing = 3
    swSaveAsDetachedDrawing = 4

class swSaveAsmAsPartOptions_e(IntEnum):
    """swSaveAsmAsPartOptions_e (4 constants, from SwConst)."""
    swSaveAsmAsPart_AllComponents = 1
    swSaveAsmAsPart_ExteriorComponents = 2
    swSaveAsmAsPart_ExteriorFaces = 3
    swSaveAsmAsPart_UserDefinedComponents = 4

class swSaveItemsPathError_e(IntEnum):
    """swSaveItemsPathError_e (4 constants, from SwConst)."""
    swSaveItemsPathError_Succeeded = 0
    swSaveItemsPathError_ArraySizeNotMatching = 1
    swSaveItemsPathError_InvalidPath = 2
    swSaveItemsPathError_WrongComponentName = 3

class swSaveReminderIntervalMode_e(IntEnum):
    """swSaveReminderIntervalMode_e (2 constants, from SwConst)."""
    swSaveReminderIntervalMode_Changes = 1
    swSaveReminderIntervalMode_Minutes = 2

class swSaveRestoreSettingsResults_e(IntEnum):
    """swSaveRestoreSettingsResults_e (3 constants, from SwConst)."""
    swSaveRestoreSettingsSuccess = 0
    swSaveRestoreSettingsFailure_Generic = 1
    swSaveRestoreSettingsFailure_InvalidFilename = 2

class swSaveToVersion_e(IntEnum):
    """swSaveToVersion_e (3 constants, from SwConst)."""
    swSaveToVersion_DoNotUpgrade = 0
    swSaveToVersion_Penultimate = 1
    swSaveToVersion_Antepenultimate = 2

class swSaveWithReferencesOptions_e(IntEnum):
    """swSaveWithReferencesOptions_e (4 constants, from SwConst)."""
    swSaveWithReferencesOptions_None = 0
    swSaveWithReferencesOptions_IncludeVirtualComponents = 1
    swSaveWithReferencesOptions_IncludeToolBoxParts = 2
    swSaveWithReferencesOptions_IncludeBrokenReferences = 4

class swScaleType_e(IntEnum):
    """swScaleType_e (3 constants, from SwConst)."""
    swScaleAboutCentroid = 0
    swScaleAboutOrigin = 1
    swScaleAboutCoordinateSystem = 2

class swSceneBackgroundType_e(IntEnum):
    """swSceneBackgroundType_e (6 constants, from SwConst)."""
    swBackgroundType_None = 0
    swBackgroundType_Plain = 1
    swBackgroundType_Graduated = 2
    swBackgroundType_Image = 3
    swBackgroundType_UseEnvironment = 4
    swBackgroundType_Color = 5

class swSceneFloorAlign_e(IntEnum):
    """swSceneFloorAlign_e (4 constants, from SwConst)."""
    swSceneFloorAlign_VIEW = 0
    swSceneFloorAlign_XY = 1
    swSceneFloorAlign_YZ = 2
    swSceneFloorAlign_ZX = 3

class swScrewMateDistanceOptions_e(IntEnum):
    """swScrewMateDistanceOptions_e (2 constants, from SwConst)."""
    swRevolutionsPerUnitLength = 0
    swDistancePerRevolution = 1

class swSearchFolderTypes_e(IntEnum):
    """swSearchFolderTypes_e (1 constants, from SwConst)."""
    swDocumentType = 0

class swSearchIndexingPerformance_e(IntEnum):
    """swSearchIndexingPerformance_e (2 constants, from SwConst)."""
    swSearchIndexingPerformanceIndexOnlyWhenComputerIsIdle = 0
    swSearchIndexingPerformanceAlwaysIndex = 1

class swSecondaryMemberBetweenPointsDistanceFromEndType_e(IntEnum):
    """swSecondaryMemberBetweenPointsDistanceFromEndType_e (2 constants, from SwConst)."""
    swSecondaryMemberBetweenPointsDistanceFromEndType_Distance = 0
    swSecondaryMemberBetweenPointsDistanceFromEndType_LengthRatio = 1

class swSecondaryMemberUpToMembersDistanceFromEndType_e(IntEnum):
    """swSecondaryMemberUpToMembersDistanceFromEndType_e (2 constants, from SwConst)."""
    swSecondaryMemberUpToMembersDistanceFromEndType_Distance = 0
    swSecondaryMemberUpToMembersDistanceFromEndType_LengthRatio = 1

class swSecondaryMemberUpToMembersMemberPointParameters_e(IntEnum):
    """swSecondaryMemberUpToMembersMemberPointParameters_e (2 constants, from SwConst)."""
    swSecondaryMemberUpToMembersMemberPointParameters_PointMemberPair = 0
    swSecondaryMemberUpToMembersMemberPointParameters_FromPoint = 1

class swSeedAlignmentReferencePoint_e(IntEnum):
    """swSeedAlignmentReferencePoint_e (2 constants, from SwConst)."""
    swSeedAlignmentReferencePoint_BoundingBoxCenter = 0
    swSeedAlignmentReferencePoint_ComponentOrigin = 1

class swSelectOption_e(IntEnum):
    """swSelectOption_e (2 constants, from SwConst)."""
    swSelectOptionDefault = 0
    swSelectOptionExtensive = 1

class swSelectType_e(IntEnum):
    """swSelectType_e (149 constants, from SwConst)."""
    swSelNOTHING = 0
    swSelEDGES = 1
    swSelFACES = 2
    swSelVERTICES = 3
    swSelDATUMPLANES = 4
    swSelDATUMAXES = 5
    swSelDATUMPOINTS = 6
    swSelOLEITEMS = 7
    swSelATTRIBUTES = 8
    swSelSKETCHES = 9
    swSelSKETCHSEGS = 10
    swSelSKETCHPOINTS = 11
    swSelDRAWINGVIEWS = 12
    swSelGTOLS = 13
    swSelDIMENSIONS = 14
    swSelNOTES = 15
    swSelSECTIONLINES = 16
    swSelDETAILCIRCLES = 17
    swSelSECTIONTEXT = 18
    swSelSHEETS = 19
    swSelCOMPONENTS = 20
    swSelMATES = 21
    swSelBODYFEATURES = 22
    swSelREFCURVES = 23
    swSelEXTSKETCHSEGS = 24
    swSelEXTSKETCHPOINTS = 25
    swSelHELIX = 26
    swSelREFERENCECURVES = 26
    swSelREFSURFACES = 27
    swSelCENTERMARKS = 28
    swSelINCONTEXTFEAT = 29
    swSelMATEGROUP = 30
    swSelBREAKLINES = 31
    swSelINCONTEXTFEATS = 32
    swSelMATEGROUPS = 33
    swSelSKETCHTEXT = 34
    swSelSFSYMBOLS = 35
    swSelDATUMTAGS = 36
    swSelCOMPPATTERN = 37
    swSelWELDS = 38
    swSelCTHREADS = 39
    swSelDTMTARGS = 40
    swSelPOINTREFS = 41
    swSelDCABINETS = 42
    swSelEXPLVIEWS = 43
    swSelEXPLSTEPS = 44
    swSelEXPLLINES = 45
    swSelSILHOUETTES = 46
    swSelCONFIGURATIONS = 47
    swSelOBJHANDLES = 48
    swSelARROWS = 49
    swSelZONES = 50
    swSelREFEDGES = 51
    swSelREFFACES = 52
    swSelREFSILHOUETTE = 53
    swSelBOMS = 54
    swSelEQNFOLDER = 55
    swSelSKETCHHATCH = 56
    swSelIMPORTFOLDER = 57
    swSelVIEWERHYPERLINK = 58
    swSelMIDPOINTS = 59
    swSelCUSTOMSYMBOLS = 60
    swSelCOORDSYS = 61
    swSelDATUMLINES = 62
    swSelROUTECURVES = 63
    swSelBOMTEMPS = 64
    swSelROUTEPOINTS = 65
    swSelCONNECTIONPOINTS = 66
    swSelROUTESWEEPS = 67
    swSelPOSGROUP = 68
    swSelBROWSERITEM = 69
    swSelFABRICATEDROUTE = 70
    swSelSKETCHPOINTFEAT = 71
    swSelEMPTYSPACE = 72
    swSelCOMPSDONTOVERRIDE = 72
    swSelLIGHTS = 73
    swSelWIREBODIES = 74
    swSelSURFACEBODIES = 75
    swSelSOLIDBODIES = 76
    swSelFRAMEPOINT = 77
    swSelSURFBODIESFIRST = 78
    swSelMANIPULATORS = 79
    swSelPICTUREBODIES = 80
    swSelSOLIDBODIESFIRST = 81
    swSelHOLESERIES = 83
    swSelLEADERS = 84
    swSelSKETCHBITMAP = 85
    swSelDOWELSYMS = 86
    swSelEXTSKETCHTEXT = 88
    swSelBLOCKINST = 93
    swSelFTRFOLDER = 94
    swSelSKETCHREGION = 95
    swSelSKETCHCONTOUR = 96
    swSelBOMFEATURES = 97
    swSelANNOTATIONTABLES = 98
    swSelBLOCKDEF = 99
    swSelCENTERMARKSYMS = 100
    swSelSIMULATION = 101
    swSelSIMELEMENT = 102
    swSelCENTERLINES = 103
    swSelHOLETABLEFEATS = 104
    swSelHOLETABLEAXES = 105
    swSelWELDMENT = 106
    swSelSUBWELDFOLDER = 107
    swSelEXCLUDEMANIPULATORS = 111
    swSelREVISIONTABLE = 113
    swSelSUBSKETCHINST = 114
    swSelWELDMENTTABLEFEATS = 116
    swSelBODYFOLDER = 118
    swSelREVISIONTABLEFEAT = 119
    swSelSUBATOMFOLDER = 121
    swSelWELDBEADS = 122
    swSelEMBEDLINKDOC = 123
    swSelJOURNAL = 124
    swSelDOCSFOLDER = 125
    swSelCOMMENTSFOLDER = 126
    swSelCOMMENT = 127
    swSelSWIFTANNOTATIONS = 130
    swSelSWIFTFEATURES = 132
    swSelCAMERAS = 136
    swSelMATESUPPLEMENT = 138
    swSelANNOTATIONVIEW = 139
    swSelGENERALTABLEFEAT = 142
    swSelDISPLAYSTATE = 148
    swSelBELTCHAINFEATS = 149
    swSelSUBSKETCHDEF = 154
    swSelSWIFTSCHEMA = 159
    swSelTITLEBLOCK = 192
    swSelTITLEBLOCKTABLEFEAT = 206
    swSelOBJGROUP = 207
    swSelPLANESECTIONS = 219
    swSelCOSMETICWELDS = 220
    SwSelMAGNETICLINES = 225
    swSelPUNCHTABLEFEATS = 234
    swSelREVISIONCLOUDS = 240
    swSelBorder = 254
    swSelSELECTIONSETFOLDER = 258
    swSelSELECTIONSETNODE = 259
    swSelGRAPHICSBODY = 262
    swSelFACETS = 268
    swSelMESHFACETEDGES = 269
    swSelMESHFACETVERTICES = 270
    swSelMESHSOLIDBODIES = 274
    swSelADVSTRUCTMEMBER = 295
    swSelFAMILYTABLEFEAT = 316
    swSelFAMILYTABLE = 317
    swSelEVERYTHING = -3
    swSelLOCATIONS = -2
    swSelUNSUPPORTED = -1

class swSelectionMarkAction_e(IntEnum):
    """swSelectionMarkAction_e (4 constants, from SwConst)."""
    swSelectionMarkSet = 0
    swSelectionMarkAppend = 1
    swSelectionMarkRemove = 2
    swSelectionMarkClear = 3

class swSelectionReferenceTypes_e(IntEnum):
    """swSelectionReferenceTypes_e (7 constants, from SwConst)."""
    swReferenceTypeVertex = 1
    swReferenceTypeEdge = 2
    swReferenceTypeFace = 3
    swReferenceTypeRefSurface = 4
    swReferenceTypeRefPlan = 5
    swReferenceTypeSketchPoint = 6
    swReferenceTypeBody = 7

class swSensorAlertType_e(IntEnum):
    """swSensorAlertType_e (10 constants, from SwConst)."""
    swSensorAlert_GreaterThan = 0
    swSensorAlert_LessThan = 1
    swSensorAlert_Exactly = 2
    swSensorAlert_NotGreaterThan = 3
    swSensorAlert_NotLessThan = 4
    swSensorAlert_NotExactly = 5
    swSensorAlert_Between = 6
    swSensorAlert_NotBetween = 7
    swSensorAlert_True = 8
    swSensorAlert_False = 9

class swSensorType_e(IntEnum):
    """swSensorType_e (5 constants, from SwConst)."""
    swSensorSimulation = 0
    swSensorMassProperty = 1
    swSensorDimension = 2
    swSensorInterfaceDetection = 3
    swSensorProximity = 5

class swSetComponentIdentifierResult_e(IntEnum):
    """swSetComponentIdentifierResult_e (5 constants, from SwConst)."""
    swSetComponentIdentifierResult_Success = 0
    swSetComponentIdentifierResult_InvalidPrimary = 1
    swSetComponentIdentifierResult_InvalidSecondary = 2
    swSetComponentIdentifierResult_InvalidTertiary = 4
    swSetComponentIdentifierResult_BlockedBySystemOption = 8

class swSetComponentsAndTransformsStatus_e(IntEnum):
    """swSetComponentsAndTransformsStatus_e (3 constants, from SwConst)."""
    swSetComponentsAndTransforms_Failed = 0
    swSetComponentsAndTransforms_Succeeded = 1
    swSetComponentsAndTransforms_InvalidInput = 2

class swSetHelixRegionParameterStatus_e(IntEnum):
    """swSetHelixRegionParameterStatus_e (3 constants, from SwConst)."""
    swSetHelixRegionParam_Succeeded = 0
    swSetHelixRegionParam_Failed = 1
    swSetHelixRegionParam_InvalidInput = 2

class swSetRouteFixedLengthError_e(IntEnum):
    """swSetRouteFixedLengthError_e (7 constants, from SwConst)."""
    swSetRouteFixedLengthError_NoError = 0
    swSetRouteFixedLengthError_NotFixedLengthSegment = 1
    swSetRouteFixedLengthError_NotFlexible = 2
    swSetRouteFixedLengthError_NoProperty = 3
    swSetRouteFixedLengthError_SetLengthFailed = 4
    swSetRouteFixedLengthError_SelectionFailed = 5
    swSetRouteFixedLengthError_FailedMinBendRadius = 6

class swSetRoutePathForWireErrorType_e(IntEnum):
    """swSetRoutePathForWireErrorType_e (3 constants, from SWRoutingLib)."""
    swSetRoutePathSuccess = 0
    swSetRoutePathTooManyConnectorsSelected = 1
    swSetRoutePathFailed = 2

class swSetSectionLabelStatus_e(IntEnum):
    """swSetSectionLabelStatus_e (4 constants, from SwConst)."""
    swSetSectionLabel_DuplicateLabelFailure = -2
    swSetSectionLabel_Failure = -1
    swSetSectionLabel_Okay = 0
    swSetSectionLabel_DuplicateLabelWarning = 1

class swSetValueInConfiguration_e(IntEnum):
    """swSetValueInConfiguration_e (5 constants, from SwConst)."""
    swSetValue_NoConfiguration = -1
    swSetValue_UseCurrentSetting = 0
    swSetValue_InThisConfiguration = 1
    swSetValue_InAllConfigurations = 2
    swSetValue_InSpecificConfigurations = 3

class swSetValueReturnStatus_e(IntEnum):
    """swSetValueReturnStatus_e (6 constants, from SwConst)."""
    swSetValue_Successful = 0
    swSetValue_Failure = 1
    swSetValue_InvalidValue = 2
    swSetValue_DrivenDimension = 3
    swSetValue_ModelNotLoaded = 4
    swSetValue_FrozenFeatureOwner = 5

class swSheetMetalAutoReliefTypes_e(IntEnum):
    """swSheetMetalAutoReliefTypes_e (3 constants, from SwConst)."""
    swSheetMetalAutoReliefTypes_e_Rectangular = 1
    swSheetMetalAutoReliefTypes_e_Obround = 2
    swSheetMetalAutoReliefTypes_e_Tear = 3

class swSheetMetalBendNotesBorderSize_e(IntEnum):
    """swSheetMetalBendNotesBorderSize_e (7 constants, from SwConst)."""
    swSheetMetalBendNotesBorderSizeTightFit = 0
    swSheetMetalBendNotesBorderSizeOneCharacter = 1
    swSheetMetalBendNotesBorderSizeTwoCharacters = 2
    swSheetMetalBendNotesBorderSizeThreeCharacters = 3
    swSheetMetalBendNotesBorderSizeFourCharacters = 4
    swSheetMetalBendNotesBorderSizeFiveCharacters = 5
    swSheetMetalBendNotesBorderSizeUserDefined = 6

class swSheetMetalGussetProfileDimType_e(IntEnum):
    """swSheetMetalGussetProfileDimType_e (2 constants, from SwConst)."""
    swSheetMetalGussetProfileDimType_IndentDepth = 0
    swSheetMetalGussetProfileDimType_ProfileDimensions = 1

class swSheetMetalGussetProfileType_e(IntEnum):
    """swSheetMetalGussetProfileType_e (2 constants, from SwConst)."""
    swSheetMetalGussetProfileType_Rib = 0
    swSheetMetalGussetProfileType_Custom = 1

class swSheetMetalMBDBendNotesStyle_e(IntEnum):
    """swSheetMetalMBDBendNotesStyle_e (3 constants, from SwConst)."""
    swSheetMetalMBDBendNotesStyle_AboveBendLine = 0
    swSheetMetalMBDBendNotesStyle_BelowBendLine = 1
    swSheetMetalMBDBendNotesStyle_WithLeader = 2

class swSheetMetalModifierError_e(IntEnum):
    """swSheetMetalModifierError_e (6 constants, from SwConst)."""
    swSheetMetalModifierError_NoError = 0
    swSheetMetalModifierError_OldArchitecture = 1
    swSheetMetalModifierError_NotEnabledOnTemplate = 2
    swSheetMetalModifierError_InvalidProperty = 3
    swSheetMetalModifierError_UnspecifiedError = 4
    swSheetMetalModifierError_GaugeTablePathNotEmpty = 5

class swSheetMetalOverlapTypes_e(IntEnum):
    """swSheetMetalOverlapTypes_e (3 constants, from SwConst)."""
    swSheetMetalOverlapTypes_OpenButt = 0
    swSheetMetalOverlapTypes_Overlap = 1
    swSheetMetalOverlapTypes_Underlap = 2

class swSheetMetalOverrideDefaultParameters_e(IntEnum):
    """swSheetMetalOverrideDefaultParameters_e (3 constants, from SwConst)."""
    swSheetMetalOverrideDefaultParameters_BendParameters = 0
    swSheetMetalOverrideDefaultParameters_BendAllowance = 1
    swSheetMetalOverrideDefaultParameters_AutoRelief = 2

class swSheetMetalReliefTypes_e(IntEnum):
    """swSheetMetalReliefTypes_e (5 constants, from SwConst)."""
    swSheetMetalReliefRectangular = 1
    swSheetMetalReliefTear = 2
    swSheetMetalReliefObround = 3
    swSheetMetalReliefNone = 4
    swSheetMetalReliefTearBend = 5

class swSheetMetalRibGussetType_e(IntEnum):
    """swSheetMetalRibGussetType_e (2 constants, from SwConst)."""
    swSheetMetalRibGussetType_Rounded = 0
    swSheetMetalRibGussetType_Flat = 1

class swSheetPrintQuadrant_e(IntEnum):
    """swSheetPrintQuadrant_e (5 constants, from SwConst)."""
    swSheetPrintQuadNotSet = 0
    swSheetPrintQuadQ1 = 1
    swSheetPrintQuadQ2 = 2
    swSheetPrintQuadQ3 = 3
    swSheetPrintQuadQ4 = 4

class swSheetSewingError_e(IntEnum):
    """swSheetSewingError_e (5 constants, from SwConst)."""
    swSewingOk = 0
    swBadArgument = 1
    swUnspecifiedError = 2
    swSewingFailed = 3
    swSewingIncomplete = 4

class swSheetSewingOption_e(IntEnum):
    """swSheetSewingOption_e (3 constants, from SwConst)."""
    swSewToSolid = 0
    swSewToSheets = 1
    swSewToSolidOrSheets = 2

class swShowMessageBarResult_e(IntEnum):
    """swShowMessageBarResult_e (4 constants, from SwConst)."""
    swShowMessageBarResult_Shown = 0
    swShowMessageBarResult_DontShowAgain = 1
    swShowMessageBarResult_FailedInvalidDefinition = 2
    swShowMessageBarResult_FailedInvalidHandler = 3

class swShowNotificationResult_e(IntEnum):
    """swShowNotificationResult_e (4 constants, from SwConst)."""
    swShowNotificationResult_Shown = 0
    swShowNotificationResult_DontShowAgain = 1
    swShowNotificationResult_FailedInvalidDefinition = 2
    swShowNotificationResult_FailedInvalidHandler = 3

class swShutOffSurfaceFeatureStatus_e(IntEnum):
    """swShutOffSurfaceFeatureStatus_e (3 constants, from SwConst)."""
    STATUS_SHUTOFF_REDUNDANT = 1
    STATUS_SHUTOFF_COMPLETE = 2
    STATUS_SHUTOFF_INCOMPLETE = 3

class swShutOffSurfacePatchType_e(IntEnum):
    """swShutOffSurfacePatchType_e (3 constants, from SwConst)."""
    swPatchTypeNoFill = 0
    swPatchTypeContact = 1
    swPatchTypeTangent = 2

class swSimpleFilletPartialEdgeCondition_e(IntEnum):
    """swSimpleFilletPartialEdgeCondition_e (4 constants, from SwConst)."""
    swPartialEdgeNone = 0
    swPartialEdgeDistanceOffset = 1
    swPartialEdgePercentOffset = 2
    swPartialEdgeReferenceOffset = 3

class swSimpleFilletType_e(IntEnum):
    """swSimpleFilletType_e (3 constants, from SwConst)."""
    swConstRadiusFillet = 0
    swFaceFillet = 2
    swFullRoundFillet = 3

class swSimpleFilletWhichFaces_e(IntEnum):
    """swSimpleFilletWhichFaces_e (6 constants, from SwConst)."""
    swSimpleFilletSingleRadius = 0
    swFaceFilletSet1 = 1
    swFaceFilletSet2 = 2
    swFullRoundFilletSet1 = 3
    swFullRoundFilletCenterSet = 4
    swFullRoundFilletSet2 = 5

class swSimulationDamperType_e(IntEnum):
    """swSimulationDamperType_e (2 constants, from SwConst)."""
    swSimulationDamper_Linear = 0
    swSimulationDamper_Torsional = 1

class swSimulationForceActionType_e(IntEnum):
    """swSimulationForceActionType_e (2 constants, from SwConst)."""
    swSimulationForceAction_ActionOnly = 0
    swSimulationForceAction_ActionAndRecation = 1

class swSimulationForceFunctionType_e(IntEnum):
    """swSimulationForceFunctionType_e (5 constants, from SwConst)."""
    swSimulationForceFunction_Constant = 0
    swSimulationForceFunction_Step = 1
    swSimulationForceFunction_Harmonic = 2
    swSimulationForceFunction_Function = 3
    swSimulationForceFunction_Spline = 4

class swSimulationForceType_e(IntEnum):
    """swSimulationForceType_e (2 constants, from SwConst)."""
    swSimulationForce_LinearForce = 0
    swSimulationForce_Torque = 1

class swSimulationGravityAxisName_e(IntEnum):
    """swSimulationGravityAxisName_e (4 constants, from SwConst)."""
    swSimulationGravityAxis_Invalid = -1
    swSimulationGravityAxis_X = 0
    swSimulationGravityAxis_Y = 1
    swSimulationGravityAxis_Z = 2

class swSimulationMotorDriveType_e(IntEnum):
    """swSimulationMotorDriveType_e (3 constants, from SwConst)."""
    swSimulationMotorDrive_Displacement = 0
    swSimulationMotorDrive_Velocity = 1
    swSimulationMotorDrive_Acceleration = 2

class swSimulationMotorMotionType_e(IntEnum):
    """swSimulationMotorMotionType_e (5 constants, from SwConst)."""
    swSimulationMotorMotion_Constant = 0
    swSimulationMotorMotion_Step = 1
    swSimulationMotorMotion_Harmonic = 2
    swSimulationMotorMotion_Function = 3
    swSimulationMotorMotion_Spline = 4

class swSimulationMotorType_e(IntEnum):
    """swSimulationMotorType_e (2 constants, from SwConst)."""
    swSimulationLinearMotor = 0
    swSimulationRotaryMotor = 1

class swSimulationSpringType_e(IntEnum):
    """swSimulationSpringType_e (2 constants, from SwConst)."""
    swSimulationSpring_Linear = 0
    swSimulationSpring_Torsional = 1

class swSkInternalPntOpts_e(IntEnum):
    """swSkInternalPntOpts_e (3 constants, from SwConst)."""
    swSkPntsOff = 0
    swSkPntsOn = 1
    swSkPntsDefault = 2

class swSkOffsetCapEndType_e(IntEnum):
    """swSkOffsetCapEndType_e (3 constants, from SwConst)."""
    swSkOffsetNoCaps = 0
    swSkOffsetArcCaps = 1
    swSkOffsetLineCaps = 2

class swSkOffsetMakeConstructionType_e(IntEnum):
    """swSkOffsetMakeConstructionType_e (4 constants, from SwConst)."""
    swSkOffsetDontMakeConstruction = 0
    swSkOffsetMakeOrigConstruction = 1
    swSkOffsetMakeOffsConstruction = 2
    swSkOffsetMakeBothConstruction = 3

class swSketchChamferType_e(IntEnum):
    """swSketchChamferType_e (3 constants, from SwConst)."""
    swSketchChamfer_DistanceAngle = 0
    swSketchChamfer_DistanceDistance = 1
    swSketchChamfer_DistanceEqual = 2

class swSketchCheckFeatureProfileUsage_e(IntEnum):
    """swSketchCheckFeatureProfileUsage_e (24 constants, from SwConst)."""
    swSketchCheckFeature_UNSET = 0
    swSketchCheckFeature_BASEEXTRUDE = 1
    swSketchCheckFeature_BASEEXTRUDETHIN = 2
    swSketchCheckFeature_BOSSEXTRUDE = 3
    swSketchCheckFeature_BOSSEXTRUDETHIN = 4
    swSketchCheckFeature_SURFACEEXTRUDE = 5
    swSketchCheckFeature_BASEREVOLVE = 6
    swSketchCheckFeature_BASEREVOLVETHIN = 7
    swSketchCheckFeature_BOSSREVOLVE = 8
    swSketchCheckFeature_BOSSREVOLVETHIN = 9
    swSketchCheckFeature_SURFACEREVOLVE = 10
    swSketchCheckFeature_CUTEXTRUDE = 11
    swSketchCheckFeature_CUTEXTRUDETHIN = 12
    swSketchCheckFeature_CUTREVOLVE = 13
    swSketchCheckFeature_CUTREVOLVETHIN = 14
    swSketchCheckFeature_SWEEPSECTION = 15
    swSketchCheckFeature_SURFACESWEEPSECTION = 16
    swSketchCheckFeature_SWEEPPATHORGUIDE = 17
    swSketchCheckFeature_LOFTSECTION = 18
    swSketchCheckFeature_SURFACELOFTSECTION = 19
    swSketchCheckFeature_LOFTGUIDE = 20
    swSketchCheckFeature_RIBSECTION = 21
    swSketchCheckFeature_SHEETMETAL_BASEFLANGE = 22
    swSketchCheckFeature_MOLD_PARTINGSURFACES = 23

class swSketchCheckFeatureStatus_e(IntEnum):
    """swSketchCheckFeatureStatus_e (25 constants, from SwConst)."""
    swSketchCheckFeatureStatus_UnknownError = -1
    swSketchCheckFeatureStatus_OK = 0
    swSketchCheckFeatureStatus_EntXEnt = 1
    swSketchCheckFeatureStatus_EntXSelf = 2
    swSketchCheckFeatureStatus_EntUnspecBad = 3
    swSketchCheckFeatureStatus_ThreeEnts = 4
    swSketchCheckFeatureStatus_EmptySketch = 5
    swSketchCheckFeatureStatus_WrongOpen = 6
    swSketchCheckFeatureStatus_WrongManyContours = 7
    swSketchCheckFeatureStatus_ZeroLengthEnt = 8
    swSketchCheckFeatureStatus_ManyOpen = 9
    swSketchCheckFeatureStatus_NoOpen = 10
    swSketchCheckFeatureStatus_MixedContours = 11
    swSketchCheckFeatureStatus_CturXCtur = 12
    swSketchCheckFeatureStatus_DisjCturs = 13
    swSketchCheckFeatureStatus_OpenWantClosed = 14
    swSketchCheckFeatureStatus_ClosedWantOpen = 15
    swSketchCheckFeatureStatus_DoubleContainment = 16
    swSketchCheckFeatureStatus_MoreThanOneContour = 17
    swSketchCheckFeatureStatus_OneOpenContourExpected = 18
    swSketchCheckFeatureStatus_OneClosedContourExpected = 19
    swSketchCheckFeatureStatus_WantSingleOpenOrMultiClosedDisjoint = 20
    swSketchCheckFeatureStatus_NeedsAxis = 21
    swSketchCheckFeatureStatus_OpenOrUnclear = 22
    swSketchCheckFeatureStatus_ContourIntersectsCenterLine = 23

class swSketchEntityType_e(IntEnum):
    """swSketchEntityType_e (6 constants, from SwConst)."""
    swSketchEntityPoint = 1
    swSketchEntityLine = 2
    swSketchEntityArc = 3
    swSketchEntityEllipse = 4
    swSketchEntityParabola = 5
    swSketchEntitySpline = 6

class swSketchFullyDefineRelationType_e(IntEnum):
    """swSketchFullyDefineRelationType_e (10 constants, from SwConst)."""
    swSketchFullyDefineRelationType_Equal = 1
    swSketchFullyDefineRelationType_Horizontal = 2
    swSketchFullyDefineRelationType_Vertical = 4
    swSketchFullyDefineRelationType_Tangent = 8
    swSketchFullyDefineRelationType_Perpendicular = 16
    swSketchFullyDefineRelationType_Colinear = 32
    swSketchFullyDefineRelationType_Concentric = 64
    swSketchFullyDefineRelationType_Parallel = 128
    swSketchFullyDefineRelationType_Midpoint = 256
    swSketchFullyDefineRelationType_Coincident = 512

class swSketchPictureTransparencyStyle_e(IntEnum):
    """swSketchPictureTransparencyStyle_e (4 constants, from SwConst)."""
    swSketchPictureTransparencyNone = 0
    swSketchPictureTransparencyFromFile = 1
    swSketchPictureTransparencyFullImage = 2
    swSketchPictureTransparencyUserDefined = 3

class swSketchPointType_e(IntEnum):
    """swSketchPointType_e (12 constants, from SwConst)."""
    swSketchPointType_Unknown = -1
    swSketchPointType_Internal = 0
    swSketchPointType_User = 1
    swSketchPointType_Spline = 2
    swSketchPointType_Datum = 3
    swSketchPointType_VirtualSharp = 4
    swSketchPointType_Parabola = 5
    swSketchPointType_MidPoint = 6
    swSketchPointType_FramePoint = 7
    swSketchPointType_Origin = 8
    swSketchPointType_Ellipse = 9
    swSketchPointType_External = 10

class swSketchRelationEntityTypes_e(IntEnum):
    """swSketchRelationEntityTypes_e (15 constants, from SwConst)."""
    swSketchRelationEntityType_Unknown = 0
    swSketchRelationEntityType_SubSketch = 1
    swSketchRelationEntityType_Point = 2
    swSketchRelationEntityType_Line = 3
    swSketchRelationEntityType_Arc = 4
    swSketchRelationEntityType_Ellipse = 5
    swSketchRelationEntityType_Parabola = 6
    swSketchRelationEntityType_Spline = 7
    swSketchRelationEntityType_Hatch = 8
    swSketchRelationEntityType_Text = 9
    swSketchRelationEntityType_Plane = 10
    swSketchRelationEntityType_Cylinder = 11
    swSketchRelationEntityType_Sphere = 12
    swSketchRelationEntityType_Surface = 13
    swSketchRelationEntityType_Dimension = 14

class swSketchRelationFilterType_e(IntEnum):
    """swSketchRelationFilterType_e (8 constants, from SwConst)."""
    swAll = 0
    swDangling = 1
    swOverDefining = 2
    swExternal = 3
    swDefinedInContext = 4
    swLocked = 5
    swBroken = 6
    swSelectedEntities = 7

class swSketchSegmentType_e(IntEnum):
    """swSketchSegmentType_e (2 constants, from SwConst)."""
    swSketchSegmentType_sketchpoints = 1
    swSketchSegmentType_sketchsegments = 2

class swSketchSegments_e(IntEnum):
    """swSketchSegments_e (6 constants, from SwConst)."""
    swSketchLINE = 0
    swSketchARC = 1
    swSketchELLIPSE = 2
    swSketchSPLINE = 3
    swSketchTEXT = 4
    swSketchPARABOLA = 5

class swSketchSlotCreationType_e(IntEnum):
    """swSketchSlotCreationType_e (4 constants, from SwConst)."""
    swSketchSlotCreationType_line = 0
    swSketchSlotCreationType_center_line = 1
    swSketchSlotCreationType_arc = 2
    swSketchSlotCreationType_3pointarc = 3

class swSketchSlotLengthType_e(IntEnum):
    """swSketchSlotLengthType_e (2 constants, from SwConst)."""
    swSketchSlotLengthType_CenterCenter = 0
    swSketchSlotLengthType_FullLength = 1

class swSketchTrimChoice_e(IntEnum):
    """swSketchTrimChoice_e (7 constants, from SwConst)."""
    swSketchTrimClosest = 0
    swSketchTrimCorner = 1
    swSketchTrimTwoEntities = 2
    swSketchTrimEntityPoint = 3
    swSketchTrimEntities = 4
    swSketchTrimOutside = 5
    swSketchTrimInside = 6

class swSlicingTypes_e(IntEnum):
    """swSlicingTypes_e (5 constants, from SwConst)."""
    swSlicingTypes_None = 0
    swSlicingTypes_Intersection = 1
    swSlicingTypes_Exact = 2
    swSlicingTypes_Circle = 4
    swSlicingTypes_Rectangle = 8

class swSlotMateConstraintOptions_e(IntEnum):
    """swSlotMateConstraintOptions_e (4 constants, from SwConst)."""
    swSlotMateConstraintOption_Free = 0
    swSlotMateConstraintOption_Centered = 1
    swSlotMateConstraintOption_Distance = 2
    swSlotMateConstraintOption_Percent = 3

class swSmartComponentSelectionTypes_e(IntEnum):
    """swSmartComponentSelectionTypes_e (2 constants, from SwConst)."""
    swSmartComponentFeatures = 1
    swSmartComponentComponents = 2

class swSmartDimensionDirection_e(IntEnum):
    """swSmartDimensionDirection_e (4 constants, from SwConst)."""
    swSmartDimensionDirection_Right = 0
    swSmartDimensionDirection_Up = 1
    swSmartDimensionDirection_Left = 2
    swSmartDimensionDirection_Down = 3

class swSolidBodiesDescriptionPropertyIndex(IntEnum):
    """swSolidBodiesDescriptionPropertyIndex (4 constants, from SwConst)."""
    swSolidBodiesDescriptionProp_None = 0
    swSolidBodiesDescriptionProp_Length = 1
    swSolidBodiesDescriptionProp_Thickness = 2
    swSolidBodiesDescriptionProp_Width = 3

class swSolidworksEditionOptions_e(IntEnum):
    """swSolidworksEditionOptions_e (7 constants, from SwConst)."""
    SolidworksUnknownEdition = 0
    SolidworksCommercialEdition = 1
    SolidworksEducationalEdition = 2
    SolidworksStudentEdition = 3
    SolidworksStudentDesignKitEdition = 4
    SolidworksPersonalEdition = 5
    SolidworksMakerEdition = 6

class swSolidworksWeldmentEndCondOptions_e(IntEnum):
    """swSolidworksWeldmentEndCondOptions_e (6 constants, from SwConst)."""
    swEndConditionNone = 0
    swEndConditionMiter = 1
    swEndConditionButt1 = 2
    swEndConditionButt2 = 3
    swEndConditionTrim = 4
    swEndConditionUseDefault = 5

class swSpecialMotionEventType_e(IntEnum):
    """swSpecialMotionEventType_e (1 constants, from SwMotionStudy)."""
    swSpecialMotionEventType_Contact = 1

class swSpeedpakUpdate_e(IntEnum):
    """swSpeedpakUpdate_e (3 constants, from SwConst)."""
    swSpeedpakUpdate_All = 0
    swSpeedpakUpdate_None = 1
    swSpeedpakUpdate_WithRebuildOnSaveMark = 2

class swSplitBodyType_e(IntEnum):
    """swSplitBodyType_e (3 constants, from SwConst)."""
    swSplitBodyType_e_Show = 0
    swSplitBodyType_e_Hide = 1
    swSplitBodyType_e_Consume = 2

class swSplitFaceOnParam_e(IntEnum):
    """swSplitFaceOnParam_e (2 constants, from SwConst)."""
    swSplitFaceOnParamU = 1
    swSplitFaceOnParamV = 2

class swSplitFacesOption_e(IntEnum):
    """swSplitFacesOption_e (2 constants, from SwConst)."""
    swSplitFacesAtPlusMinusDraftTransition = 0
    swSplitFacesAtSpecifiedAngle = 1

class swSplitLineFeatureType_e(IntEnum):
    """swSplitLineFeatureType_e (3 constants, from SwConst)."""
    swSplitLineFeatureType_Draft = 0
    swSplitLineFeatureType_Projection = 1
    swSplitLineFeatureType_Intersection = 2

class swSplitLineSplitSurfaceType_e(IntEnum):
    """swSplitLineSplitSurfaceType_e (2 constants, from SwConst)."""
    swSplitLineSplitSurfaceType_Natural = 0
    swSplitLineSplitSurfaceType_Linear = 1

class swSplitMemberDimensionType_e(IntEnum):
    """swSplitMemberDimensionType_e (2 constants, from SwConst)."""
    swSplitMemberDimensionType_SplitLength = 0
    swSplitMemberDimensionType_Instance = 1

class swSpringDefineType_e(IntEnum):
    """swSpringDefineType_e (3 constants, from SwConst)."""
    swSpringDefineType_PitchAndRevolution = 0
    swSpringDefineType_HeightAndRevolution = 1
    swSpringDefineType_HeightAndPitch = 2

class swSpringExtensionEndType_e(IntEnum):
    """swSpringExtensionEndType_e (3 constants, from SwConst)."""
    swSpringExtensionEndType_FullLoop = 0
    swSpringExtensionEndType_HalfLoop = 1
    swSpringExtensionEndType_UserDefined = 2

class swSpringProfileType_e(IntEnum):
    """swSpringProfileType_e (3 constants, from SwConst)."""
    swSpringProfileType_Circle = 0
    swSpringProfileType_Rectangle = 1
    swSpringProfileType_Trapezoid = 2

class swSpringTorsionEndType_e(IntEnum):
    """swSpringTorsionEndType_e (4 constants, from SwConst)."""
    swSpringTorsionEndType_Hook = 0
    swSpringTorsionEndType_Straight = 1
    swSpringTorsionEndType_Hinge = 2
    swSpringTorsionEndType_StraightOffset = 3

class swSpringType_e(IntEnum):
    """swSpringType_e (4 constants, from SwConst)."""
    swSpringType_Compression = 0
    swSpringType_Extension = 1
    swSpringType_Torsion = 2
    swSpringType_Spiral = 3

class swStackedBalloonDirection_e(IntEnum):
    """swStackedBalloonDirection_e (5 constants, from SwConst)."""
    swStackedBalloonDir_None = 0
    swStackedBalloonDir_Up = 1
    swStackedBalloonDir_Down = 2
    swStackedBalloonDir_Left = 3
    swStackedBalloonDir_Right = 4

class swStandardHeaderFooterPageSetupTexts_e(IntEnum):
    """swStandardHeaderFooterPageSetupTexts_e (5 constants, from SwConst)."""
    swHeaderFooterText_PageNumber = 1
    swHeaderFooterText_PageCount = 2
    swHeaderFooterText_Date = 3
    swHeaderFooterText_Time = 4
    swHeaderFooterText_Filename = 5

class swStandardViews_e(IntEnum):
    """swStandardViews_e (9 constants, from SwConst)."""
    swFrontView = 1
    swBackView = 2
    swLeftView = 3
    swRightView = 4
    swTopView = 5
    swBottomView = 6
    swIsometricView = 7
    swTrimetricView = 8
    swDimetricView = 9

class swStartConditions_e(IntEnum):
    """swStartConditions_e (4 constants, from SwConst)."""
    swStartSketchPlane = 0
    swStartSurface = 1
    swStartVertex = 2
    swStartOffset = 3

class swStep242Error_e(IntEnum):
    """swStep242Error_e (6 constants, from SwConst)."""
    swPublishStep242_Success = 0
    swPublishStep242_InvalidPath = 1
    swPublishStep242_UnknownError = 3
    swPublishStep242_MBDLicenseNotAvailable = 4
    swPublishStep242_EditionError = 5
    swPublishStep242_CustomPropertyError = 6

class swStopContinuePrompt_e(IntEnum):
    """swStopContinuePrompt_e (3 constants, from SwConst)."""
    swContinueResponse_Stop = 1
    swContinueResponse_Continue = 2
    swContinueResponse_Prompt = 3

class swStraightHoleClassificationType_e(IntEnum):
    """swStraightHoleClassificationType_e (4 constants, from SwConst)."""
    swStraightHoleClassificationType_Nominal = 0
    swStraightHoleClassificationType_Clearance = 1
    swStraightHoleClassificationType_Transitional = 2
    swStraightHoleClassificationType_Press = 3

class swStraightHoleFilter_e(IntEnum):
    """swStraightHoleFilter_e (6 constants, from SwConst)."""
    swStraightHoleFilter_All = 0
    swStraightHoleFilter_Nuts = 1
    swStraightHoleFilter_Fasteners = 2
    swStraightHoleFilter_Standoffs = 3
    swStraightHoleFilter_Studs = 4
    swStraightHoleFilter_Pins = 5

class swStraightHoleFitType_e(IntEnum):
    """swStraightHoleFitType_e (3 constants, from SwConst)."""
    swStraightHoleFitType_Close = 0
    swStraightHoleFitType_Normal = 1
    swStraightHoleFitType_Loose = 2

class swStraightTapHoleCustomSizing_e(IntEnum):
    """swStraightTapHoleCustomSizing_e (3 constants, from SwConst)."""
    swStraightTapHoleCustomSizing_TapDrillDiameter = 0
    swStraightTapHoleCustomSizing_TapDrillDiameterWithCosmeticThread = 1
    swStraightTapHoleCustomSizing_MajorDiameter = 2

class swStraightTapHoleEquation_e(IntEnum):
    """swStraightTapHoleEquation_e (4 constants, from SwConst)."""
    swStraightTapHoleEquation_Diameter = 0
    swStraightTapHoleEquation_DiameterAndHalf = 1
    swStraightTapHoleEquation_TwiceTheDiameter = 2
    swStraightTapHoleEquation_UserDefinedValue = 3

class swStraightTapHoleThreadClass_e(IntEnum):
    """swStraightTapHoleThreadClass_e (3 constants, from SwConst)."""
    swStraightTapHoleThreadClass_1B = 1
    swStraightTapHoleThreadClass_2B = 2
    swStraightTapHoleThreadClass_3B = 3

class swStructureProfileAlignmentType_e(IntEnum):
    """swStructureProfileAlignmentType_e (2 constants, from SwConst)."""
    swStructureProfileAlignmentType_HorizontalAxis = 0
    swStructureProfileAlignmentType_VerticalAxis = 1

class swStructureProfileMirrorType_e(IntEnum):
    """swStructureProfileMirrorType_e (2 constants, from SwConst)."""
    swStructureProfileMirrorType_HorizontalAxis = 0
    swStructureProfileMirrorType_VerticalAxis = 1

class swStructureProfilePiercePointType_e(IntEnum):
    """swStructureProfilePiercePointType_e (10 constants, from SwConst)."""
    swStructureProfilePiercePoint_Center = 0
    swStructureProfilePiercePoint_TopCenter = 1
    swStructureProfilePiercePoint_BottomCenter = 2
    swStructureProfilePiercePoint_TopLeft = 3
    swStructureProfilePiercePoint_TopRight = 4
    swStructureProfilePiercePoint_CenterLeft = 5
    swStructureProfilePiercePoint_CenterRight = 6
    swStructureProfilePiercePoint_BottomLeft = 7
    swStructureProfilePiercePoint_BottomRight = 8
    swStructureProfilePiercePoint_Selection = 9

class swStructureSplitMemberType_e(IntEnum):
    """swStructureSplitMemberType_e (2 constants, from SwConst)."""
    swStructureSplitMember_Reference = 0
    swStructureSplitMember_Dimension = 1

class swStructureSystemMemberCreationType_e(IntEnum):
    """swStructureSystemMemberCreationType_e (7 constants, from SwConst)."""
    swStructureSystemMemberCreationType_Primary_PathSegment = 0
    swStructureSystemMemberCreationType_Primary_RefPlane = 1
    swStructureSystemMemberCreationType_Primary_PointLength = 2
    swStructureSystemMemberCreationType_Primary_FacePlaneIntersection = 3
    swStructureSystemMemberCreationType_Secondary_SupportPlane = 4
    swStructureSystemMemberCreationType_Secondary_BetweenPoints = 5
    swStructureSystemMemberCreationType_Secondary_UpToMembers = 6

class swStructureSystemMemberType_e(IntEnum):
    """swStructureSystemMemberType_e (2 constants, from SwConst)."""
    swStructureSystemMemberType_Primary = 0
    swStructureSystemMemberType_Secondary = 1

class swStyleSplineCurveType_e(IntEnum):
    """swStyleSplineCurveType_e (4 constants, from SwConst)."""
    BezierCurve = 0
    BSpline_Degree3 = 1
    BSpline_Degree5 = 2
    BSpline_Degree7 = 3

class swSummInfoField_e(IntEnum):
    """swSummInfoField_e (10 constants, from SwConst)."""
    swSumInfoTitle = 0
    swSumInfoSubject = 1
    swSumInfoAuthor = 2
    swSumInfoKeywords = 3
    swSumInfoComment = 4
    swSumInfoSavedBy = 5
    swSumInfoCreateDate = 6
    swSumInfoSaveDate = 7
    swSumInfoCreateDate2 = 8
    swSumInfoSaveDate2 = 9

class swSunlightInfoType_e(IntEnum):
    """swSunlightInfoType_e (3 constants, from SwConst)."""
    swSunlight_Sunrise = 1
    swSunlight_Sunset = 2
    swSunlight_LengthOfDay = 3

class swSuppressDialog_e(IntEnum):
    """swSuppressDialog_e (3 constants, from SwConst)."""
    swSuppressDialog_None = 1
    swSuppressDialog_All = 2
    swSuppressDialog_LocateReference = 4

class swSuppressionError_e(IntEnum):
    """swSuppressionError_e (4 constants, from SwConst)."""
    swSuppressionBadComponent = 0
    swSuppressionBadState = 1
    swSuppressionChangeOk = 2
    swSuppressionChangeFailed = 3

class swSurfaceCutFeatureError_e(IntEnum):
    """swSurfaceCutFeatureError_e (3 constants, from SwConst)."""
    swSurfaceCutFeatureError_NoError = 0
    swSurfaceCutFeatureError_BodiesNotSpecified = 1
    swSurfaceCutFeatureError_InvalidVariant = 2

class swSurfaceExtendEndCond_e(IntEnum):
    """swSurfaceExtendEndCond_e (3 constants, from SwConst)."""
    swSurfaceExtendEndCondDistance = 0
    swSurfaceExtendEndCondUpToPoint = 1
    swSurfaceExtendEndCondUpToSurface = 2

class swSurfaceFinishSymbolOrientation_e(IntEnum):
    """swSurfaceFinishSymbolOrientation_e (5 constants, from SwConst)."""
    swSFOrientation_Upright = 1
    swSFOrientation_Rotated90 = 2
    swSFOrientation_Perpendicular = 3
    swSFOrientation_PerpendicularFlipped = 4
    swSFOrientation_UserDefined = 5

class swSurfaceFinishSymbolText_e(IntEnum):
    """swSurfaceFinishSymbolText_e (10 constants, from SwConst)."""
    swSFSymbolMaterialRemovalAllowance = 1
    swSFSymbolProductionMethod = 2
    swSFSymbolSamplingLength = 3
    swSFSymbolOtherRoughnessValue = 4
    swSFSymbolMaximumRoughness = 5
    swSFSymbolMinimumRoughness = 6
    swSFSymbolRoughnessSpacing = 7
    swSFSymbolRoughnessValue1 = 8
    swSFSymbolRoughnessValue2 = 9
    swSFSymbolRoughnessValue3 = 10

class swSurfaceTrimType_e(IntEnum):
    """swSurfaceTrimType_e (2 constants, from SwConst)."""
    swTypeTrimTool = 0
    swTypeMutualTrim = 1

class swSurfaceTypes_e(IntEnum):
    """swSurfaceTypes_e (10 constants, from SwConst)."""
    PLANE_TYPE = 4001
    CYLINDER_TYPE = 4002
    CONE_TYPE = 4003
    SPHERE_TYPE = 4004
    TORUS_TYPE = 4005
    BSURF_TYPE = 4006
    BLEND_TYPE = 4007
    OFFSET_TYPE = 4008
    EXTRU_TYPE = 4009
    SREV_TYPE = 4010

class swSustainabilityDurationType_e(IntEnum):
    """swSustainabilityDurationType_e (4 constants, from sustainabilityLib)."""
    swSustainabilityYear = 1
    swSustainabilityMonth = 2
    swSustainabilityDay = 3
    swSustainabilityHour = 4

class swSustainabilityEnergyType_e(IntEnum):
    """swSustainabilityEnergyType_e (7 constants, from sustainabilityLib)."""
    swSustainabilityNone = -1
    swSustainabilityElectricity = 0
    swSustainabilityNaturalGas = 1
    swSustainabilityDiesel = 2
    swSustainabilityGasoline = 3
    swSustainabilityKerosene = 4
    swSustainabilityLightFuelOil = 5

class swSustainabilityErrors_e(IntEnum):
    """swSustainabilityErrors_e (3 constants, from sustainabilityLib)."""
    swSustainabilityUnkownError = 0
    swSustainabilityNoData = 1
    swSustainabilityNoError = 2

class swSustainabilityFuelType_e(IntEnum):
    """swSustainabilityFuelType_e (3 constants, from sustainabilityLib)."""
    swSustainabilityFuelNone = -1
    swSustainabilityFuelElectricity = 0
    swSustainabilityFuelNaturalGas = 1

class swSustainabilityManufacturingPaintType_e(IntEnum):
    """swSustainabilityManufacturingPaintType_e (3 constants, from sustainabilityLib)."""
    swSustainabilityNoPaint = -1
    swSustainabilityWaterbasedPaint = 0
    swSustainabilitySolventbasedPaint = 1

class swSustainabilityManufacturingProcessType_e(IntEnum):
    """swSustainabilityManufacturingProcessType_e (11 constants, from sustainabilityLib)."""
    swSustainabilityCustom = 0
    swSustainabilityDieCasted = 1
    swSustainabilityExtrusion = 2
    swSustainabilityForged = 3
    swSustainabilityMachinedSandCasting = 4
    swSustainabilityMilled = 5
    swSustainabilityManufacturingNone = 6
    swSustainabilitySandCasted = 7
    swSustainabilitySheetmetal = 8
    swSustainabilityStamped_FormedSheetmetal = 9
    swSustainabilityTurned = 10

class swSustainabilityRegionName_e(IntEnum):
    """swSustainabilityRegionName_e (9 constants, from sustainabilityLib)."""
    swSustainabilityUnknownRegion = 0
    swSustainabilityNorthAmerica = 1
    swSustainabilityEurope = 2
    swSustainabilityAsia = 3
    swSustainabilityJapan = 4
    swSustainabilitySouthAmerica = 5
    swSustainabilityAustralia = 6
    swSustainabilityIndia = 7
    swSustainabilityNumElems = 8

class swSustainabilitySaveAsFileType_e(IntEnum):
    """swSustainabilitySaveAsFileType_e (3 constants, from sustainabilityLib)."""
    swSustainabilityDocxReport = 1
    swSustainabilitySpreadsheet = 2
    swSustainabilityGabiInputFile = 3

class swSweepDirection_e(IntEnum):
    """swSweepDirection_e (3 constants, from SwConst)."""
    swSweepDirection1 = 0
    swSweepBidirectional = 1
    swSweepDirection2 = 2

class swSweptFlangeError_e(IntEnum):
    """swSweptFlangeError_e (5 constants, from SwConst)."""
    swSweptFlangeError_None = 0
    swSweptFlangeError_InvalidProfile = 1
    swSweptFlangeError_InvalidPath = 2
    swSweptFlangeError_SelfIntersectingGeometry = 4
    swSweptFlangeError_InvalidSheetMetalParameters = 8

class swSweptFlangePositionTypes_e(IntEnum):
    """swSweptFlangePositionTypes_e (3 constants, from SwConst)."""
    swSweptFlangePositionType_MaterialInside = 1
    swSweptFlangePositionType_MaterialOutside = 2
    swSweptFlangePositionType_BendOutside = 3

class swSymbol_e(IntEnum):
    """swSymbol_e (8 constants, from SwConst)."""
    swSymNONE = 0
    swSymDEGREE = 32
    swSymPLUSMINUS = 33
    swSymCENTERLINE = 34
    swSymFREESTATE = 35
    swSymSTATISTICAL = 36
    swSymTANGENTPLANE = 37
    swSymCONTINUOUS = 38

class swSystemColorsCurrentColorScheme_e(IntEnum):
    """swSystemColorsCurrentColorScheme_e (3 constants, from SwConst)."""
    swSystemColorsCurrentColorSchemeBlueHighlight = 0
    swSystemColorsCurrentColorSchemeGreenHighlight = 1
    swSystemColorsCurrentColorSchemeOrangeHighlight = 2

class swSystemColorsEnvelopes_e(IntEnum):
    """swSystemColorsEnvelopes_e (3 constants, from SwConst)."""
    swSystemColorsEnvelopes_SemiTransparent = 0
    swSystemColorsEnvelopes_Opaque = 1
    swSystemColorsEnvelopes_DoNotChange = 2

class swSystemColorsIconColor_e(IntEnum):
    """swSystemColorsIconColor_e (2 constants, from SwConst)."""
    swSystemColorsIconColorDefault = 0
    swSystemColorsIconColorClassic = 1

class swSystemOptionDisplayAntiAliasing_e(IntEnum):
    """swSystemOptionDisplayAntiAliasing_e (3 constants, from SwConst)."""
    swSystemOptionDisplayAntiAliasing_None = 1
    swSystemOptionDisplayAntiAliasing_Edges = 2
    swSystemOptionDisplayAntiAliasing_FullScene = 3

class swTabEdgesType_e(IntEnum):
    """swTabEdgesType_e (3 constants, from SwConst)."""
    SharpEdge = 0
    FilletEdge = 1
    ChamferEdge = 2

class swTabSlotFeatureHeightType_e(IntEnum):
    """swTabSlotFeatureHeightType_e (3 constants, from SwConst)."""
    Blind = 0
    UpToSurface = 1
    OffsetFromSurface = 2

class swTabSlotFeatureSpacingType_e(IntEnum):
    """swTabSlotFeatureSpacingType_e (2 constants, from SwConst)."""
    EqualSpacing = 0
    SpacingLength = 1

class swTableAnnotationType_e(IntEnum):
    """swTableAnnotationType_e (11 constants, from SwConst)."""
    swTableAnnotation_General = 0
    swTableAnnotation_HoleChart = 1
    swTableAnnotation_BillOfMaterials = 2
    swTableAnnotation_RevisionBlock = 3
    swTableAnnotation_WeldmentCutList = 4
    swTableAnnotation_TitleBlock = 5
    swTableAnnotation_WeldTable = 6
    swTableAnnotation_BendTable = 7
    swTableAnnotation_PunchTable = 8
    swTableAnnotation_GeneralTolerance = 9
    swTableAnnotation_FamilyTable = 10

class swTableCellOrientation_e(IntEnum):
    """swTableCellOrientation_e (7 constants, from SwConst)."""
    swTableCellOrientation_Right = 0
    swTableCellOrientation_Left = 1
    swTableCellOrientation_Up = 2
    swTableCellOrientation_Down = 3
    swTableCellOrientation_Varies = 4
    swTableCellOrientation_Rotate90CW = 5
    swTableCellOrientation_Rotate90CCW = 6

class swTableCellRangeIdentifier_e(IntEnum):
    """swTableCellRangeIdentifier_e (2 constants, from SwConst)."""
    swTableCellRange_Current = -1
    swTableCellRange_All = -2

class swTableColumnTypes_e(IntEnum):
    """swTableColumnTypes_e (40 constants, from SwConst)."""
    swTableColumnType_UserDefined = 0
    swHoleTableColumnType_XLocation = 101
    swHoleTableColumnType_YLocation = 102
    swHoleTableColumnType_Tag = 103
    swHoleTableColumnType_Quantity = 104
    swHoleTableColumnType_Size = 105
    swBomTableColumnType_PartNumber = 201
    swBomTableColumnType_ItemNumber = 202
    swBomTableColumnType_Quantity = 203
    swBomTableColumnType_CustomProperty = 204
    swBomTableColumnType_UnitOfMeasure = 205
    swBomTableColumnType_Equation = 206
    swBomTableColumnType_ComponentReference = 207
    swBomTableColumnType_ToolboxProperty = 208
    swBomTableColumnType_CutListProperties = 209
    swBomTableColumnType_CutListItemName = 210
    swBomTableColumnType_PLMProperty = 211
    swRevisionTableColumnType_Zone = 301
    swRevisionTableColumnType_Revision = 302
    swRevisionTableColumnType_Description = 303
    swRevisionTableColumnType_Date = 304
    swRevisionTableColumnType_Approved = 305
    swRevisionTableColumnType_CustomProperties = 306
    swWeldTableColumnType_ItemNumber = 401
    swWeldTableColumnType_Quantity = 402
    swWeldTableColumnType_CutListName = 403
    swWeldTableColumnType_CustomProperty = 404
    swBendTableColumnType_Tag = 501
    swBendTableColumnType_Direction = 502
    swBendTableColumnType_Angle = 503
    swBendTableColumnType_InnerRadius = 504
    swBendTableColumnType_ComplementaryAngle = 505
    swBendTableColumnType_BendOrder = 506
    swBendTableColumnType_BendAllowance = 507
    swPunchTableColumnType_XLocation = 601
    swPunchTableColumnType_YLocation = 602
    swPunchTableColumnType_PunchID = 603
    swPunchTableColumnType_Quantity = 604
    swPunchTableColumnType_Angle = 605
    swPunchTableColumnType_Tag = 606

class swTableHeaderPosition_e(IntEnum):
    """swTableHeaderPosition_e (3 constants, from SwConst)."""
    swTableHeader_None = 0
    swTableHeader_Top = 1
    swTableHeader_Bottom = 2

class swTableItemInsertPosition_e(IntEnum):
    """swTableItemInsertPosition_e (5 constants, from SwConst)."""
    swTableItemInsertPosition_First = 1
    swTableItemInsertPosition_Before = 2
    swTableItemInsertPosition_After = 3
    swTableItemInsertPosition_Last = 4
    swTableItemMovePosition_Relative = 5

class swTableMergeLocations_e(IntEnum):
    """swTableMergeLocations_e (3 constants, from SwConst)."""
    swTableMerge_WithPrevious = 1
    swTableMerge_WithNext = 2
    swTableMerge_All = 3

class swTableRowColSizeChangeBehavior_e(IntEnum):
    """swTableRowColSizeChangeBehavior_e (3 constants, from SwConst)."""
    swTableRowColChange_TableSizeCanChange = 0
    swTableRowColChange_AbsorbedByNext = 1
    swTableRowColChange_AbsorbedByPrevious = 2

class swTableSplitDirection_e(IntEnum):
    """swTableSplitDirection_e (3 constants, from SwConst)."""
    swTableSplit_None = 0
    swTableSplit_Horizontal = 1
    swTableSplit_Vertical = 2

class swTableSplitLocations_e(IntEnum):
    """swTableSplitLocations_e (4 constants, from SwConst)."""
    swTableSplit_BeforeRow = 1
    swTableSplit_AfterRow = 2
    swTableSplit_BeforeColumn = 3
    swTableSplit_AfterColumn = 4

class swTableTagStyle_e(IntEnum):
    """swTableTagStyle_e (3 constants, from SwConst)."""
    swTable_AlphaNumericTags = 1
    swTable_NumericTags = 2
    swTable_ManualTags = 3

class swTangencyType_e(IntEnum):
    """swTangencyType_e (5 constants, from SwConst)."""
    swTangencyNone = 0
    swTangencyNormalToProfile = 1
    swTangencyDirectionVector = 2
    swTangencyAllFaces = 3
    swMinimumTwist = 10

class swTangentArcTypes_e(IntEnum):
    """swTangentArcTypes_e (4 constants, from SwConst)."""
    swForward = 1
    swLeft = 2
    swBack = 3
    swRight = 4

class swTangentMagnitudeDirection_e(IntEnum):
    """swTangentMagnitudeDirection_e (2 constants, from SwConst)."""
    swTangentMagnitudeDirection1 = 1
    swTangentMagnitudeDirection2 = 2

class swTaperedTapCustomSizing_e(IntEnum):
    """swTaperedTapCustomSizing_e (2 constants, from SwConst)."""
    swTaperedTapCustomSizing_MinorDiameterWithCosmeticThread = 1
    swTaperedTapCustomSizing_MajorDiameter = 2

class swTaperedTapThreadClass_e(IntEnum):
    """swTaperedTapThreadClass_e (2 constants, from SwConst)."""
    swTaperedTapThreadClass_1 = 1
    swTaperedTapThreadClass_2 = 2

class swTaskPaneBitmapsOptions_e(IntEnum):
    """swTaskPaneBitmapsOptions_e (6 constants, from SwConst)."""
    swTaskPaneBitmapsOptions_Close = 1
    swTaskPaneBitmapsOptions_Help = 2
    swTaskPaneBitmapsOptions_Ok = 3
    swTaskPaneBitmapsOptions_Next = 4
    swTaskPaneBitmapsOptions_Back = 5
    swTaskPaneBitmapsOptions_Options = 6

class swTaskPaneNotify_e(IntEnum):
    """swTaskPaneNotify_e (4 constants, from SwConst)."""
    swAppTaskPaneActivateNotify = 1
    swAppTaskPaneDeactivateNotify = 2
    swAppTaskPaneDestroyNotify = 3
    swAppTaskPaneToolbarButtonClicked = 4

class swTaskPaneTab_e(IntEnum):
    """swTaskPaneTab_e (6 constants, from SwConst)."""
    swDesignLibrary = 1
    swFileExplorer = 2
    swResources = 3
    swClipBoard = 4
    swCustomProps = 5
    swPnID = 6

class swTaskpaneViewStatus_e(IntEnum):
    """swTaskpaneViewStatus_e (3 constants, from SwConst)."""
    swTaskpaneView_Okay = 0
    swTaskpaneView_UnsupportedHandler = 1
    swTaskpaneView_CreationFailure = -1

class swTbCommand_e(IntEnum):
    """swTbCommand_e (6 constants, from SwConst)."""
    swTbCONTROL = -2
    swTbACTIVE = -1
    swTbNONE = 0
    swTbPART = 1
    swTbASSEMBLY = 2
    swTbDRAWING = 3

class swTbControlModes_e(IntEnum):
    """swTbControlModes_e (3 constants, from SwConst)."""
    swTbSTOP = 0
    swTbCONTINUE = 1
    swTbOleInplaceMode = 2

class swTbSaveModes_e(IntEnum):
    """swTbSaveModes_e (2 constants, from SwConst)."""
    swTbSAVE = 0
    swTbLOAD = 1

class swTempBodySelectOptions_e(IntEnum):
    """swTempBodySelectOptions_e (2 constants, from SwConst)."""
    swTempBodySelectOptionNone = 0
    swTempBodySelectable = 1

class swTesselationMatchType_e(IntEnum):
    """swTesselationMatchType_e (3 constants, from SwConst)."""
    swTesselationMatchFacetTopology = 0
    swTesselationMatchFacetGeometry = 1
    swTesselationMatchEdgeCurve = 2

class swTextAlignmentVertical_e(IntEnum):
    """swTextAlignmentVertical_e (3 constants, from SwConst)."""
    swTextAlignmentTop = 0
    swTextAlignmentMiddle = 1
    swTextAlignmentBottom = 2

class swTextInBoxStyle_e(IntEnum):
    """swTextInBoxStyle_e (3 constants, from SwConst)."""
    swTextInBoxStyleNone = 0
    swTextInBoxStyleWrap = 1
    swTextInBoxStyleFit = 2

class swTextJustification_e(IntEnum):
    """swTextJustification_e (4 constants, from SwConst)."""
    swTextJustificationNone = 0
    swTextJustificationLeft = 1
    swTextJustificationCenter = 2
    swTextJustificationRight = 3

class swTextPosition_e(IntEnum):
    """swTextPosition_e (6 constants, from SwConst)."""
    swUPPER_LEFT = 0
    swLOWER_LEFT = 1
    swCENTER = 2
    swUPPER_RIGHT = 3
    swLOWER_RIGHT = 4
    swUPPER_CENTER = 5

class swTextSize_e(IntEnum):
    """swTextSize_e (3 constants, from SwConst)."""
    swTextSize_Small = 0
    swTextSize_Medium = 1
    swTextSize_Large = 2

class swTextureRenderModes_e(IntEnum):
    """swTextureRenderModes_e (3 constants, from SwConst)."""
    swTextureRenderModeImage = 0
    swTextureRenderModeBlend = 1
    swTextureRenderModeLuminance = 2

class swThickenDirection_e(IntEnum):
    """swThickenDirection_e (3 constants, from SwConst)."""
    swThickenDirection_Side1 = 0
    swThickenDirection_Side2 = 1
    swThickenDirection_Both = 2

class swThickenThicknessType_e(IntEnum):
    """swThickenThicknessType_e (3 constants, from SwConst)."""
    swThickenSideOne = 0
    swThickenSideTwo = 1
    swThickenSideBoth = 2

class swThinWallType_e(IntEnum):
    """swThinWallType_e (4 constants, from SwConst)."""
    swThinWallOneDirection = 0
    swThinWallOppDirection = 1
    swThinWallMidPlane = 2
    swThinWallTwoDirection = 3

class swThreadEndCondition_e(IntEnum):
    """swThreadEndCondition_e (3 constants, from SwConst)."""
    swThreadEndCondition_Blind = 0
    swThreadEndCondition_Revolutions = 1
    swThreadEndCondition_UpToSelection = 2

class swThreadMethod_e(IntEnum):
    """swThreadMethod_e (2 constants, from SwConst)."""
    swThreadMethod_Cut = 0
    swThreadMethod_Extrude = 1

class swThreadMirrorType_e(IntEnum):
    """swThreadMirrorType_e (2 constants, from SwConst)."""
    swThreadMirrorType_Horizontally = 0
    swThreadMirrorType_Vertically = 1

class swTiffCompressionScheme_e(IntEnum):
    """swTiffCompressionScheme_e (3 constants, from SwConst)."""
    swTiffUncompressed = 0
    swTiffPackbitsCompression = 1
    swTiffGroup4FaxCompression = 2

class swTiffImageType_e(IntEnum):
    """swTiffImageType_e (4 constants, from SwConst)."""
    swTiffImageBlackAndWhite = 0
    swTiffImageRGB = 1
    swTiffImageGrayScale = 2
    swTiffImageRGBA = 3

class swTolType_e(IntEnum):
    """swTolType_e (13 constants, from SwConst)."""
    swTolNONE = 0
    swTolBASIC = 1
    swTolBILAT = 2
    swTolLIMIT = 3
    swTolSYMMETRIC = 4
    swTolMIN = 5
    swTolMAX = 6
    swTolMETRIC = 7
    swTolFIT = 7
    swTolFITWITHTOL = 8
    swTolFITTOLONLY = 9
    swTolBLOCK = 10
    swTolGeneral = 11

class swToleranceZoneModifier_e(IntEnum):
    """swToleranceZoneModifier_e (4 constants, from SwConst)."""
    swToleranceZoneModifier_None = 0
    swToleranceZoneModifier_Unknown = 1
    swToleranceZoneModifier_Diameter = 2
    swToleranceZoneModifier_SphericalDiameter = 3

class swTolerances_e(IntEnum):
    """swTolerances_e (6 constants, from SwConst)."""
    swBSCurveOutputTol = 0
    swBSCurveNonRationalOutputTol = 1
    swUVCurveOutputTol = 2
    swSurfChordTessellationTol = 3
    swSurfAngularTessellationTol = 4
    swCurveChordTessellationTol = 5

class swToolBoxPartType_e(IntEnum):
    """swToolBoxPartType_e (3 constants, from SwConst)."""
    swNotAToolboxPart = 0
    swToolboxStandardPart = 1
    swToolboxCopiedPart = 2

class swToolBoxPropertyName_e(IntEnum):
    """swToolBoxPropertyName_e (3 constants, from SwConst)."""
    swToolBoxPropertyName_PartName = 0
    swToolBoxPropertyName_Specification = 1
    swToolBoxPropertyName_Standard = 2

class swToolbarDockStatePosition_e(IntEnum):
    """swToolbarDockStatePosition_e (6 constants, from SwConst)."""
    swDockNoToolbar = -1
    swNoDock = 0
    swDockTop = 1
    swDockBottom = 2
    swDockRight = 3
    swDockLeft = 4

class swToolbarLayoutOption_e(IntEnum):
    """swToolbarLayoutOption_e (3 constants, from SwConst)."""
    swToolbarLayoutOption_None = 0
    swToolbarLayoutOption_AllToolbars = 1
    swToolbarLayoutOption_MacroToolbarOnly = 2

class swToolbarStates_e(IntEnum):
    """swToolbarStates_e (1 constants, from SwConst)."""
    swToolbarHidden = 0

class swToolbar_e(IntEnum):
    """swToolbar_e (45 constants, from SwConst)."""
    swSketchToolsToolbar = 0
    swMainToolbar = 1
    swStandardToolbar = 2
    swViewToolbar = 3
    swSketchRelationsToolbar = 4
    swMacroToolbar = 5
    swSketchToolbar = 6
    swAssemblyToolbar = 7
    swDrawingToolbar = 8
    swAnnotationToolbar = 9
    swWebToolbar = 10
    swFeatureToolbar = 11
    swFontToolbar = 12
    swLineToolbar = 13
    swSelectionFilterToolbar = 14
    swReferenceGeometryToolbar = 15
    swStandardViewsToolbar = 16
    swToolsToolbar = 17
    swCurvesToolbar = 18
    swMoldToolsToolbar = 19
    swSheetMetalToolbar = 20
    swSurfacesToolbar = 21
    swAlignToolbar = 22
    swLayerToolbar = 23
    sw2Dto3DToolbar = 24
    swRoutingToolbar = 25
    swSimulationToolbar = 26
    swSplineToolbar = 27
    swContextToolbar = 28
    swBlocksToolbar = 29
    swTaskPaneToolbar = 30
    swQuickSnapToolbar = 31
    swOfficeToolbar = 32
    swTolXpertToolbar = 33
    swDimXpertToolbar = 33
    swTableToolbar = 34
    swWeldmentToolbar = 35
    swAnimationPaneToolbar = 36
    swScreenCaptureToolbar = 37
    swLayoutToolbar = 38
    swRenderToolbar = 39
    swSheetFormatToolbar = 40
    swConfigurationToolbar = 41
    swDisplayStatesToolbar = 42
    swSOLIDWORKSMBDToolbars = 43

class swTopoEntity_e(IntEnum):
    """swTopoEntity_e (7 constants, from SwConst)."""
    swTopoVertex = 1
    swTopoEdge = 2
    swTopoLoop = 3
    swTopoFace = 4
    swTopoShell = 5
    swTopoBody = 6
    swTopoRegion = 7

class swTopologyTypes_e(IntEnum):
    """swTopologyTypes_e (3 constants, from SwConst)."""
    swTopologyNull = 0
    swTopologyCoEdge = 1
    swTopologyVertex = 2

class swTopology_e(IntEnum):
    """swTopology_e (4 constants, from SwConst)."""
    swTopoSolidBody = 1
    swTopoSheetBody = 2
    swTopoWireBody = 3
    swTopoMinimumBody = 4

class swTrackingIDError_e(IntEnum):
    """swTrackingIDError_e (6 constants, from SwConst)."""
    swTrackingIDError_NoError = 0
    swTrackingIDError_UnknownError = 1
    swTrackingIDError_InvalidTrackingCookie = 2
    swTrackingIDError_InvalidTrackingID = 3
    swTrackingIDError_UntrackableObject = 4
    swTrackingIDError_UntrackedObject = 5

class swTranslationNotifyOptions_e(IntEnum):
    """swTranslationNotifyOptions_e (1 constants, from SwConst)."""
    swTranslationNotifySilentMode = 1

class swTransparencyState_e(IntEnum):
    """swTransparencyState_e (3 constants, from SwConst)."""
    swTransparencyStateUnknown = -1
    swTransparencyStateTransparent = 0
    swTransparencyStateNonTransparent = 1

class swTreeControlItemType_e(IntEnum):
    """swTreeControlItemType_e (3 constants, from SwConst)."""
    swFeatureManagerItem_Unsupported = 0
    swFeatureManagerItem_Feature = 1
    swFeatureManagerItem_Component = 2

class swTriadManipulatorControlPoints_e(IntEnum):
    """swTriadManipulatorControlPoints_e (7 constants, from SwConst)."""
    swTriadManipulatorOrigin = 0
    swTriadManipulatorXAxis = 1
    swTriadManipulatorYAxis = 2
    swTriadManipulatorZAxis = 3
    swTriadManipulatorXYPlane = 4
    swTriadManipulatorYZPlane = 5
    swTriadManipulatorZXPlane = 6

class swTriadManipulatorDoNotShow_e(IntEnum):
    """swTriadManipulatorDoNotShow_e (11 constants, from SwConst)."""
    swTriadManipulatorShowAll = 0
    swTriadManipulatorDoNotShowOrigin = 1
    swTriadManipulatorDoNotShowXAxis = 2
    swTriadManipulatorDoNotShowYAxis = 4
    swTriadManipulatorDoNotShowZAxis = 8
    swTriadManipulatorDoNotShowXYPlane = 16
    swTriadManipulatorDoNotShowYZPlane = 32
    swTriadManipulatorDoNotShowZXPlane = 64
    swTriadManipulatorDoNotShowXYRING = 128
    swTriadManipulatorDoNotShowYZRING = 256
    swTriadManipulatorDoNotShowZXRING = 512

class swTrimToolMemberObjectType_e(IntEnum):
    """swTrimToolMemberObjectType_e (2 constants, from SwConst)."""
    swTrimToolMemberObjectType_swCornerMember = 0
    swTrimToolMemberObjectType_swCornerTreatmentFeature = 1

class swTwistControlType_e(IntEnum):
    """swTwistControlType_e (6 constants, from SwConst)."""
    swTwistControlFollowPath = 0
    swTwistControlKeepNormalConstant = 1
    swTwistControlFollowPathFirstGuideCurve = 2
    swTwistControlFollowFirstSecondGuideCurves = 3
    swTwistControlConstantTwistAlongPath = 8
    swTwistControlNormalConstantTwistAlongPath = 9

class swUIStates_e(IntEnum):
    """swUIStates_e (1 constants, from SwConst)."""
    swIsHiddenInFeatureMgr = 1

class swUnitSystem_e(IntEnum):
    """swUnitSystem_e (5 constants, from SwConst)."""
    swUnitSystem_CGS = 1
    swUnitSystem_MKS = 2
    swUnitSystem_IPS = 3
    swUnitSystem_Custom = 4
    swUnitSystem_MMGS = 5

class swUnitsDecimalRounding_e(IntEnum):
    """swUnitsDecimalRounding_e (4 constants, from SwConst)."""
    swUnitsDecimalRounding_HalfAway = 0
    swUnitsDecimalRounding_HalfTowards = 1
    swUnitsDecimalRounding_HalfToEven = 2
    swUnitsDecimalRounding_Truncate = 3

class swUnitsEnergyUnit_e(IntEnum):
    """swUnitsEnergyUnit_e (4 constants, from SwConst)."""
    swUnitsEnergyUnit_Joule = 1
    swUnitsEnergyUnit_Ergs = 2
    swUnitsEnergyUnit_BTU = 3
    swUnitsEnergyUnit_KilowattHour = 4

class swUnitsForce_e(IntEnum):
    """swUnitsForce_e (8 constants, from SwConst)."""
    swUnitsForce_Dynes = 1
    swUnitsForce_Millinewtons = 2
    swUnitsForce_Newtons = 3
    swUnitsForce_Kilonewtons = 4
    swUnitsForce_Meganewtons = 5
    swUnitsForce_Poundfeet = 6
    swUnitsForce_KgForce = 7
    swUnitsForce_OunceForce = 8

class swUnitsMassPropMass_e(IntEnum):
    """swUnitsMassPropMass_e (4 constants, from SwConst)."""
    swUnitsMassPropMass_Milligrams = 1
    swUnitsMassPropMass_Grams = 2
    swUnitsMassPropMass_Kilograms = 3
    swUnitsMassPropMass_Pounds = 4

class swUnitsMassPropVolume_e(IntEnum):
    """swUnitsMassPropVolume_e (21 constants, from SwConst)."""
    swUnitsMassPropVolume_Angstroms3 = 1
    swUnitsMassPropVolume_Nanometers3 = 2
    swUnitsMassPropVolume_Microns3 = 3
    swUnitsMassPropVolume_Millimeters3 = 4
    swUnitsMassPropVolume_Centimeters3 = 5
    swUnitsMassPropVolume_Meters3 = 6
    swUnitsMassPropVolume_Microinches3 = 7
    swUnitsMassPropVolume_Mils3 = 8
    swUnitsMassPropVolume_Inches3 = 9
    swUnitsMassPropVolume_Feet3 = 10
    swUnitsMassPropVolume_MicroLiters = 11
    swUnitsMassPropVolume_MilliLiters = 12
    swUnitsMassPropVolume_CentiLiters = 13
    swUnitsMassPropVolume_DeciLiters = 14
    swUnitsMassPropVolume_Liters = 15
    swUnitsMassPropVolume_HectoLiters = 16
    swUnitsMassPropVolume_USFluidOunce = 17
    swUnitsMassPropVolume_USPints = 18
    swUnitsMassPropVolume_USGallons = 19
    swUnitsMassPropVolume_IMPGallons = 20
    swUnitsMassPropVolume_IMPCubicYards = 21

class swUnitsPowerUnit_e(IntEnum):
    """swUnitsPowerUnit_e (3 constants, from SwConst)."""
    swUnitsPowerUnit_Watt = 1
    swUnitsPowerUnit_Horsepower = 2
    swUnitsPowerUnit_Kilowatt = 3

class swUnitsTimeUnit_e(IntEnum):
    """swUnitsTimeUnit_e (6 constants, from SwConst)."""
    swUnitsTimeUnit_Second = 1
    swUnitsTimeUnit_Millisecond = 2
    swUnitsTimeUnit_Minute = 3
    swUnitsTimeUnit_Hour = 4
    swUnitsTimeUnit_Microsecond = 5
    swUnitsTimeUnit_Nanosecond = 6

class swUpdateProgressError_e(IntEnum):
    """swUpdateProgressError_e (5 constants, from SwConst)."""
    swUpdateProgressError_UnknownError = 0
    swUpdateProgressError_Success = 1
    swUpdateProgressError_UserCancel = 2
    swUpdateProgressError_OutOfBounds = 3
    swUpdateProgressError_NotInitialized = 4

class swUserMessageBarResponseType_e(IntEnum):
    """swUserMessageBarResponseType_e (3 constants, from SwConst)."""
    swUserMessageBarResponseType_None = 0
    swUserMessageBarResponseType_Button = 1
    swUserMessageBarResponseType_Link = 2

class swUserMessageBarSeverity_e(IntEnum):
    """swUserMessageBarSeverity_e (4 constants, from SwConst)."""
    swUserMessageBarSeverity_Information = 0
    swUserMessageBarSeverity_Acknowledgement = 1
    swUserMessageBarSeverity_Warning = 2
    swUserMessageBarSeverity_Error = 3

class swUserNotificationPosition_e(IntEnum):
    """swUserNotificationPosition_e (5 constants, from SwConst)."""
    swUserNotificationPosition_Default = 0
    swUserNotificationPosition_TopCenter = 1
    swUserNotificationPosition_TopRight = 2
    swUserNotificationPosition_BottomCenter = 3
    swUserNotificationPosition_BottomRight = 4

class swUserNotificationResponseType_e(IntEnum):
    """swUserNotificationResponseType_e (3 constants, from SwConst)."""
    swUserNotificationResponseType_None = 0
    swUserNotificationResponseType_Button = 1
    swUserNotificationResponseType_Link = 2

class swUserNotificationSeverity_e(IntEnum):
    """swUserNotificationSeverity_e (4 constants, from SwConst)."""
    swUserNotificationSeverity_Information = 0
    swUserNotificationSeverity_Acknowledgement = 1
    swUserNotificationSeverity_Warning = 2
    swUserNotificationSeverity_Error = 3

class swUserPreferenceDoubleValue_e(IntEnum):
    """swUserPreferenceDoubleValue_e (220 constants, from SwConst)."""
    swDetailingNoteFontHeight = 0
    swDetailingDimFontHeight = 1
    swSTLDeviation = 2
    swSTLAngleTolerance = 3
    swSpinBoxMetricLengthIncrement = 4
    swSpinBoxEnglishLengthIncrement = 5
    swSpinBoxAngleIncrement = 6
    swMaterialPropertyDensity = 7
    swTiffPrintPaperWidth = 8
    swTiffPrintPaperHeight = 9
    swTiffPrintDrawingPaperHeight = 8
    swTiffPrintDrawingPaperWidth = 9
    swDetailingCenterlineExtension = 10
    swDetailingBreakLineGap = 11
    swDetailingCenterMarkSize = 12
    swDetailingWitnessLineGap = 13
    swDetailingWitnessLineExtension = 14
    swDetailingObjectToDimOffset = 15
    swDetailingDimToDimOffset = 16
    swDetailingMaxLinearToleranceValue = 17
    swDetailingMinLinearToleranceValue = 18
    swDetailingMaxAngularToleranceValue = 19
    swDetailingMinAngularToleranceValue = 20
    swDetailingToleranceTextScale = 21
    swDetailingToleranceTextHeight = 22
    swDetailingNoteBentLeaderLength = 23
    swDetailingArrowHeight = 24
    swDetailingArrowWidth = 25
    swDetailingArrowLength = 26
    swDetailingSectionArrowHeight = 27
    swDetailingSectionArrowWidth = 28
    swDetailingSectionArrowLength = 29
    swGridMajorSpacing = 30
    swSnapToAngleValue = 31
    swImageQualityShadedDeviation = 32
    swDrawingDefaultSheetScaleNumerator = 33
    swDrawingDefaultSheetScaleDenominator = 34
    swDrawingDetailViewScale = 35
    swViewRotationArrowKeys = 36
    swMateAnimationSpeed = 37
    swViewAnimationSpeed = 38
    swDetailingDimBentLeaderLength = 39
    swMaterialPropertyCrosshatchScale = 40
    swMaterialPropertyCrosshatchAngle = 41
    swDrawingAreaHatchScale = 42
    swDrawingAreaHatchAngle = 43
    swPageSetupPrinterTopMargin = 44
    swPageSetupPrinterBottomMargin = 45
    swPageSetupPrinterLeftMargin = 46
    swPageSetupPrinterRightMargin = 47
    swPageSetupPrinterThinLineWeight = 48
    swPageSetupPrinterNormalLineWeight = 49
    swPageSetupPrinterThickLineWeight = 50
    swPageSetupPrinterThick2LineWeight = 51
    swPageSetupPrinterThick3LineWeight = 52
    swPageSetupPrinterThick4LineWeight = 53
    swPageSetupPrinterThick5LineWeight = 54
    swPageSetupPrinterThick6LineWeight = 55
    swPageSetupPrinterDrawingScale = 56
    swPageSetupPrinterPartAsmScale = 57
    swCustomizedImportTolerance = 58
    swDetailingBalloonBentLeaderLength = 60
    swBOMControlSplitHeight = 61
    swAnnotationTextScaleNumerator = 62
    swAnnotationTextScaleDenominator = 63
    swDetailingDimBreakGap = 64
    swCurvatureValue1 = 65
    swCurvatureValue2 = 66
    swCurvatureValue3 = 67
    swCurvatureValue4 = 68
    swCurvatureValue5 = 69
    swDetailingBreakLineExtension = 70
    swDetailingToleranceFitTolTextScale = 71
    swDetailingToleranceFitTolTextHeight = 72
    swDocumentColorAdvancedAmbient = 73
    swDocumentColorAdvancedDiffuse = 74
    swDocumentColorAdvancedSpecularity = 75
    swDocumentColorAdvancedShininess = 76
    swDocumentColorAdvancedTransparency = 77
    swDocumentColorAdvancedEmission = 78
    swDxfOutputScaleFactor = 79
    swHoleTableTagAngle = 80
    swHoleTableTagOffset = 81
    swDetailingMaxWitnessLineLength = 82
    swDrawingKeyboardMovementIncrement = 83
    swSketchSnapsAngleValue = 84
    swDxfMergingDistance = 85
    swDetailingDimRadialSnapAngle = 86
    swViewTransitionHideShowComponent = 87
    swViewTransitionIsolate = 88
    swLineFontVisibleEdgesThicknessCustom = 89
    swLineFontHiddenEdgesThicknessCustom = 90
    swLineFontSketchCurvesThicknessCustom = 91
    swLineFontDetailCircleThicknessCustom = 92
    swLineFontSectionLineThicknessCustom = 93
    swLineFontDimensionsThicknessCustom = 94
    swLineFontConstructionCurvesThicknessCustom = 95
    swLineFontCrosshatchThicknessCustom = 96
    swLineFontTangentEdgesThicknessCustom = 97
    swLineFontDetailBorderThicknessCustom = 98
    swLineFontCosmeticThreadThicknessCustom = 99
    swLineFontHideTangentEdgeThicknessCustom = 100
    swLineFontViewArrowThicknessCustom = 101
    swLineFontExplodedLinesThicknessCustom = 102
    swLineFontBreakLineThicknessCustom = 103
    swDetailingBalloonLeaderLineThicknessCustom = 104
    swDetailingBalloonFrameLineThicknessCustom = 105
    swDetailingDatumLeaderLineThicknessCustom = 106
    swDetailingDatumFrameLineThicknessCustom = 107
    swDetailingGtolLeaderLineThicknessCustom = 108
    swDetailingGtolFrameLineThicknessCustom = 109
    swDetailingNoteLeaderLineThicknessCustom = 110
    swDetailingSFSymbolLeaderLineThicknessCustom = 111
    swDetailingWeldSymbolLeaderLineThicknessCustom = 112
    swDetailingAnnotationBentLeaderLength = 113
    swDetailingGtolBentLeaderLength = 114
    swDetailingSFSymbolBentLeaderLength = 115
    swDetailingMaxToleranceValue = 116
    swDetailingMinToleranceValue = 117
    swSpinBoxTimeIncrement = 118
    swDetailingBorderUserDefined = 119
    swDetailingBOMBalloonCustomSize = 120
    swDetailingBOMStackedBalloonCustomSize = 121
    swLineFontSpeedPakDrawingsModelEdgesThicknessCustom = 122
    swPartDimXpertLengthUnitTol1Value = 123
    swPartDimXpertLengthUnitTol2Value = 124
    swPartDimXpertLengthUnitTol3Value = 125
    swPartDimXpertAngularUnitTolValue = 126
    swPartDimXpertLocationDistanceTolUpperValue = 127
    swPartDimXpertLocationDistanceTolLowerValue = 128
    swPartDimXpertLocationAngleTolUpperValue = 129
    swPartDimXpertLocationAngleTolLowerValue = 130
    swPartDimXpertChainPatternLocTolUpperValue = 131
    swPartDimXpertChainPatternLocTolLowerValue = 132
    swPartDimXpertChainInnerTolUpperValue = 133
    swPartDimXpertChainInnerTolLowerValue = 134
    swPartDimXpertGeometricPrimaryTolValue = 135
    swPartDimXpertGeometricSecondFeatureSizeTolValue = 136
    swPartDimXpertGeometricSecondPlaneFeatureTolValue = 137
    swPartDimXpertGeometricThirdFeatureSizeTolValue = 138
    swPartDimXpertGeometricThirdPlaneFeatureTolValue = 139
    swPartDimXpertGeometricPositionTolValue = 140
    swPartDimXpertGeometricPositionCompositeTolValue = 141
    swPartDimXpertGeometricSurfaceProfileTolValue = 142
    swPartDimXpertGeometricSurfaceProfileCompositeTolValue = 143
    swPartDimXpertGeometricRunoutTolValue = 144
    swPartDimXpertChamferWidthRatio = 145
    swPartDimXpertChamferMaxWidth = 146
    swPartDimXpertChamferDistanceTolUpperValue = 147
    swPartDimXpertChamferDistanceTolLowerValue = 148
    swPartDimXpertChamferAngleTolUpperValue = 149
    swPartDimXpertChamferAngleTolLowerValue = 150
    swPartDimXpertSizeDiameterTolUpperValue = 151
    swPartDimXpertSizeDiameterTolLowerValue = 152
    swPartDimXpertSizeCounterboreDiameterTolUpperValue = 153
    swPartDimXpertSizeCounterboreDiameterTolLowerValue = 154
    swPartDimXpertSizeCountersinkDiameterTolUpperValue = 155
    swPartDimXpertSizeCountersinkDiameterTolLowerValue = 156
    swPartDimXpertSizeCountersinkAngleTolUpperValue = 157
    swPartDimXpertSizeCountersinkAngleTolLowerValue = 158
    swPartDimXpertSizeLengthSlotTolUpperValue = 159
    swPartDimXpertSizeLengthSlotTolLowerValue = 160
    swPartDimXpertSizeWidthSlotTolUpperValue = 161
    swPartDimXpertSizeWidthSlotTolLowerValue = 162
    swPartDimXpertSizeDepthTolUpperValue = 163
    swPartDimXpertSizeDepthTolLowerValue = 164
    swPartDimXpertSizeFilletRadiusTolUpperValue = 165
    swPartDimXpertSizeFilletRadiusTolLowerValue = 166
    swPunchTableTagAngle = 167
    swPunchTableTagOffset = 168
    swLineFontAdjoiningComponentCustom = 169
    swQuickViewTransparencyLevel = 170
    swDetailingRevisionCloudLineThicknessCustom = 171
    swDetailingRevisionCloudMaxArcRadius = 172
    swSheetMetalBendNotesLeaderLineThicknessCustom = 173
    swSheetMetalBendNotesBorderSizeCustom = 174
    swSheetMetalBendNotesLeaderLength = 175
    swDetailingBorderAddPadding = 176
    swDetailingBOMBalloonPadding = 177
    swDetailingBOMStackedBalloonPadding = 178
    swDetailingTablesHorizontalPadding = 179
    swDetailingTablesVerticalPadding = 180
    swLineFontBendLineUpThicknessCustom = 181
    swLineFontBendLineDownThicknessCustom = 182
    swLineFontEnvelopeComponentThicknessCustom = 183
    swDetailingCenterOfMassSize = 184
    swViewSelectorSpeed = 185
    swDetailingBalloonQtyGapDistance = 186
    swDimensionsExtensionLineStyleThicknessCustom = 188
    swSmartMateSensitivity = 189
    swSystemTouchRotateWidth = 190
    swSystemTouchRotateVersusPanThreshhold = 191
    swDetailingParaSpacing = 192
    swTwistCountValuePerMeter = 194
    swDetailingLocationLabelFrameLineThicknessCustom = 195
    swDetailingLocationLabelStyleCustomSize = 196
    swDetailingLocationLabelPadding = 197
    swDetailingCenterMarkGap = 198
    swDetailingBorderLeaderCustomLineThickness = 199
    swDetailingBorderZoneDividerLength = 200
    swDetailingBorderOuterCenterZoneDividerLength = 201
    swDetailingBorderInnerCenterZoneDividerLength = 202
    swDetailingBorderZoneDividerCustomLineThickness = 203
    swDetailingOrdinateSize = 204
    swLineFontEmphasizedSectionThicknessCustom = 205
    swPrint3DBoxX = 206
    swPrint3DBoxY = 207
    swPrint3DBoxZ = 208
    swMatesMaximumDeviationForMisalignedMates = 209
    swASMSLDPRT_ExcludeComponentsByVisibilityThreshold = 210
    swASMSLDPRT_ExcludeComponentsByBBoxVolumeThreshold = 211
    swPLYDeviation = 212
    swPLYAngleTolerance = 213
    swSheetMetalMBDLeaderLineThicknessCustom = 214
    swSheetMetalMBDBorderSizeCustom = 215
    swSheetMetalMBDLeaderLength = 216
    swDetailingHatchDensityLimit = 217
    swAbsChordalErrorVal = 218
    swAbsNormalDeviationVal = 219
    swAbsEdgeLengthVal = 220

class swUserPreferenceIntegerValue_e(IntEnum):
    """swUserPreferenceIntegerValue_e (628 constants, from SwConst)."""
    swDxfVersion = 0
    swDxfOutputFonts = 1
    swDxfMappingFileIndex = 2
    swAutoSaveInterval = 3
    swResolveLightweight = 4
    swAcisOutputVersion = 5
    swTiffScreenOrPrintCapture = 6
    swTiffImageType = 7
    swTiffCompressionScheme = 8
    swTiffPrintDPI = 9
    swTiffPrintPaperSize = 10
    swTiffPrintScaleFactor = 11
    swCreateBodyFromSurfacesOption = 12
    swDetailingDimensionStandard = 13
    swDetailingDualDimPosition = 14
    swDetailingDimTrailingZero = 15
    swDetailingArrowStyleForDimensions = 16
    swDetailingDimensionArrowPosition = 17
    swDetailingLinearDimLeaderStyle = 18
    swDetailingRadialDimLeaderStyle = 19
    swDetailingAngularDimLeaderStyle = 20
    swDetailingLinearToleranceStyle = 21
    swDetailingAngularToleranceStyle = 22
    swDetailingToleranceTextSizing = 23
    swDetailingLinearDimPrecision = 24
    swDetailingLinearTolPrecision = 25
    swDetailingAltLinearDimPrecision = 26
    swDetailingAltLinearTolPrecision = 27
    swDetailingAngularDimPrecision = 28
    swDetailingAngularTolPrecision = 29
    swDetailingNoteTextAlignment = 30
    swDetailingNoteLeaderSide = 31
    swDetailingBalloonStyle = 32
    swDetailingBalloonFit = 33
    swDetailingBOMBalloonStyle = 34
    swDetailingBOMBalloonFit = 35
    swDetailingBOMUpperText = 36
    swDetailingBOMLowerText = 37
    swDetailingArrowStyleForEdgeVertexAttachment = 38
    swDetailingArrowStyleForFaceAttachment = 39
    swDetailingArrowStyleForUnattached = 40
    swDetailingVirtualSharpStyle = 41
    swGridMinorLinesPerMajor = 42
    swSnapPointsPerMinor = 43
    swImageQualityShaded = 44
    swImageQualityWireframe = 45
    swImageQualityWireframeValue = 46
    swUnitsLinear = 47
    swUnitsLinearDecimalDisplay = 48
    swUnitsLinearDecimalPlaces = 49
    swUnitsLinearFractionDenominator = 50
    swUnitsAngular = 51
    swUnitsAngularDecimalPlaces = 52
    swLineFontVisibleEdgesThickness = 53
    swLineFontVisibleEdgesStyle = 54
    swLineFontHiddenEdgesThickness = 55
    swLineFontHiddenEdgesStyle = 56
    swLineFontSketchCurvesThickness = 57
    swLineFontSketchCurvesStyle = 58
    swLineFontDetailCircleThickness = 59
    swLineFontDetailCircleStyle = 60
    swLineFontSectionLineThickness = 61
    swLineFontSectionLineStyle = 62
    swLineFontDimensionsThickness = 63
    swLineFontDimensionsStyle = 64
    swLineFontConstructionCurvesThickness = 65
    swLineFontConstructionCurvesStyle = 66
    swLineFontCrosshatchThickness = 67
    swLineFontCrosshatchStyle = 68
    swLineFontTangentEdgesThickness = 69
    swLineFontTangentEdgesStyle = 70
    swLineFontDetailBorderThickness = 71
    swLineFontDetailBorderStyle = 72
    swLineFontCosmeticThreadThickness = 73
    swLineFontCosmeticThreadStyle = 74
    swStepAP = 75
    swHiddenEdgeDisplayDefault = 76
    swTangentEdgeDisplayDefault = 77
    swSTLQuality = 78
    swDrawingProjectionType = 79
    swDrawingPrintCrosshatchOutOfDateViews = 80
    swPerformanceAssemRebuildOnLoad = 81
    swLoadExternalReferences = 82
    swIGESRepresentation = 83
    swIGESSystem = 84
    swIGESCurveRepresentation = 85
    swViewRotationMouseSpeed = 86
    swBackupCopiesPerDocument = 87
    swCheckForOutOfDateLightweightComponents = 88
    swParasolidOutputVersion = 89
    swLineFontHideTangentEdgeThickness = 90
    swLineFontHideTangentEdgeStyle = 91
    swLineFontViewArrowThickness = 92
    swLineFontViewArrowStyle = 93
    swEdgesHiddenEdgeDisplay = 94
    swEdgesTangentEdgeDisplay = 95
    swEdgesShadedModeDisplay = 96
    swDetailingBOMStackedBalloonStyle = 97
    swDetailingBOMStackedBalloonFit = 98
    swSystemColorsViewportBackground = 99
    swSystemColorsTopGradientColor = 100
    swSystemColorsBottomGradientColor = 101
    swSystemColorsDynamicHighlight = 102
    swSystemColorsHighlight = 103
    swSystemColorsSelectedItem1 = 104
    swSystemColorsSelectedItem2 = 105
    swSystemColorsSelectedItem3 = 106
    swSystemColorsSelectedFaceShaded = 107
    swSystemColorsDrawingsVisibleModelEdge = 108
    swSystemColorsDrawingsHiddenModelEdge = 109
    swSystemColorsDrawingsPaperBorder = 110
    swSystemColorsDrawingsPaperShadow = 111
    swSystemColorsDrawingsSheetBorder = 111
    swSystemColorsImportedDrivingAnnotation = 112
    swSystemColorsImportedDrivenAnnotation = 113
    swSystemColorsSketchOverDefined = 114
    swSystemColorsSketchFullyDefined = 115
    swSystemColorsSketchUnderDefined = 116
    swSystemColorsSketchInvalidGeometry = 117
    swSystemColorsSketchNotSolved = 118
    swSystemColorsGridLinesMinor = 119
    swSystemColorsGridLinesMajor = 120
    swSystemColorsConstructionGeometry = 121
    swSystemColorsDanglingDimension = 122
    swSystemColorsText = 123
    swSystemColorsAssemblyEditPart = 124
    swSystemColorsAssemblyEditPartHiddenLines = 125
    swSystemColorsAssemblyNonEditPart = 126
    swSystemColorsInactiveEntity = 127
    swSystemColorsTemporaryGraphics = 128
    swSystemColorsTemporaryGraphicsShaded = 129
    swSystemColorsActiveSelectionListBox = 130
    swSystemColorsSurfacesOpenEdge = 131
    swSystemColorsTreeViewBackground = 132
    swAcisOutputUnits = 133
    swSystemColorsShadedEdge = 134
    swDxfOutputLineStyles = 135
    swDxfOutputNoScale = 136
    swPageSetupPrinterOrientation = 138
    swPageSetupPrinterDrawingColor = 139
    swImportCheckAndRepair = 140
    swUseCustomizedImportTolerance = 141
    swStepExportPreference = 142
    swEdgesInContextEditTransparencyType = 143
    swEdgesInContextEditTransparency = 144
    swPlaneDisplayFrontFaceColor = 145
    swPlaneDisplayBackFaceColor = 146
    swPlaneDisplayTransparency = 147
    swPlaneDisplayIntersectionLineColor = 148
    swDetailingDatumDisplayType = 149
    swBOMConfigurationAnchorType = 150
    swBOMConfigurationWhatToShow = 151
    swBOMControlMissingRowDisplay = 152
    swBOMControlSplitDirection = 153
    swDetailingChamferDimLeaderStyle = 154
    swDetailingChamferDimTextStyle = 155
    swDetailingChamferDimXStyle = 156
    swDocumentColorFeatBend = 157
    swDocumentColorFeatBoss = 158
    swDocumentColorFeatCavity = 159
    swDocumentColorFeatChamfer = 160
    swDocumentColorFeatCut = 161
    swDocumentColorFeatLoftCut = 162
    swDocumentColorFeatSurfCut = 163
    swDocumentColorFeatSweepCut = 164
    swDocumentColorFeatWeldBead = 165
    swDocumentColorFeatExtrude = 166
    swDocumentColorFeatFillet = 167
    swDocumentColorFeatHole = 168
    swDocumentColorFeatLibrary = 169
    swDocumentColorFeatLoft = 170
    swDocumentColorFeatMidSurface = 171
    swDocumentColorFeatPattern = 172
    swDocumentColorFeatRefSurface = 173
    swDocumentColorFeatRevolution = 174
    swDocumentColorFeatShell = 175
    swDocumentColorFeatDerivedPart = 176
    swDocumentColorFeatSweep = 177
    swDocumentColorFeatThicken = 178
    swDocumentColorFeatRib = 179
    swDocumentColorFeatDome = 180
    swDocumentColorFeatForm = 181
    swDocumentColorFeatShape = 182
    swDocumentColorFeatReplaceFace = 183
    swDocumentColorWireFrame = 184
    swDocumentColorShading = 185
    swDocumentColorHidden = 186
    swLineFontExplodedLinesThickness = 187
    swLineFontExplodedLinesStyle = 188
    swSystemColorsRefTriadX = 189
    swSystemColorsRefTriadY = 190
    swSystemColorsRefTriadZ = 191
    swAcisOutputGeometryPreference = 192
    swSystemColorsDTDim = 193
    swLargeAsmModeThreshold = 194
    swLargeAsmModeAutoActivate = 195
    swLargeAsmModeCheckOutOfDateLightweight = 196
    swLargeAsmModeAutoRecoverCount = 197
    swLargeAsmModeDisplayModeForNewDrawViews = 198
    swLineFontBreakLineThickness = 199
    swLineFontBreakLineStyle = 200
    swSaveAssemblyAsPartOptions = 201
    swDetailingDimensionTextAlignmentVertical = 202
    swDetailingDimensionTextAlignmentHorizontal = 203
    swDetailingToleranceFitTolTextSizing = 204
    swImportUnitPreference = 205
    swImportCurvePreference = 206
    swImportUseBrep = 207
    swImportStlVrmlModelType = 208
    swSystemColorsSelectedItem4 = 209
    swImportStlVrmlUnits = 210
    swExportStlUnits = 211
    swExportVrmlUnits = 212
    swSystemColorsSketchInactive = 213
    swExternalReferencesUpdateOutOfDateLinkedDesignTable = 214
    swSystemColorsTreeItemNormal = 215
    swSystemColorsTreeItemSelected = 216
    swSystemColorsDrawingsPaper = 217
    swSystemColorsDrawingsBackground = 218
    swSystemColorsDrawingsViewBorder = 219
    swDetailingNotesLeaderStyle = 220
    swSystemColorsDrawingsLockedFocus = 221
    swRevisionTableTagStyle = 222
    swRevisionTableSymbolShape = 223
    swBomTableZeroQuantityDisplay = 224
    swDocumentColorFeatStructuralMember = 225
    swDocumentColorFeatGusset = 226
    swDocumentColorFeatEndCap = 227
    swDetailingAutoBalloonLayout = 228
    swDocumentColorFeatWrap = 229
    swRebuildOnActivation = 230
    swSystemColorsImportedAnnotation = 231
    swSystemColorsNonImportedAnnotation = 232
    swLevelOfDetail = 233
    swLargeAsmLevelOfDetail = 234
    swPropertyManagerColorDivider = 235
    swCollabCheckReadOnlyModifiedInterval = 236
    swEdrawingsSaveAsSelectionOption = 237
    swHoleTableOriginStandard = 238
    swHoleTableTagStyle = 239
    swHoleTableHoleLocationPrecision = 240
    swDetailingDetailViewLabels_Name = 241
    swDetailingDetailViewLabels_Label = 242
    swDetailingDetailViewLabels_Scale = 243
    swDetailingDetailViewLabels_Delimiter = 244
    swDetailingSectionViewLabels_Name = 245
    swDetailingSectionViewLabels_Label = 246
    swDetailingSectionViewLabels_Scale = 247
    swDetailingSectionViewLabels_Delimiter = 248
    swDetailingAuxViewLabels_Name = 249
    swDetailingAuxViewLabels_Label = 250
    swDetailingAuxViewLabels_Scale = 251
    swDetailingAuxViewLabels_Delimiter = 252
    swDxfMultiSheetOption = 253
    swUnitsDualLinear = 254
    swUnitsDualLinearDecimalDisplay = 255
    swUnitsDualLinearDecimalPlaces = 256
    swUnitsDualLinearFractionDenominator = 257
    swUnitsMassPropLength = 258
    swUnitsMassPropMass = 259
    swUnitsMassPropVolume = 260
    swUnitsMassPropDecimalPlaces = 261
    swUnitsForce = 262
    swUnitSystem = 263
    swBendNoteStyle = 264
    swDetailingLeadingZero = 265
    swDetailingToleranceFitTolDisplayLinear = 266
    swDetailingToleranceFitTolDisplayAngular = 267
    swMaterialPropertyAreaHatchFillStyle = 268
    swDrawingAreaHatchFillStyle = 269
    swPerformanceViewsToDraftQuality = 270
    swFeatureManagerDisplayWarnings = 271
    swSheetMetalColorBendLinesUp = 272
    swSheetMetalColorBendLinesDown = 273
    swSheetMetalColorFormFeature = 274
    swSheetMetalColorBendLinesHems = 275
    swSheetMetalColorModelEdges = 276
    swSystemColorsDimsNotMarkedForDrawing = 277
    swSystemColorsAsmInterferenceVolume = 278
    swSystemColorsSwiftAnnotations = 279
    swSystemColorsSwiftUnderConstrained = 280
    swSystemColorsSwiftFullyConstrained = 281
    swSystemColorsSwiftOverConstrained = 282
    swSystemColorsToleranceAnalysisDim = 283
    swSystemColorsPropertyManagerColor = 284
    swPropertyManagerColorBackground = 285
    swPropertyManagerColorActiveClosedDivider = 286
    swPropertyManagerColorEditBox = 287
    swPropertyManagerColorEditText = 288
    swPropertyManagerColorLabelAndIcon = 289
    swPropertyManagerColorTitle = 290
    swPropertyManagerColorOuterBorder = 291
    swPropertyManagerColorInnerBorder = 292
    swPropertyManagerColorTopBorder = 293
    swPropertyManagerColorImportantMessage = 294
    swSystemColorsHiddenEdgeSelectionShow = 295
    swDetailingForeshortenedDiameterStyle = 296
    swRevisionTableMultipleSheetStyle = 297
    swUndoStepsMaximum = 298
    swDetailingDimFractionStyle = 299
    swDetailingDimFractionScaleIndex = 300
    swAutoSaveIntervalMode = 301
    swBackupRemoveInterval = 302
    swSaveReminderInterval = 303
    swSaveReminderIntervalMode = 304
    swColorsBackgroundAppearance = 305
    swRebuildErrorAction = 306
    swSheetMetalColorFlatPatternSketch = 307
    swLineFontVisibleEdgesEndCap = 308
    swLineFontHiddenEdgesEndCap = 309
    swLineFontSketchCurvesEndCap = 310
    swDetailingDimXpertChamferScheme = 311
    swDetailingDimXpertSlotScheme = 312
    swDetailingDimXpertFilletOptions = 313
    swDetailingDimXpertChamferOptions = 314
    swSystemColorsGhostSelColor = 315
    swFeatureManagerBlocksVisibility = 318
    swFeatureManagerDesignBinderVisibility = 319
    swFeatureManagerAnnotationsVisibility = 320
    swFeatureManagerLightsVisibility = 321
    swFeatureManagerSolidBodiesVisibility = 322
    swFeatureManagerSurfaceBodiesVisibility = 323
    swFeatureManagerEquationsVisibility = 324
    swFeatureManagerMaterialVisibility = 325
    swFeatureManagerDefaultPlanesVisibility = 326
    swFeatureManagerOriginVisibility = 327
    swFeatureManagerMateReferencesVisibility = 328
    swFeatureManagerDesignTableVisibility = 329
    swSearchResultsPerPage = 330
    swSearchMaxResultsPerDataSource = 331
    swUnitsForceDecimalPlaces = 332
    swUnitsEnergyUnits = 333
    swUnitsEnergyDecimalPlaces = 334
    swUnitsPowerUnits = 335
    swUnitsPowerDecimalPlaces = 336
    swUnitsTimeUnits = 337
    swUnitsTimeDecimalPlaces = 338
    swSystemColorsInactiveHandles = 339
    swPropertyMgrDockingState = 340
    swDetailingBalloonLeaderStyle = 341
    swDetailingBalloonLeaderLineStyle = 342
    swDetailingBalloonLeaderLineThickness = 343
    swDetailingBalloonFrameLineStyle = 344
    swDetailingBalloonFrameLineThickness = 345
    swDetailingDatumLeaderLineStyle = 346
    swDetailingDatumLeaderLineThickness = 347
    swDetailingDatumFrameLineStyle = 348
    swDetailingDatumFrameLineThickness = 349
    swDetailingGtolLeaderStyle = 350
    swDetailingGtolLeaderSide = 351
    swDetailingGtolLeaderLineStyle = 352
    swDetailingGtolLeaderLineThickness = 353
    swDetailingGtolFrameLineStyle = 354
    swDetailingGtolFrameLineThickness = 355
    swDetailingNoteLeaderLineStyle = 356
    swDetailingNoteLeaderLineThickness = 357
    swDetailingSFSymbolLeaderStyle = 358
    swDetailingSFSymbolLeaderLineStyle = 359
    swDetailingSFSymbolLeaderLineThickness = 360
    swDetailingWeldSymbolLeaderSide = 361
    swDetailingWeldSymbolLeaderLineStyle = 362
    swDetailingWeldSymbolLeaderLineThickness = 363
    swDetailingGeneralTableBorderLineWeight = 364
    swDetailingGeneralTableGridLineWeight = 365
    swDetailingBillOfMaterialBorderLineWeight = 366
    swDetailingBillOfMaterialGridLineWeight = 367
    swDetailingHoleTableBorderLineWeight = 368
    swDetailingHoleTableGridLineWeight = 369
    swDetailingRevisionTableBorderLineWeight = 370
    swDetailingRevisionTableGridLineWeight = 371
    swDetailingDimensionTextAndLeaderStyle = 372
    swDetailingToleranceStyle = 375
    swDetailingToleranceFitTolDisplay = 376
    swFeatureManagerSensorVisibility = 377
    swFeatureManagerTableFolderVisibility = 378
    swSystemColorsDrawingsSpeedPakModelEdge = 379
    swFeatureManagerConfigTableFolderVisibility = 380
    swDetailingDatumGbLeaderStyle = 381
    swDetailingTitleBlockTableBorderLineWeight = 382
    swDetailingTitleBlockTableGridLineWeight = 383
    swExportVrmlVersion = 384
    swExportJpegCompression = 385
    swSystemColorsDrawingsModelTangentEdges = 386
    swSystemColorsMateCalloutHealthy = 387
    swSystemColorsMateCalloutWarning = 388
    swSystemColorsMateCalloutError = 389
    swCenterLineMarkOrient = 390
    swLineFontSpeedPakDrawingsModelEdgesThickness = 400
    swLineFontSpeedPakDrawingsModelEdgesStyle = 401
    swDisplayStateCreationChoice = 402
    swSystemColorsSheetMetalTemporaryGraphics = 403
    swSystemColorsMeasureSelection = 404
    swPartDimXpertLengthUnitTol1Decimals = 405
    swPartDimXpertLengthUnitTol2Decimals = 406
    swPartDimXpertLengthUnitTol3Decimals = 407
    swPartDimXpertGeneralToleranceClass = 408
    swPartDimXpertLocationDistanceTolType = 409
    swPartDimXpertLocationAngleTolType = 410
    swPartDimXpertLocationDistanceBlockPrecision = 411
    swPartDimXpertLocationAngleBlockPrecision = 412
    swPartDimXpertChainPatternLocTolType = 413
    swPartDimXpertChainInnerTolType = 414
    swPartDimXpertChainPatternLocBlockPrecision = 415
    swPartDimXpertChainDistanceBwtnFeatBlockPrecision = 416
    swPartDimXpertChamferDistanceTolType = 417
    swPartDimXpertChamferAngleTolType = 418
    swPartDimXpertChamferDistanceBlockPrecision = 419
    swPartDimXpertChamferAngleBlockPrecision = 420
    swPartDimXpertSizeDiameterTolType = 421
    swPartDimXpertSizeCounterboreDiameterTolType = 422
    swPartDimXpertSizeCountersinkDiameterTolType = 423
    swPartDimXpertSizeCountersinkAngleTolType = 424
    swPartDimXpertSizeLengthSlotTolType = 425
    swPartDimXpertSizeWidthSlotTolType = 426
    swPartDimXpertSizeDepthTolType = 427
    swPartDimXpertSizeFilletRadiusTolType = 428
    swPartDimXpertSizeDiameterBlockPrecsion = 429
    swPartDimXpertSizeCounterboreDiameterBlockPrecsion = 430
    swPartDimXpertSizeCountersinkDiameterBlockPrecsion = 431
    swPartDimXpertSizeCountersinkAngleBlockPrecision = 432
    swPartDimXpertSizeLengthSlotBlockPrecision = 433
    swPartDimXpertSizeWidthSlotBlockPrecision = 434
    swPartDimXpertSizeDepthBlockPrecision = 435
    swPartDimXpertSizeFilletRadiusBlockPrecision = 436
    swPartDimXpertDisplaySlotDimensionType = 437
    swPartDimXpertDisplayHoleDimensionType = 438
    swPartDimXpertDisplayGtolLinearDimAttachment = 439
    swPartDimXpertDisplayDatumGtolSurfaceAttachment = 440
    swPartDimXpertDisplayDatumGtolLinearDimAttachment = 441
    swExportIFCUnits = 442
    swDetailingOrthoViewLabels_Scale = 443
    swDetailingOrthoViewLabels_Delimiter = 444
    swSystemOptionDisplayAntiAliasing = 445
    swTableHoleDualDimensionPos = 446
    swSystemColorsDrawingsChangedDimensions = 447
    swDetailingBendTableBorderLineWeight = 448
    swDetailingBendTableGridLineWeight = 449
    swBendLeadingZero = 450
    swBendTableZeroQuantityDisplay = 451
    swBendInnerRadiusPrecision = 452
    swBendAngularPrecision = 453
    swBendTableTagStyle = 454
    swPunchTableOriginStandard = 455
    swPunchTableLocationPrecision = 456
    swTablePunchDualDimensionPos = 457
    swPunchTableTagStyle = 458
    swDetailingSectionArrowStyle = 459
    swPerformanceFeedback = 460
    swLineFontAdjoiningComponent = 461
    swLineFontAdjoiningComponentStyle = 462
    swSystemColorsNoteHandle = 463
    swSystemColorsCrossHair = 464
    swSystemColorsNoteEditHandle = 465
    swSystemColorsTemporarySketchDragging = 466
    swSystemColorsWeldPathSelection = 467
    swDetailingPunchTableBorderLineWeight = 468
    swShowEquationCircularReferencesMessage = 469
    swDetailingPunchTableGridLineWeight = 470
    swDetailingWeldTableGridLineWeight = 471
    swDetailingWeldTableBorderLineWeight = 472
    swSearchIndexingPerformance = 473
    swLargeAsmModeLargeDesignReviewThreshhold = 474
    swShowEquationPotentialCircularReferencesMessage = 475
    swSaveReminderAutoDismissInterval = 476
    swDetailingRevisionCloudLineStyle = 477
    swDetailingRevisionCloudLineThickness = 478
    swDetailingHalfSectionArrow = 479
    swBendAllowancePrecision = 480
    swFeatureManagerFavorites = 481
    swFeatureManagerEDrawingMarkups = 482
    swSheetMetalColorBoundingBox = 483
    swSheetMetalBendNotesLeaderLineStyle = 484
    swSheetMetalBendNotesLeaderLineThickness = 485
    swSheetMetalBendNotesBorderStyle = 486
    swSheetMetalBendNotesBorderSize = 487
    swSheetMetalBendNotesTextAlignment = 488
    swSheetMetalBendNotesLeaderAnchor = 489
    swSheetMetalBendNotesLeaderDisplay = 490
    swSystemColorsCurrentColorScheme = 491
    swSystemColorsEnvelopes = 492
    swDetailingRadialDimsArrowPlacement = 493
    swSearchDissectionDailyStartTime = 494
    swSearchDissectionDailyStopTime = 495
    swLineFontBendLineUpStyle = 496
    swLineFontBendLineDownStyle = 497
    swLineFontEnvelopeComponentStyle = 498
    swLineFontBendLineUpThickness = 499
    swLineFontBendLineDownThickness = 500
    swLineFontEnvelopeComponentThickness = 501
    swEnvelopeComponentColor = 502
    swAssemblyVisualizationComponentColor1 = 503
    swAssemblyVisualizationComponentColor2 = 504
    swAssemblyVisualizationComponentColor3 = 505
    swAssemblyVisualizationComponentColor4 = 506
    swAssemblyVisualizationComponentColor5 = 507
    swAssemblyVisualizationComponentColor6 = 508
    swDetailingMiscView_Scale = 509
    swDetailingMiscView_Delimiter = 510
    swDetailingMiscView_Name = 511
    swDetailingAuxView_ViewIndication = 512
    swDetailingAuxView_Rotation = 513
    swDetailingSectionView_Rotation = 515
    swDimensionsExtensionLineStyle = 516
    swDimensionsExtensionLineStyleThickness = 517
    swDetailingOrthoView_Name = 518
    swAssemblyOpenMessagesDismissTime = 519
    swButtonSize = 520
    swTextSize = 521
    swUnitsDecimalRounding = 522
    swDetailingLocationLabelFrameLineStyle = 523
    swDetailingLocationLabelFrameLineThickness = 524
    swDetailingLocationLabelStyle = 525
    swDetailingLocationLabelFit = 526
    swDetailingLocationLabelUpperText = 527
    swDetailingLocationLabelLowerText = 528
    swDrawingSheetsZonesOrigin = 529
    swDrawingSheetsZonesLetterLayout = 530
    swDetailingBalloonAutoBalloons = 531
    swFeatureManagerSelectionSetsVisibility = 532
    swFeatureManagerHistory = 533
    swPDFExportShadedDraftDPI = 534
    swPDFExportOleDPI = 535
    swTwistCountValue = 536
    swManipConnectionPointColor = 537
    swRefVisualizationParentColor = 538
    swRefVisualizationChildrenColor = 539
    swDrawingSheetCustomPropSheetNo = 540
    swIFCExportSaveType = 541
    swDetailingSectionViewLineStyleDisplay = 542
    swSaveIFCFormat = 543
    swDetailingLinearForeshortened = 544
    swCartoonEdgeThickness = 545
    swTempGraphicsAddMaterialColor = 546
    swTempGraphicsRemoveMaterialColor = 547
    swDetailingBorderLeaderLineStyle = 548
    swDetailingBorderLeaderLineThickness = 549
    swDetailingBorderZoneDividerLineStyle = 550
    swDetailingBorderZoneDividerLineThickness = 551
    swIFCOmniUniClassPreference = 552
    swSystemColorsIconColor = 553
    swSystemColorsBackground = 554
    swShadedSketchContourColor = 555
    sw3DPDFAccuracy = 556
    swLineFontEmphasizedSectionOutlineStyle = 557
    swLineFontEmphasizedSectionThickness = 558
    swLineFontEmphasizedSectionEndCapStyle = 559
    swBasicDimType = 560
    swPolarMinHoles = 561
    swGraphicsTreeItemNormalColor = 562
    swZoneLineColor = 563
    swSketch_Auto_Solve_Threshold = 564
    swDrawing_Auto_Solve_Threshold = 565
    swPenSketchStrokeThickness = 566
    swPenSketchStrokeColor = 567
    swMatesDefaultMisalignedType = 569
    swUpdateOutOfDateSpeedPakConfigOnSave = 570
    swFeatureManagerMeshBodiesVisibility = 571
    swSolidBodiesDescriptionFirstPropertyIndex = 572
    swSolidBodiesDescriptionSecondPropertyIndex = 573
    swSolidBodiesDescriptionThirdPropertyIndex = 574
    swDefaultConfigSortOrder = 575
    swGraphicalAnnotationsColor = 576
    swImportNeutral_KnitOption = 577
    swImportNeutral_CurvesAndPointsOption = 578
    swImportNeutralAssemblyStructureMapping = 579
    swImportNeutralUnits = 580
    swBBoxDescriptionApplyMethod = 581
    swDetailingTrailingZeroTolerance = 582
    swDetailingTrailingZeroProperties = 583
    swDetailingAngleTrailingZero = 584
    swDetailingAngleTrailingZeroTolerance = 585
    swDetailingAngularRunningTrailingZero = 586
    swDetailingAngularRunningTrailingZeroTolerance = 587
    swEdrawingsAttachmentOption = 588
    swEdrawingsAttachmentType = 589
    swExportPlyUnits = 591
    swPLYQuality = 592
    swMaximumRecentDocuments = 593
    swFlatPatternColorsBendLinesUpDirection = 594
    swFlatPatternColorsBendLinesDownDirection = 595
    swFlatPatternColorsFromFeature = 596
    swFlatPatternColorsBendLinesHems = 597
    swFlatPatternColorsModelEdges = 598
    swFlatPatternColorsFlatPatternSketchColor = 599
    swFlatPatternColorsBoundingBox = 600
    swSheetMetalMBDBendNotesStyle = 601
    swSheetMetalMBDLeaderStyle = 602
    swSheetMetalMBDLeaderLineThickness = 603
    swSheetMetalMBDTextAlignment = 604
    swSheetMetalMBDLeaderAnchor = 605
    swSheetMetalMBDLeaderDisplay = 606
    swSheetMetalMBDBalloonStyle = 607
    swSheetMetalMBDFit = 608
    swSheetMetalMBDLineStyle_BendLinesUp = 609
    swSheetMetalMBDLineStyle_BendLinesDown = 610
    swFeatureManagerMarkupsVisibility = 611
    swEnableAutoMateFlip = 612
    swSystemColorsSelectedItem5 = 613
    swSystemColorsSelectedItem6 = 614
    swFeatureManagerTranslatedLanguage = 615
    swAssemblyLoadComponents = 616
    swConfigurationViewForFeatureManagerTree = 617
    swDetailingGtolMaterialConditionSymbolPlacement = 618
    swBomOverriddenCellValueColor = 619
    swSheetPrintQuadrant = 620
    swSketchExplodedColor = 621
    swDefaultBOMPartNumberForNewConfig = 622
    swDimOverriddenCellValueColor = 623
    swOppHandMirrorComp = 624
    swGtolDecimalSeparatorType = 625
    swCollinearChainDimensionArrowHeadTerminationStyle = 626
    swRecognizedMeshFaceColor = 627
    swUnrecognizedMeshFaceColor = 628
    swDetailingSFSymbolStandard = 629
    swZoomLevelOnOpen = 630
    swSMGExportProfile = 631
    swSMGRefineRelativeType = 632
    swSMGRefinementType = 633
    swSMGRefinementRelativeQuality = 634
    swPMIEditColor = 635
    swPrimaryComponentIdentifier = 636
    swPartDimXpertToleranceMethod = 637
    swDetailingFamilyTableGridLineWeight = 638
    swDetailingFamilyTableBorderLineWeight = 639
    swExportSVPJFileFormatGroupType = 640
    swMarkAssyAsModifiedWhenCosmeticChangesToRefDocs = 641
    swDxfGeomExportOption = 642
    swSaveToVersion = 643

class swUserPreferenceOption_e(IntEnum):
    """swUserPreferenceOption_e (35 constants, from SwConst)."""
    swDetailingNoOptionSpecified = 0
    swDetailingAnnotation = 100
    swDetailingBalloon = 101
    swDetailingDatum = 102
    swDetailingGeometricTolerance = 103
    swDetailingNote = 104
    swDetailingSurfaceFinishSymbol = 105
    swDetailingWeldSymbol = 106
    swDetailingRevisionCloud = 107
    swDetailingTableAnnotation = 150
    swDetailingGeneralTable = 151
    swDetailingBillOfMaterial = 152
    swDetailingHoleTable = 153
    swDetailingRevisionTable = 154
    swDetailingDimension = 200
    swDetailingAngleDimension = 201
    swDetailingArcLengthDimension = 202
    swDetailingChamferDimension = 203
    swDetailingDiameterDimension = 204
    swDetailingHoleDimension = 205
    swDetailingLinearDimension = 206
    swDetailingOrdinateDimension = 207
    swDetailingRadiusDimension = 208
    swDetailingAngularRunningDimension = 209
    swDetailingDrawingView = 300
    swDetailingDetailView = 301
    swDetailingSectionView = 302
    swDetailingAuxiliaryView = 303
    swDetailingOrthoView = 304
    swDetailingBendTable = 305
    swDetailingPunchTable = 306
    swDetailingWeldTable = 307
    swDetailingMiscView = 308
    swDetailingLocationLabel = 309
    swDetailingFamilyTable = 310

class swUserPreferenceRoutingDouble_e(IntEnum):
    """swUserPreferenceRoutingDouble_e (2 constants, from SWRoutingLib)."""
    swSlackPercentage = 1
    swTextSizeForConnectionAndRoutePoints = 2

class swUserPreferenceRoutingFileLocations_e(IntEnum):
    """swUserPreferenceRoutingFileLocations_e (10 constants, from SWRoutingLib)."""
    swRoutingLibraryPath = 1
    swFileLocationsRoutingAssemblyTemplate = 2
    swFileLocationsRoutingStandardTubes = 3
    swFileLocationsRoutingPipeTubeCoveringLibrary = 4
    swFileLocationsRoutingCableLibrary = 5
    swFileLocationsRoutingComponentLibrary = 6
    swFileLocationsRoutingStandardCable = 7
    swFileLocationsRoutingCoveringLibrary = 8
    swFileLocationsRoutingTagSchemes = 9
    swFileLocationsRoutingInterconnectsLibrary = 10

class swUserPreferenceRoutingInteger_e(IntEnum):
    """swUserPreferenceRoutingInteger_e (2 constants, from SWRoutingLib)."""
    swComponentRotationIncrementDegrees = 1
    swEnableMinimumBendRadiusChecks = 2

class swUserPreferenceRoutingToggle_e(IntEnum):
    """swUserPreferenceRoutingToggle_e (20 constants, from SWRoutingLib)."""
    swAutomaticallyCreateSketchFillets = 1
    swSaveRouteAssemblyExternally = 2
    swSaveRoutePartsExternally = 3
    swUseAutomaticNamingForRouteParts = 4
    swCreateCustomFittings = 5
    swCreatePipesOnOpenLineSegments = 6
    swAutomaticallyRouteOnDropOfFlangeConnectors = 7
    swAutomaticallyRouteOnDropOfClips = 8
    swAutomaticallyAddDimensionToRouteStubs = 9
    swEnableRouteErrorChecking = 10
    swDisplayErrorBalloons = 11
    swIncludeCoveringsInBOM = 12
    swAlwaysUseDefaultDocumentTemplate = 13
    swUseTriadToPosAndOrientComp = 14
    swUseAutoNamingForRouteParts = 15
    swUseCenterlineDim = 16
    swAutomaticallyZoomToFitRouteComponents = 17
    swUseConfigureComponentsToSelectConfigurations = 18
    swCreateRoutePartForSegmentsHavingBendRadiusLessThanMinimum = 19
    swHideConfigurationDialogForSWElectricalComponents = 20

class swUserPreferenceStringListValue_e(IntEnum):
    """swUserPreferenceStringListValue_e (3 constants, from SwConst)."""
    swDxfMappingFiles = 0
    swEmodelSelectionList = 1
    swEmodelAttachmentList = 2

class swUserPreferenceStringValue_e(IntEnum):
    """swUserPreferenceStringValue_e (141 constants, from SwConst)."""
    swFileLocationsDocuments = 1
    swFileLocationsPaletteFeatures = 2
    swFileLocationsPaletteParts = 3
    swFileLocationsPaletteFormTools = 4
    swFileLocationsBlocks = 5
    swFileLocationsDocumentTemplates = 6
    swFileLocationsSheetFormat = 7
    swDefaultTemplatePart = 8
    swDefaultTemplateAssembly = 9
    swDefaultTemplateDrawing = 10
    swBackupDirectory = 11
    swFileLocationsBendTable = 12
    swMaterialPropertyCrosshatchPattern = 13
    swDrawingAreaHatchPattern = 14
    swDetailingNextDatumFeatureLabel = 15
    swFileSaveAsCoordinateSystem = 16
    swFileLocationsPaletteAssemblies = 17
    swCustomPropertyUsedAsComponentDescription = 18
    swFileLocationsLibraryFeatures = 19
    swFileLocationsMacroFeatures = 20
    swFileLocationsWebFolders = 21
    swFileLocationsBOMTemplates = 22
    swFileLocationsMacros = 23
    swFileLocationsJournalFile = 24
    swFileLocationsCustomPropertyFile = 25
    swFileLocationsHoleCalloutFormatFile = 26
    swFileLocationsDimensionFavorites = 27
    swFileLocationsMaterialDatabases = 28
    swFileLocationsWeldmentProfiles = 29
    swFileLocationsColorSwatches = 30
    swFileLocationsTextures = 31
    swFileLocationsWeldmentPropertyFile = 32
    swFileLocationsHoleTableTemplates = 33
    swFileLocationsWeldmentCutListTemplates = 34
    swFileLocationsRevisionTableTemplates = 35
    swDrawingCustomPropertyUsedAsRevision = 36
    swFileLocationsRouteComponentLibrary = 37
    swFileLocationsDesignLibrary = 38
    swFileLocationsLineStyleDefinitions = 39
    swFileLocationsDesignJournalTemplate = 40
    swFileLocationsRouteCableLibrary = 41
    swFileLocationsAppearances = 42
    swFileLocationsScenes = 43
    swFileLocationsLights = 44
    swFileLocationsBendNoteFormatFile = 45
    swSeparatorCharacterForDims = 46
    swFileLocationsRouteCoveringLibrary = 47
    swFileLocationsDesignCheckerFile = 48
    swReferenceTriadXLabel = 49
    swReferenceTriadYLabel = 50
    swReferenceTriadZLabel = 51
    swHoleWizardToolBoxFolder = 52
    swAutoSaveDirectory = 53
    swColorsBackgroundImageFile = 54
    swDetailingBOMUpperCustomProperty = 55
    swDetailingBOMLowerCustomProperty = 56
    swFileLocationsTxCalloutFormatFile = 57
    swFileLocations3DCCModelFolder = 58
    swFileLocationsHoleWizardFavoritesDB = 59
    swFileLocationsSearchPaths = 60
    swFileLocationsSheetMetalGaugeTable = 61
    swFileLocationsSpellingFolders = 62
    swDetailingLayer = 63
    swFileLocationsDraftingStandard = 64
    swDetailingDimensionStandardName = 65
    swOverriddenQuantityColumnName = 66
    swFileLocationsCustomAppearances = 67
    swFileLocationsCustomDecals = 68
    swFileLocationsCustomScenes = 69
    swFileLocationsTitleBlockTableTemplate = 70
    swFileLocationsBendCalculationTable = 71
    swFileLocationsThemeFolder = 72
    swExportIFCType = 73
    swFileLocationsFuncBldrSegTypeDefinitions = 74
    swFileLocationsSustainabilityReportTemplateFolder = 75
    swFileLocationsCostingReportTemplateFolder = 76
    swFileLocationsCostingTemplates = 77
    swFileLocationsWeldTableTemplate = 78
    swFileLocationsBendTableTemplate = 79
    swFileLocationsPunchTableTemplate = 80
    swDetailingDetailViewLabels_CustomName = 81
    swDetailingDetailViewLabels_CustomScale = 82
    swDetailingSectionViewLabels_CustomName = 83
    swDetailingSectionViewLabels_CustomScale = 84
    swDetailingAuxViewLabels_CustomName = 85
    swDetailingAuxViewLabels_CustomScale = 86
    swCenterLineLayer = 87
    swCenterMarkLayer = 88
    swSheetMetalBendNotesLayer = 89
    swSearchDissectionLocation = 91
    swFileLocationsSymbolLibraryFolder = 92
    swFileLocationsNewSheetFormat = 93
    swDetailingMiscView_CustomName = 94
    swDetailingMiscView_CustomScale = 95
    swDraftStandardExclusionList = 96
    swDetailingOrthoView_CustomName = 97
    swDetailingOrthoView_CustomScale = 98
    swElecDuctingDuctName = 99
    swElecCableTrayDuctName = 100
    swHvacRectDuctName = 101
    swHvacCirDuctName = 102
    swElecDuctingElbowName = 102
    swElecCableTrayElbowName = 103
    swHvacRectElbowName = 104
    swHvacCirElbowName = 105
    swBorderLayer = 106
    swFileLocationsThreadProfiles = 107
    swFileLocationsGeneralTablesTemplate = 108
    swFileLocationsTxGeneralFileLocation = 109
    swMySldSettings = 110
    swSolidBodiesBBoxDescriptionPrefix = 111
    swSolidBodiesBBoxDescriptionFirstSeparator = 112
    swSolidBodiesBBoxDescriptionSecondSeparator = 113
    swSolidBodiesBBoxDescriptionSuffix = 114
    swSheetMetalDescription = 115
    swDimXpertGeneralToleranceCustomTable = 116
    swFileLocationsDefaultSave = 117
    swHoleTagsList = 118
    swBomTableBOMHeaderCustomText_ForTopLevelOnlyBOM = 119
    swBomTableBOMHeaderCustomText_ForPartOnlyBOM = 120
    swBomTableBOMHeaderCustomText_ForIndentedBOM = 121
    swFileLocationsDrawingScaleStandard = 122
    swStructureSystemsFolder = 123
    swWeldmentStructureCutlistID = 124
    swWeldmentSheetmetalCutlistID = 125
    swWeldmentGenericCutlistID = 126
    swFileLocationsHatchPatternFile = 127
    swFileLocationsInspectionProjects = 128
    swFileLocationsInspectionReports = 129
    swLastSynchronizationTimeStamp = 130
    swFileLocationsInspectionExports = 131
    swFileLocationsStructureSystemsConnectionElements = 132
    swFileLocationsConnectedLibrary = 133
    swExportOutputCoordinateSystem = 134
    swFileLocationsDefeatureRuleSets = 135
    swOppPrefixSuffixText = 136
    swVirtualComponentPrefixedit = 137
    swIFCExportPropertySetMappingFile = 138
    swSMGMetaPropertyName = 139
    swFileLocationsFamilyTableTemplates = 140
    swMultiCAD_ImportQueuePath = 141

class swUserPreferenceTextFormat_e(IntEnum):
    """swUserPreferenceTextFormat_e (51 constants, from SwConst)."""
    swDetailingNoteTextFormat = 0
    swDetailingDimensionTextFormat = 1
    swDetailingSectionTextFormat = 2
    swDetailingDetailTextFormat = 3
    swDetailingViewArrowTextFormat = 4
    swDetailingSurfaceFinishTextFormat = 5
    swDetailingWeldSymbolTextFormat = 6
    swDetailingGeneralTableTextFormat = 7
    swDetailingBalloonTextFormat = 8
    swDetailingDetailLabelTextFormat = 9
    swDetailingSectionLabelTextFormat = 10
    swDetailingBillOfMaterialTextFormat = 11
    swDetailingHoleTableTextFormat = 12
    swDetailingRevisionTableTextFormat = 13
    swDetailingDatumTextFormat = 14
    swDetailingGeometricToleranceTextFormat = 15
    swDetailingAuxiliaryLabelTextFormat = 16
    swDetailingTableTextFormat = 17
    swDetailingViewTextFormat = 18
    swDetailingAnnotationTextFormat = 19
    swDetailingTitleBlockTableTextFormat = 20
    swDetailingOrthoLabelTextFormat = 21
    swDetailingBendTextFormat = 22
    swDetailingSectionLabelNameTextFormat = 23
    swDetailingSectionLabelLabelTextFormat = 24
    swDetailingSectionLabelScaleTextFormat = 25
    swDetailingSectionLabelDelimiterTextFormat = 26
    swDetailingPunchTextFormat = 27
    swSheetMetalBendNotesTextFormat = 28
    swDetailingWeldSymbolTextRootInsideFont = 29
    swDetailingMiscView_NameTextFormat = 30
    swDetailingMiscView_ScaleTextFormat = 31
    swDetailingMiscView_DelimiterTextFormat = 32
    swDetailingAuxView_NameTextFormat = 33
    swDetailingAuxView_LabelTextFormat = 34
    swDetailingAuxView_RotationTextFormat = 35
    swDetailingAuxView_ScaleTextFormat = 36
    swDetailingAuxView_DelimiterTextFormat = 37
    swDetailingSectionView_RotationTextFormat = 38
    swDetailingOrthoView_NameTextFormat = 39
    swDetailingOrthoView_ScaleTextFormat = 40
    swDetailingOrthoView_DelimiterTextFormat = 41
    swDetailingDetailView_NameTextFormat = 42
    swDetailingDetailView_LabelTextFormat = 43
    swDetailingDetailView_ScaleTextFormat = 44
    swDetailingDetailView_DelimiterTextFormat = 45
    swDetailingLocationLabelTextFormat = 46
    swPointAxisCoordSystemNameFontTextFormat = 47
    swPointAxisCoordSystemLabelFontTextFormat = 48
    swSheetMetalMBDTextFormat = 49
    swDetailingFamilyTableTextFormat = 50

class swUserPreferenceToggle_e(IntEnum):
    """swUserPreferenceToggle_e (828 constants, from SwConst)."""
    swUseFolderSearchRules = 0
    swDisplayArcCenterPoints = 1
    swDisplayEntityPoints = 2
    swIgnoreFeatureColors = 3
    swDisplayAxes = 4
    swDisplayPlanes = 5
    swDisplayOrigins = 6
    swDisplayTemporaryAxes = 7
    swDxfMapping = 8
    swSketchAutomaticRelations = 9
    swInputDimValOnCreate = 10
    swFullyConstrainedSketchMode = 11
    swXTAssemSaveFormat = 12
    swDisplayCoordSystems = 13
    swExtRefOpenReadOnly = 14
    swExtRefNoPromptOrSave = 15
    swExtRefMultipleContexts = 16
    swExtRefAutoGenNames = 17
    swExtRefUpdateCompNames = 18
    swDisplayReferencePoints = 19
    swDisplayRoutePoints = 19
    swUseShadedFaceHighlight = 20
    swDXFDontShowMap = 21
    swThumbnailGraphics = 22
    swUseAlphaTransparency = 23
    swDynamicDrawingViewActivation = 24
    swAutoLoadPartsLightweight = 25
    swIGESStandardSetting = 26
    swIGESNurbsSetting = 27
    swTiffPrintScaleToFit = 28
    swDisplayVirtualSharps = 29
    swUpdateMassPropsDuringSave = 30
    swDisplayAnnotations = 31
    swDisplayFeatureDimensions = 32
    swDisplayReferenceDimensions = 33
    swDisplayAnnotationsUseAssemblySettings = 34
    swDisplayNotes = 35
    swDisplayGeometricTolerances = 36
    swDisplaySurfaceFinishSymbols = 37
    swDisplayWeldSymbols = 38
    swDisplayDatums = 39
    swDisplayDatumTargets = 40
    swDisplayCosmeticThreads = 41
    swDetailingDisplayWithBrokenLeaders = 42
    swDetailingDualDimensions = 43
    swDetailingDisplayDatumsPer1982 = 44
    swDetailingDisplayAlternateSection = 45
    swDetailingCenterMarkShowLines = 46
    swDetailingFixedSizeWeldSymbol = 47
    swDetailingDimsShowParenthesisByDefault = 48
    swDetailingDimsSnapTextToGrid = 49
    swDetailingDimsCenterText = 50
    swDetailingRadialDimsDisplay2ndOutsideArrow = 51
    swDetailingRadialDimsArrowsFollowText = 52
    swDetailingDimLeaderOverrideStandard = 53
    swDetailingNotesDisplayWithBentLeader = 54
    swDisplayTextAtSameSizeAlways = 55
    swDisplayOnlyInViewOfCreation = 56
    swGridDisplay = 57
    swGridDisplayDashed = 58
    swGridAutomaticScaling = 59
    swSnapToPoints = 60
    swSnapToAngle = 61
    swUnitsLinearRoundToNearestFraction = 62
    swUnitsLinearFeetAndInchesFormat = 63
    swFeatureManagerEnsureVisible = 64
    swFeatureManagerNameFeatureWhenCreated = 65
    swFeatureManagerKeyboardNavigation = 66
    swFeatureManagerDynamicHighlight = 67
    swColorsGradientPartBackground = 68
    swSTLBinaryFormat = 69
    swSTLShowInfoOnSave = 70
    swSTLDontTranslateToPositive = 71
    swSTLComponentsIntoOneFile = 72
    swSTLCheckForInterference = 73
    swOpenLastUsedDocumentAtStart = 74
    swSingleCommandPerPick = 75
    swShowDimensionNames = 76
    swShowErrorsEveryRebuild = 77
    swMaximizeDocumentOnOpen = 78
    swEditDesignTableInSeparateWindow = 80
    swEnablePropertyManager = 81
    swUseSystemSeparatorForDims = 82
    swUseEnglishLanguage = 83
    swDrawingAutomaticModelDimPlacement = 84
    swDrawingDisplayViewBorders = 85
    swAutomaticScaling3ViewDrawings = 86
    swDrawingAutomaticBomUpdate = 87
    swDrawingSelectHiddenEntities = 88
    swDrawingCreateDetailAsCircle = 89
    swAutomaticDrawingViewUpdate = 90
    swDrawingDetailInferCorner = 91
    swDrawingDetailInferCenter = 92
    swDrawingViewShowContentsWhileDragging = 93
    swSketchAlternateSplineCreation = 94
    swSketchInferFromModel = 95
    swSketchPromptToCloseSketch = 96
    swSketchCreateSketchOnNewPart = 97
    swSketchOverrideDimensionsOnDrag = 98
    swSketchDisplayPlaneWhenShaded = 99
    swSketchOverdefiningDimsPromptToSetState = 100
    swSketchOverdefiningDimsSetDrivenByDefault = 101
    swPerformanceVerifyOnRebuild = 102
    swPerformanceDynamicUpdateOnMove = 103
    swPerformanceAlwaysGenerateCurvature = 104
    swPerformanceWin95ZoomClipping = 105
    swIGESDuplicateEntities = 106
    swIGESHighTrimCurveAccuracy = 107
    swIGESExportSketchEntities = 108
    swIGESComponentsIntoOneFile = 109
    swIGESFlattenAssemHierarchy = 110
    swAlwaysUseDefaultTemplates = 111
    swUseSimpleOpenGL = 112
    swShowRefGeomName = 113
    swUseShadedPreview = 114
    swEdgesHiddenEdgeSelectionInWireframe = 115
    swEdgesHiddenEdgeSelectionInHLR = 116
    swEdgesRepaintAfterSelectionInHLR = 117
    swEdgesHighlightFeatureEdges = 118
    swEdgesDynamicHighlight = 119
    swEdgesHighQualityDisplay = 120
    swEdgesOpenEdgesDifferentColor = 121
    swEnableConfirmationCorner = 122
    swAutoShowPropertyManager = 123
    swIncontextFeatureHolderVisibility = 124
    swTransparencyHighQualityDynamic = 125
    swEdgesShadedEdgesDifferentColor = 126
    swEdgesAntiAlias = 127
    swPageSetupPrinterUsePrinterMargin = 128
    swPageSetupPrinterDrawingScaleToFit = 129
    swPageSetupPrinterPartAsmPrintWindow = 130
    swDisplayShadowsInShadedMode = 131
    swDrawingViewSmoothDynamicMotion = 132
    swDrawingEliminateDuplicateDimsOnInsert = 133
    swRapidDraftPrintOutOfSynchWaterMark = 134
    swDrawingViewAutoHideComponents = 135
    swEdgesDisplayShadedPlanes = 136
    swPlaneDisplayShowEdges = 137
    swPlaneDisplayShowIntersections = 138
    swColorsUseSpecifiedEditColors = 139
    swEnablePerformanceEmail = 141
    swSnapOnlyIfGridDisplayed = 142
    swDetailingBalloonsDisplayWithBentLeader = 143
    swBOMConfigurationLocked = 144
    swBOMConfigurationUseDocumentFont = 145
    swBOMConfigurationUseSummaryInfo = 146
    swBOMConfigurationAlignBottom = 147
    swBOMContentsDisplayAtTop = 148
    swBOMControlIdFromAssembly = 149
    swBOMControlMissingRows = 150
    swBOMControlSplitTable = 151
    swAutomaticDrawingViewUpdateDefault = 152
    swAutomaticDrawingViewUpdateForceOff = 153
    swAnnotationDisplayHideDanglingDim = 154
    swDetailingDimBreakAroundArrow = 155
    swDetailingDimensionsToleranceUseParentheses = 156
    swDetailingDimensionsToleranceUseDimensionFont = 157
    swImageQualityApplyToAllReferencedPartDoc = 158
    swPrintBackground = 159
    swEDrawingsCompression = 160
    swImportSolidSurface = 161
    swImportFreeCurves = 162
    swImport2dCurvesAs2dSketch = 163
    swLargeAsmModeAutoLoadLightweight = 166
    swLargeAsmModeUpdateMassPropsOnSave = 167
    swLargeAsmModeAutoRecover = 168
    swLargeAsmModeRemoveDetail = 169
    swLargeAsmModeHideAllItems = 170
    swLargeAsmModeDynHighlightFeatureMgr = 171
    swLargeAsmModeDynHighlightGraphicsView = 172
    swLargeAsmModeAntiAliasEdgesFastMode = 173
    swLargeAsmModeShadowsShadedMode = 174
    swLargeAsmModeTransparencyNormalViewMode = 175
    swLargeAsmModeTransparencyDynamicViewMode = 176
    swLargeAsmModeShowContentsDragDrawView = 177
    swLargeAsmModeSmoothDynamicMotionDrawView = 178
    swLargeAsmModeDrawingHLREdgesWhenShaded = 179
    swLargeAsmModeAutoHideCompsDrawViewCreation = 180
    swLargeAsmModeDrawingAutoLoadModels = 181
    swLargeAsmModeAlwaysGenerateCurvature = 182
    swImportStepConfigData = 183
    swIGESExportSolidAndSurface = 184
    swIGESExportFreeCurves = 185
    swIGESExportAsWireframe = 186
    swDetailingDimensionsAngularToleranceUseParentheses = 187
    swDetailingDimensionsToleranceFitTolUseDimensionFont = 188
    swDetailingAutoInsertCenterMarks = 189
    swDetailingAutoInsertCenterLines = 190
    swSTLPreview = 191
    swDetailingCenterMarkUseCenterLine = 192
    swMaterialPropertySolidFill = 193
    swSaveEModelData = 194
    swDisplayCurves = 195
    swDisplaySketches = 196
    swDisplayAllAnnotations = 197
    swViewDisplayHideAllTypes = 198
    swColorsUseShadedEdgeColor = 199
    swViewpointPreserveNormals = 200
    swSaveBackupFilesInSameLocationAsOriginal = 201
    swNotifySNLNotObtainedForEDrawingsSave = 202
    swPerformanceRemoveDetailDuringZoomPanRotate = 203
    swDisplayEnableSelectionThroughTransparency = 204
    swDisplayReferenceTriad = 205
    swDrawingsDefaultDisplayTypeFastHLRHLV = 206
    swDrawingsDefaultDisplayTypeHLREdgesWhenShaded = 207
    swPerformanceSave = 208
    swDetailingAutoUpdateBOM = 209
    swImageQualityUseHighQualityEdgeSize = 210
    swDrawingSaveShadedData = 211
    swEDrawingsOkayToMeasure = 212
    swBomTableKeepMissingItems = 213
    swBomTableStrikeThroughMissingItems = 214
    swRevisionTableUpdateAllLabels = 215
    swIGESImportShowLevel = 216
    swColorsMatchViewAndFeatureManagerBackground = 217
    swEDrawingsSaveShadedDataInDrawings = 218
    swDisplayReferencePoints2 = 219
    swImportMultBodyAsPartData = 220
    swEDrawingsExportSTLOkay = 221
    swDetailingDisplaySFSymbolsPer2002 = 222
    swDontCopyQTYColumnNameFromTemplate = 223
    swEDrawingsSaveAnimationOkay = 224
    swInsertViewForNewDrawing = 225
    swInsertComponentForNewAssembly = 226
    swCollabTopDocsNoPromptOrSave = 227
    swCollabEnableMultiUser = 228
    swViewSketchRelations = 229
    swDisplayShadedCosmeticThreads = 230
    swCollabAddShortcutMenuItems = 231
    swCollabCheckReadOnlyModifiedByOthers = 232
    swDisplayAllSplineHandles = 233
    swAssemblyAllowComponentMoveByDragging = 234
    swHoleTableCombineTags = 235
    swHoleTableCombineSameSize = 236
    swHoleTableHoleCentersVisible = 237
    swHoleTableAutomaticUpdate = 238
    swDetailingDimOffsetText = 239
    swDetailingDetailViewLabels_PerStandard = 240
    swDetailingDetailViewLabels_Stacked = 241
    swDetailingSectionViewLabels_PerStandard = 242
    swDetailingSectionViewLabels_Stacked = 243
    swDetailingAuxViewLabels_PerStandard = 244
    swDetailingAuxViewLabels_Stacked = 245
    swExportVrmlAllComponentsInSingleFile = 246
    swDetailingAutoInsertBalloons = 247
    swDetailingAutoInsertDimsMarkedForDrawing = 248
    swSketchInference = 249
    swSketchNoSolveMove = 250
    swDetailingDimANSIBentLeader = 251
    swUnitsDualLinearRoundToNearestFraction = 252
    swUnitsDualLinearFeetAndInchesFormat = 253
    swOneConfigOnlyTopLevelBom = 254
    swImageQualitySaveTesselationWithPartDoc = 255
    swShowSheetMetalBendNotes = 256
    swDetailingCThreadDisplayHighQuality = 257
    swDetailingDimsPrefixInsideBasicTolBox = 258
    swDetailingDimsAutoJogOrdinates = 259
    swColorsWireframeHLRShadedSame = 260
    swEditMacroAfterRecord = 261
    swUseEnglishLanguageFeatureNames = 262
    swDrawingDisplayArcCenterPoints = 263
    swDrawingDisplayEntityPoints = 264
    swDrawingPrintBreaklinesInBrokenView = 265
    swSketchSnapsPoints = 266
    swSketchSnapsCenterPoints = 267
    swSketchSnapsMidPoints = 268
    swSketchSnapsQuadrantPoints = 269
    swSketchSnapsIntersections = 270
    swSketchSnapsNearest = 271
    swSketchSnapsTangent = 272
    swSketchSnapsPerpendicular = 273
    swSketchSnapsParallel = 274
    swSketchSnapsHVLines = 275
    swSketchSnapsHVPoints = 276
    swSketchSnapsLength = 277
    swSketchSnapsGrid = 278
    swSketchSnapToGridIfDisplayed = 279
    swSketchSnapsAngle = 280
    swPerformanceSheetMetalIgnoreSelfIntersect = 281
    swExternalReferencesDisable = 282
    swFileExplorerShowMyDocuments = 283
    swFileExplorerShowMyComputer = 284
    swFileExplorerShowMyNetworkPlaces = 285
    swFileExplorerShowRecentDocuments = 286
    swFileExplorerShowHiddenReferencedDocuments = 287
    swFileExplorerShowSamples = 288
    swBomTableDontAddQTYNextToConfigName = 289
    swImportAutoRunImportDiagnosticsPersist = 290
    swImportAutoRunImportDiagnostics = 291
    swQuickTipsPart = 292
    swQuickTipsAssembly = 293
    swQuickTipsDrawing = 294
    swSketchLineLengthVirtualSharp3d = 295
    swSketchShowSplineControlPolygon = 296
    swLargeAsmModeEnabled = 297
    swLargeAsmModeSuspendAutoRebuild = 298
    swLargeAsmModeUseHLREdgesInShaded = 299
    swFourViewportProjectionType = 300
    swImportIDFAddDrilledHoles = 301
    swImportIDFReverseUndersideComponents = 302
    swImportStlVrmlTextureInformation = 303
    swImportUGToolBodies = 304
    swDxfUseSolidworksLayers = 305
    swDisplayRelationsShowPropertyManager = 306
    swReferenceTriadUseAlternateLabels = 307
    swDetailingAutoInsertCenterMarksForHoles = 308
    swDetailingAutoInsertCenterMarksForFillets = 309
    swDetailingScaleWithDimHeight = 310
    swDetailingScaleWithSectionTextHeight = 311
    swUserEnableAutoFix = 312
    swDisplayLights = 313
    swDisplayCameras = 314
    swDxfEndPointMerge = 316
    swPerformancePreviewDuringOpen = 317
    swImportDxfDimsToPartSketch = 318
    swAutoSaveEnable = 319
    swBackupEnable = 320
    swBackupRemoveEnable = 321
    swSaveReminderEnable = 322
    swPDFExportInColor = 323
    swPDFExportEmbedFonts = 324
    swPDFExportHighQuality = 325
    swPDFExportPrintHeaderFooter = 326
    swPDFExportUseCurrentPrintLineWeights = 327
    swSketchShadowDrag = 328
    swWarnSaveUpdateErrors = 329
    swEnablePerformanceFeedback = 330
    swShowDrawingViewPalette = 331
    swDisplayDimensionsFlatToScreen = 332
    swPerformanceAlwaysResolveSubassemblies = 333
    swWarnSavingReferencedDoc = 334
    swFeatureManagerTransparentFlyout = 335
    swDetailingDimsShowBroken = 336
    swDetailingDetailViewLabels_AboveView = 337
    swDetailingSectionViewLabels_AboveView = 338
    swDetailingAuxViewLabels_AboveView = 339
    swPreserveRedundantGeometry = 340
    swTranslateNameAttribFromKernelBody = 341
    swPageSetupHighQuality = 345
    swSketchShowSplineOuterComb = 346
    swViewShowAnnotationLinkErrors = 347
    swViewShowAnnotationLinkVariables = 348
    swHideUnitsOfLengthValues = 349
    swShowNewsFeedsInTaskPane = 350
    swViewReverseWheelZoomDirection = 351
    swDrawingMarkAllDimensionsForDrawing = 352
    swDrawingShowSheetFormatDialog = 353
    swDrawingSheetBackgroundAsPicture = 354
    swDisplayNotesFlatToScreen = 355
    swDisplayMissingRefsWhenEditFeature = 356
    swSearchWhileTyping = 357
    swDxfExportSplinesAsSplines = 358
    swDetailingDimsFollowDimXpertLayout = 359
    swDisplayDimXpertDimensions = 360
    swDetailingShowHaloAroundAnnotation = 361
    swDetailingImportEntireAssemblyAnnotations = 362
    swSearchIncludeContentCentral = 363
    swUserEnablePlasticsMode = 364
    swDrawingDisableNoteDimensionInference = 365
    swEDrawingsSaveAnimationToAllConfigs = 366
    swEDrawingsSaveAnimationRecalculate = 367
    swPromptForAutoMateFlip = 368
    swViewZoomFitAndCenter = 369
    swDisplayCameraFOVBox = 370
    swSketchAcceptNumericInput = 372
    swDisableWeldmentConfigStrings = 373
    swDisplayLiveSections = 374
    swDetailingAnnotationUseBentLeaders = 375
    swDetailingBalloonUseDocBentLeaderLength = 376
    swDetailingGtolUseDocBentLeaderLength = 377
    swDetailingNoteUseDocBentLeaderLength = 378
    swDetailingSFSymbolUseDocBentLeaderLength = 379
    swDetailingShowDualDimensionUnits = 380
    swDetailingOrdinateDisplayAsChain = 382
    swDetailingDatumsAnchorFilled = 383
    swDetailingDatumsAnchorShoulder = 384
    swEDrawingsSaveBOM = 385
    swClearanceShowIgnored = 386
    swClearanceIgnoreEqual = 387
    swClearanceSubAssyAsComp = 388
    swClearanceCreateFasteners = 389
    swClearanceMakeTransparent = 390
    swClearanceDisplayOption = 391
    swStopDebuggingVstaOnExit = 392
    swOverrideQuantityColumnName = 393
    swAutoSizePropertyManager = 394
    swUserEnablePlasticsMode2 = 395
    swStepExportSplitPeriodic = 396
    swStepExportFaceEdgeProps = 397
    swSATExportSplitPeriodic = 398
    swSATExportFaceEdgeProps = 399
    swDXFHighQualityExport = 400
    swDetailingNotesLeaderJustificationSnapping = 401
    swDetailingAutoInsertCenterMarksForSlots = 402
    swStepExportConfigurationData = 403
    swImageQualityZoomToFitForPreviewImages = 404
    swTiffPrintAllSheets = 405
    swTiffPrintUseSheetSize = 406
    swDrawingAutoSpaceDimsOnDelete = 407
    swDetailingTablesUseTemplateSettings = 408
    swSaveNewComponentsToExternalFile = 409
    swDoublePrimeMark = 410
    swDrawingHideEnds = 411
    swCenterLineMarkLinear = 412
    swCenterLineMarkCircular = 413
    swCenterLineMarkEndsOnlyLinear = 414
    swCenterLineMarkEndsOnlyCircular = 415
    swPreciseRenderingOfOverlappingGeometry = 416
    swEnableMouseGestures = 417
    swPartExportFlatPattern = 418
    swHoleTableReuseDeleted = 419
    swHoleTableAddNewAtEnd = 420
    swFlatPatternOpt_SimplifyBends = 421
    swFlatPatternOpt_CornerTreatment = 422
    swSATExportMultLumpsToSingleBody = 423
    swPartDimXpertBlockTolerance = 424
    swPartDimXpertLocationInclinedPlane = 425
    swPartDimXpertChainHoleDimensionChain = 426
    swPartDimXpertChainPocketDimensionChain = 427
    swPartDimXpertGeometricApplyMMC = 428
    swPartDimXpertGeometricCreateBasicDimension = 429
    swPartDimXpertGeometricBasicDimensionChain = 430
    swPartDimXpertGeometricPositionAtMMC = 431
    swPartDimXpertGeometricPositionComposite = 432
    swPartDimXpertGeometricSurfaceProfileComposite = 433
    swPartDimXpertDisplayEliminateDuplicates = 434
    swPartDimXpertDisplayShowInstanceCount = 435
    swDisplayPlaneSections = 436
    swDisplaySimulationSymbol = 437
    swStoreImagesWithModel = 438
    swImageQualityUseOldTangentEdgeDisplay = 439
    swAddDimensionsToSketchEntity = 440
    swDetailingOrthoViewLabels_PerStandard = 441
    swDetailingOrthoViewLabels_AboveView = 442
    swDetailingOrthoViewLabelsEnableShow = 443
    swUseModelColorInDrawings = 444
    swDetailingShowDimensionUnits = 445
    swUseFolderAsDefaultSearchLocation = 446
    swDetailingAutoInsertCenterMarksForHolesAsm = 447
    swDetailingAutoInsertCenterMarksForFilletsAsm = 448
    swDetailingAutoInsertCenterMarksForSlotsAsm = 449
    swTableHoleDualDimensionDisplay = 450
    swTableHoleShowUnitsForDualDisplay = 451
    swDXFExportHiddenLayersOn = 452
    swDXFExportHiddenLayersWarnIsOn = 453
    swDetailingLinkParentViewConfiguration = 454
    swLockRecentDocumentsList = 455
    swDxfAllSheetsToPaperSpace = 456
    swFlatPatternOpt_DisableSplitters = 457
    swFlatPatternOpt_WhenFlattenedShowPunches = 458
    swFlatPatternOpt_WhenFlattenedShowProfiles = 459
    swFlatPatternOpt_WhenFlattenedShowCenters = 460
    swUserEnableFreezeBar = 461
    swAddDimensionsToLineEntity = 462
    swAddDimensionsToRectangleEntity = 463
    swAddDimensionsToArcEntity = 464
    swAddDimensionsToCircleEntity = 465
    swAddDimensionsToSlotEntity = 466
    swUseChangedDimensions = 467
    swImportDoclessModelInAssem = 468
    swAddDrivenDimensions = 469
    swExtRefShowXInFeatureTree = 470
    swLargeAsmModeUseLargeDesignReview = 471
    swTablePunchShowUnitsForDualDisplay = 472
    swPunchTableCombineTags = 473
    swPunchTableCombineSameSize = 474
    swFlatPatternOpt_ShowGrainDirection = 475
    swFlatPatternOpt_ShowFixedFace = 476
    swAutoNormalToSketchMode = 477
    swUseSpeedpakModelColorInDrawings = 478
    swTablePunchDualDimensionsDisplay = 479
    swDrawingEliminateDuplicateModelNotesOnInsert = 480
    swDrawingDisableNoteMergeWhenDragging = 481
    swDrawingReuseViewLettersFromDeletedAuxilary = 482
    swFeatureManagerEnableTreeFilter = 483
    swDxfExportAllSheetsToPaperSpace = 484
    swDisplayAmbientOcclusionShadows = 485
    swDraftQualityAmbientOcclusion = 486
    swQuickViewTransparencyEnabled = 487
    swQuickViewTransparencyDynamic = 488
    swDetailingDimsShowLeadingZeros = 489
    swHoleTableShowAnsiInchSize = 490
    swSaveWithoutCostingData = 491
    swLoadEnvelopeLightweight = 492
    swLoadEnvelopeReadOnly = 493
    swDetailingSectionHideShoulders = 494
    swLargeAsmModeDismissAutoUpdate = 495
    swStepExport3DCurveFeatures = 497
    swDetailingAutoInsertDowelSymForHolesPart = 499
    swDetailingAutoInsertDowelSymForHolesAsm = 500
    swDetailingDimsApplyUpdatedRules = 501
    swDetailingAngularRunningDisplayAsChain = 502
    swDetailingAngularRunningExtensionLineExtend = 5030
    swDetailingAngularRunningRunBidirectionally = 504
    swDetailingDimsAutoJogAngularRunning = 505
    swDetailingLinearDimPrecisionLinkWithModel = 506
    swDetailingAltLinearDimPrecisionLinkWithModel = 507
    swDetailingDisplayDualBasicDimensionInOneBox = 509
    swAutoScaleTextureSFDecalsToModelSize = 510
    swLargeAsmModeAutoCheckUpdateAllComponents = 511
    swDisplaySpeedpakGraphicsCircle = 512
    swSheetMetalBendNotesUseDocLeaderLength = 513
    swSheetMetalBendNotesLeaderJustificationSnapping = 514
    swEnableSoundsForSolidWorksEvents = 515
    swSearchShowSolidWorksSearchBox = 516
    swSearchDissectionScheduleDaily = 517
    swDrawingDisplaySketchHatchBehindGeometry = 518
    swDetailingRadialDimsDisplayWithSolidLeader = 519
    swSketchCreateDimensionOnlyWhenEntered = 520
    swPurgeAllBodiesForNonActiveConfigurations = 521
    swDetailingAutoInsertDowelSymbols = 522
    swDetailingAutoInsertDowelSymbolsAsm = 523
    swSaveReminderAutoDismissEnable = 524
    swDrawingDisplaySketchPicturesOnSheetBehindGeometry = 525
    swDetailingShowUnitsForDualDisplay = 526
    swImageQualityWireframeHighCurveQuality = 527
    swDetailingCenterOfMassScaleByView = 528
    swDisplayCenterOfMassSymbol = 529
    swTiffPrintPadText = 530
    swUpdateExternFilesDispList = 531
    swDrawingsDefaultDisplayTypeHLREdgeQualityWhenShaded = 532
    swDrawingSheetsUseDifferentSheetFormat = 533
    swDetailingMiscView_PerStandard = 534
    swDetailingMiscView_AboveView = 535
    swDetailingMiscView_AddViewLabelOnViewCreation = 536
    swDetailingHighlightElements = 537
    swDetailingAllUpperCase = 538
    swDetailingMiscView_RemoveSpaceInScale = 539
    swWarnStartingSketchInContextAssembly = 540
    swDetailingAuxView_SimplifiedDetailed = 541
    swDetailingAuxView_RemoveSpaceInScale = 543
    swDetailingAuxView_RotateViewToHorizontalSheet = 544
    swDetailingAuxView_RotateClockwiseCounterclockwise = 545
    swEdgeQualityShadedEdgeViews = 546
    swDetailingSectionView_RemoveSpaceInScale = 549
    swColorUseSelectedItemColorsSeedsPatterns = 550
    swDimensionsExtensionLineStyleSameAsLeader = 551
    swDraftingStandardUppercase = 552
    swEdgeQualityWireframeHiddenViews = 553
    swDetailingSplitWhenTextIsSolidLeaderAligned = 555
    swEdgesDefaultBulkSelection = 556
    swDisplayPatternInformationTooltips = 557
    swAssemblyUpdateModelGraphicsWhenSavingFiles = 558
    swDetailingOrthoView_AddViewLabelOnViewCreation = 559
    swDetailingOrthoView_RemoveSpaceInScale = 560
    swDetailingSplitDualDimensions = 561
    swDetailingDetailView_RemoveSpaceInScale = 562
    swEdgesShadedModeDisplayOptimizeForThinParts = 563
    swWhileOpeningAssembliesAutoDismissMessages = 564
    swDetailingMiscView_DisplayLabelAboveView = 565
    swDetailingSplitTextDualDimensions = 566
    swDetailingOrthoView_DisplayLabelAboveView = 567
    swIGESExportSplitPeriodic = 568
    swRebuildSaveNewConfig = 569
    swTextSizeUseOperatingSystemScale = 570
    swPageSetupScaleDraftEdges = 571
    swWeldmentEnableAutomaticCutList = 572
    swWeldmentEnableAutomaticUpdate = 573
    swDisplayCompAnnotations = 575
    swShowZoneLines = 576
    swDetailingAngDimensionsRemoveInsignificantZeros = 577
    swShowMateReferenceErrors = 578
    swDetailingDimensionsToleranceInwardRounding = 579
    swDetailingNoDimSpecificOptionSpecified = 580
    swPDFExportIncludeLayersNotToPrint = 581
    swEDrawingsIncludeLayersNotToPrint = 582
    swTIFIncludeLayersNotToPrint = 583
    swSketchAddConstToRectEntity = 584
    swSketchAddConstLineDiagonalType = 585
    swDisableDerivedConfigurations = 586
    swFlatPatternOpt_WhenFlattenedShowGussetProfiles = 587
    swFlatPatternOpt_WhenFlattenedShowGussetCenters = 588
    swImportSLDXMLImportSketchData = 591
    swImportSLDXMLImportMechanismSketchObjectsAsBlocks = 592
    swAMFCompression = 593
    swAMFMaterials = 594
    swAMFColors = 595
    swEnhanceSmallFaceSelectionPrecision = 596
    swWeldmentRenameCutlistDescriptionPropertyValue = 597
    swDetailingLocationLabelAddSameSheetNumber = 598
    swDetailingConnectionLinesHolePatternsCenterMarks = 599
    swDetailingAuxView_IncludeLocationLabelsForNewViews = 600
    swDetailingDetailView_IncludeLocationLabelsForNewViews = 601
    swDetailingSectionView_IncludeLocationLabelsForNewViews = 602
    swDrawingSheetsListNumFirstInZoneCallout = 603
    swDrawingSheetsContinueColumnIteration = 604
    swDrawingEnableSymbolAddingNewRevision = 605
    swImportSLDXMLImportAssemblyMatesData = 606
    swNoteParagraphAutoNumbering = 607
    swBreakAlignWithParent = 608
    swShowAnnotationInAnnotationViews = 609
    swPrintGrid = 610
    swPrintZoneLines = 611
    swShowToolboxFavoritesFolder = 612
    swDetailingCenterMarkScaleByViewScale = 613
    swDrawingSheetsMatchCustomPropVals = 614
    swSaveAsmAsPartPreserveIDs = 615
    swHideShowSketchDimensions = 616
    swPDFViewOnSave = 617
    swDisplayDatumCoordSystems = 618
    swMakeFirstSelectionTransparentInMateDialog = 619
    swMatchConfigurationNames = 620
    swDetailingLinearForeshortenedAutomatic = 621
    swDetachSegmentOnDragMode = 622
    swDetailingDiameterForeshortenedAutomatic = 623
    swShowBreadcrumbsOnSelection = 624
    swDetailingShowPeriodWithBorders = 625
    swDetailingBorderDoubleLine = 628
    swDetailingBorderShowZoneDividers = 629
    swDetailingBorderShowColumns = 630
    swDetailingBorderShowRows = 631
    swPointAxisCoordSystemHideNames = 632
    swFeatureManagerEnableRenamingComponent = 633
    swDynamicReferenceVisualization_Parent = 634
    swDynamicReferenceVisualization_Child = 635
    sw3MFAppearances = 636
    sw3MFMaterials = 637
    sw3MFDecals = 638
    swForceEnableImportDiagnosis = 639
    swDisplayCounterpartLocationLabel = 640
    swExtRefLoadRefDocsInMemory = 641
    swScaleSketchOnFirstDimension = 642
    sw3MFShowInfoOnSave = 643
    swExtRefIncludeSubFolders = 644
    swExtRefExcludeActiveFoldersAndRecentSaveLocations = 645
    swSheetMetalOverrideTemplateParam = 646
    swSheetMetalOverrideTemplateAllowance = 647
    swSheetMetalOverrideTemplateRelief = 648
    swShadedSketchContours = 650
    swDetailingRadialDimsDisplayNearSideMessages = 651
    swCollabAddTimeStampToComments = 652
    swCollabShowCommentsInPropertyManager = 653
    swDetailingScaleForJaggedStyle = 654
    swDetailingDetailViewLabels_ScaleForJaggedOutline = 655
    swFeatureManagerEnablePreviewHiddenComponents = 656
    swWeldmentCollectIdenticalBodies = 657
    swLargeAsmModePreviewHiddenComponent = 658
    swLargeAsmModeVerificationOnRebuild = 659
    swLargeAsmModeImageQualityPerfomance = 660
    sw3DPDFCompressLossyTessellation = 661
    swDisplayDecals = 662
    swDisplayPartingLines = 663
    swDisplaySketchPlanes = 664
    swDisplayWeldBead = 665
    swIFCOmniClassPreference = 666
    swIFCUniClass2Preference = 667
    swIFCCustomPropsPreference = 668
    swIFCMaterialsMassPropertiesPreference = 669
    swDisplayEquationIds = 670
    swMagMatePreAlign = 671
    swOptimizeMatePlacement = 672
    swPdfIncludeBookmarks = 673
    swDisplayGraphicsComponents = 675
    swDraftingStandardAllUppercaseForTable = 676
    swTransferHoleWizardSizeComboBoxSettings = 677
    swAssemblyAllowCreationOfMisalignedMates = 678
    swVrmlStlImportAsPSMesh = 679
    swSolidBBoxDescriptionUseDefault = 680
    swSheetMetalBodiesDescriptionUseDefault = 681
    swVrmlStlImportSegmented = 682
    swEnableVSTAVersion3 = 683
    swViewDispGlobalBBox = 684
    swDisplayComponentDimXpertAnnotations = 685
    swImportNeutral_SolidandSurface = 686
    swImportNeutral_FreeCurvesAndPoints = 687
    swImportNeutralReferencePlane = 688
    swImportNeutral_AttributesAndProperties = 689
    swImportNeutralRunDiagnostics = 690
    swMultiCAD_Enable3DInterconnect = 691
    swDrawingTurnOffAutomaticSolveModeAndUndo = 692
    swSketchTurnOffAutomaticSolveModeAndUndo = 693
    swImportSolidBody = 694
    swImportSurfaceBody = 695
    swImportReferencePlane = 696
    swImportReferenceAxis = 697
    swImportUnconsumedSketchesAndCurves = 698
    swImportCustomProperties = 699
    swImportMaterialProperties = 700
    swImportDissolveTopLevelAssemblyOnOpen = 701
    swImportIgnoreHiddenEntities = 702
    swImportToolBodiesFromUGNX = 703
    swIncludePMI = 704
    swAssemblyAllowGraphicsComponent = 705
    swCheckCrashSolutions = 706
    swMakeTrimEntityConstruction = 707
    swIgnoreConstructionEntity = 708
    swLockRotationConcentricMates = 709
    swASMSLDPRT_ExcludeComponentsByVisibility = 710
    swASMSLDPRT_ExcludeComponentsByBBoxVolume = 712
    swASMSLDPRT_ExcludeIfToolboxComponents = 713
    swASMSLDPRT_IncludeMassProperties = 716
    swEnableAllowCosmeticThreadsUpgrade = 718
    swSheetMetalUseMaterial = 719
    swPDFExportShadedEdgesHighQuality = 720
    swBomTableShowCustomTextinBOMHeader_ForTopLevelOnlyBOM = 721
    swBomTableShowCustomTextinBOMHeader_ForPartOnlyBOM = 722
    swBomTableShowCustomTextinBOMHeader_ForIndentedBOM = 723
    swBomTableShowConfigurationInBOMHeader_ForTopLevelOnlyBOM = 724
    swBomTableShowConfigurationInBOMHeader_ForPartOnlyBOM = 725
    swBomTableShowConfigurationInBOMHeader_ForIndentedBOM = 726
    swEdit3DPDFTemplate = 727
    swPLYBinaryFormat = 728
    swPLYPreview = 729
    swPLYIncludeColors = 730
    swDisplayScrollbarsInGraphicsViewDrawings = 731
    swDisplayScrollbarsInGraphicsViewPartsAndAssemblies = 732
    swShowBreadcrumbsAtMousePointer = 733
    swIncludeDocumentsOpenedFromOtherDocuments = 734
    swIncludeSubfoldersForDrawingsSearchInPackAndGo = 735
    swAutomaticallyPopupSelectionToolForPreciseLocation = 736
    swCombineCutlistItemsInBOM = 737
    swEditNameWithSlowDoubleClick = 738
    swSheetMetalMBDDisplaySheetMetalBendNotes = 739
    swSheetMetalMBDUseDocumentLeaderLength = 740
    swSheetMetalMBDLeaderJustificationSnapping = 741
    swSheetMetalMBDShowFixedFace = 742
    swSheetMetalMBDShowGrainDirection = 743
    swSheetMetalMBDFormat = 744
    swEnablePerformancePipeline = 745
    swReferenceOnlyEnvelopeComponentType = 746
    swReferenceInContextOfTopLevelAssembly = 747
    swDisplayDataMarkNewConfig = 749
    swAllowCreationOfReferencesExternalToModel = 750
    swDetailingAnnotationShowTypeInThreadCallouts = 751
    swDetailingChainDimensionAddOverallDimensions = 752
    swDetailingChainDimensionAddLastReferenceDimension = 753
    swDraftingStandardAllUppercaseForDimensionsAndHoleCallouts = 754
    swBackupAfterMeshOrRunSimulationStudy = 755
    swIncludeDataForDelmia = 756
    swWeldmentGenerateCutlistIDs = 757
    swMultiCAD_ApplyOnlyToParts = 758
    swMultiCAD_CreateNewComponentsAsExternalFiles = 759
    swFeatureManagerShowTranslatedNameInFMTree = 760
    swAutomaticSyncSettings = 761
    swAutoSyncSettingsToInclude_SystemOptions = 762
    swAutoSyncSettingsToInclude_FileLocations = 763
    swAutoSyncSettingsToInclude_Customizations = 764
    swEnable3DEXPERIENCEIntegration = 765
    swShowCADFamilyConfigOnly3dexpIntegration = 766
    swShowCADAndOtherConfig3dexpIntegration = 767
    swEnable3DEXPERIENCEFileCompatibilityUpdate = 768
    swImportNeutralAnalyticalConversion = 769
    swUsePositiveInertiaTensorNotation = 770
    swDisplayBendLines = 771
    swTIFExportIncludeDrawingsPaperColor = 772
    swPDFExportIncludeDrawingsPaperColor = 773
    swSaveFileProperties = 774
    swSaveFilePropertiesForEachComp = 775
    swIncludeSketchData = 776
    swSystemNotificationHideGraphicsNotification = 778
    swDetailingModeSaveModelData = 779
    swDetailingModeIncludeStandardViewsInViewPalette = 780
    swStoreOLEImagesWithModel = 781
    swDetailingAnnotationApplyNewCTDepthArchForToNewParts = 782
    swCreateConfigurationTableOnOpen = 783
    swExtRefForceSaveToCurrentVersion = 784
    swDisplayTempAxesOnMouseHover = 785
    swStepExportAtomicSave = 786
    swStepExportAppearances = 787
    swDisplayMeshBREPFacetFins = 788
    swEdgesDefaultBulkSelection2 = 789
    swWeldmentUseEnglishDescriptionNameInCutlist = 790
    swMultiCAD_3DInterconnectMaintainLinks = 791
    swMultiCAD_3DInterconnectManualBreakLink = 792
    swMultiCAD_3DInterconnectLinksFlag = 793
    swSketchPreviewDimensionOnSelect = 794
    swCollinearChainDimensionOffsetText = 795
    swCollinearChainDimensionArrowHeadTermination = 796
    swHardwareAccSilhouetteEdges = 797
    swDispDimXpertDimOnTopOfModel = 798
    swDimOverriddenHighlight = 799
    swSketchSuppressedDimProfileErrorOption = 800
    swDisplayTopLevelEnvelopes = 801
    swDisplayComponentEnvelopes = 802
    swDisplayMarkups = 803
    swDisplayMotionSymbol = 804
    swDrawingOpenInDetailingMode = 805
    swDxfExportViewAsBlock = 806
    swDetailingAutoInsertCosmeticThreadForHolesAsm = 807
    swSpeedpakUpdateSlider = 808
    swNoteZoomToFit = 809
    swIFCExportUsePropertySetMappingFile = 810
    swSheetMetalDimensionFlangeSketch = 811
    swSeeThroughTransparentComponents = 812
    swDisplayCartoon = 813
    swDisplayRealViewGraphics = 814
    swSMGExportSWBOM = 815
    swSMGExportSWAssemEnvelope = 816
    swSMGExportSWAppearance = 817
    swSMGExportSWDecals = 818
    swSMGExportSWExplodedAndSavedViews = 819
    swSMGExportSWPMI = 820
    swPMIOverwriteColor = 821
    swSMGMergeFileIntoOneActorPerPart = 822
    swSMGExportInstanceNames = 823
    swSMGExportMetaProps = 824
    swSMGOverloadAssemTreeNames = 825
    swSMGExportAsBodies = 826
    swSMGExportFreeFaces = 827
    swSMGExportHiddenCompNOSHOW = 828
    swAbsChordalError = 829
    swAbsNormalDeviation = 830
    swAbsEdgeLength = 831
    swSMGEnableHealing = 832
    swGenerateCutlistIDsInDocUnits = 833
    swAutoResolveLightweightCompUponExpInFMTree = 834
    swViewShowAnnotationTextExpression = 835
    swOverrideTreeDisplaySysSettings = 836
    swSecondaryComponentDescription = 837
    swSecondaryConfigurationName = 838
    swSecondaryConfigurationDescription = 839
    swTertiaryDisplayStateName = 840
    swDoNotShowConfigOrDisplayStateName = 841
    swSecondaryPhysicalProductDescription = 842
    swSecondaryEnterpriseItemNumber = 843
    swTertiaryFileTitle = 844
    swTertiaryRevision = 845
    swAssemblyEnableCreationOfMatesUsingAI = 846
    swDisplayDspbrAppearances = 847
    swShowDismissedMessagesIconInStatusBar = 848
    swWarnOnDupCompRefsForDlg = 849
    swEnableInterfDetProgressDlg = 850
    swDrawingDisallowCreationOfMirrorViews = 851
    swImportPSEnableTemplates = 852
    swImportAssemblyHybrid = 853
    swEnableInterfDetMultiThread = 854
    swEnableSaveToVersion = 855
    swFamilyTableDimName = 856

class swUserPreferencesLanguages_e(IntEnum):
    """swUserPreferencesLanguages_e (14 constants, from SwConst)."""
    swLang_Chinese = 0
    swLang_Chinese_Simplified = 1
    swLang_Czech = 2
    swLang_English = 3
    swLang_French = 4
    swLang_German = 5
    swLang_Italian = 6
    swLang_Japanese = 7
    swLang_Korean = 8
    swLang_Polish = 9
    swLang_Portuguese_Brazilian = 10
    swLang_Russian = 11
    swLang_Spanish = 12
    swLang_Turkish = 13

class swUserUnitsType_e(IntEnum):
    """swUserUnitsType_e (2 constants, from SwConst)."""
    swLengthUnit = 0
    swAngleUnit = 1

class swVariablePitchHelixRegionParameter_e(IntEnum):
    """swVariablePitchHelixRegionParameter_e (4 constants, from SwConst)."""
    swVariablePitchHelixRegionParameter_Revolution = 0
    swVariablePitchHelixRegionParameter_Pitch = 1
    swVariablePitchHelixRegionParameter_Height = 2
    swVariablePitchHelixRegionParameter_Diameter = 3

class swVariableRadiusFilletOptions_e(IntEnum):
    """swVariableRadiusFilletOptions_e (2 constants, from SwConst)."""
    swSmoothTransition = 0
    swStraightTransition = 1

class swVersionCompatibilityResult_e(IntEnum):
    """swVersionCompatibilityResult_e (4 constants, from SwConst)."""
    swVersionCompatibilityResult_Completed = 0
    swVersionCompatibilityResult_FailUnknown = 1
    swVersionCompatibilityResult_FailFileNotResolved = 2
    swVersionCompatibilityResult_FailInvalidVersion = 3

class swVerticalJustification_e(IntEnum):
    """swVerticalJustification_e (4 constants, from SwConst)."""
    swVerticalJustificationNone = 0
    swVerticalJustificationTop = 1
    swVerticalJustificationMiddle = 2
    swVerticalJustificationBottom = 3

class swViewAlignment_e(IntEnum):
    """swViewAlignment_e (4 constants, from SwConst)."""
    swViewAlignNone = 0
    swViewAlignedChildren = 1
    swViewAligned = 2
    swViewAlignBoth = 3

class swViewDisplayMode_e(IntEnum):
    """swViewDisplayMode_e (13 constants, from SwConst)."""
    swViewDisplayMode_Wireframe = 1
    swViewDisplayMode_HiddenLinesRemoved = 2
    swViewDisplayMode_HiddenLinesGrayed = 3
    swViewDisplayMode_Shaded = 4
    swViewDisplayMode_ShadedWithEdges = 5
    swViewDisplayMode_ShadedCurvatureOn = 6
    swViewDisplayMode_ShadedCurvatureOFF = 7
    swViewDisplayMode_StripesOn = 8
    swViewDisplayMode_StripesOff = 9
    swViewDisplayMode_PerspectiveOn = 10
    swViewDisplayMode_PerspectiveOff = 11
    swViewDisplayMode_Faceted = 12
    swViewDisplayMode_IntegratedPreview = 13

class swViewDisplayType_e(IntEnum):
    """swViewDisplayType_e (8 constants, from SwConst)."""
    swIsViewSectioned = 0
    swIsViewPerspective = 1
    swIsViewShaded = 2
    swIsViewWireFrame = 3
    swIsViewHiddenLinesRemoved = 4
    swIsViewHiddenInGrey = 5
    swIsViewCurvature = 6
    swIsViewStripe = 7

class swViewEntityType_e(IntEnum):
    """swViewEntityType_e (4 constants, from SwConst)."""
    swViewEntityType_Edge = 1
    swViewEntityType_Vertex = 2
    swViewEntityType_Face = 3
    swViewEntityType_SilhouetteEdge = 4

class swViewIndication_e(IntEnum):
    """swViewIndication_e (2 constants, from SwConst)."""
    swViewIndication_ArrowMethod = 0
    swViewIndication_SameAsSection = 1

class swViewNotify_e(IntEnum):
    """swViewNotify_e (14 constants, from SwConst)."""
    swViewRepaintNotify = 1
    swViewChangeNotify = 2
    swViewDestroyNotify = 3
    swViewRepaintPostNotify = 4
    swViewBufferSwapNotify = 5
    swViewDestroyNotify2 = 6
    swViewPerspectiveViewNotify = 7
    swViewRenderLayer0Notify = 8
    swViewUserClearSelectionsNotify = 9
    swViewPrintNotify = 10
    swViewGraphicsRenderPostNotify = 11
    swViewDisplayModeChangePreNotify = 12
    swViewDisplayModeChangePostNotify = 13
    swViewPrintNotify2 = 14

class swViewOrientationUpAxisFlyout_e(IntEnum):
    """swViewOrientationUpAxisFlyout_e (2 constants, from SwConst)."""
    swViewOrientationUpAxisFlyout_Y_Up = 0
    swViewOrientationUpAxisFlyout_Z_Up = 1

class swViewportDisplay_e(IntEnum):
    """swViewportDisplay_e (4 constants, from SwConst)."""
    swViewportSingle = 1
    swViewportTwoViewHorizontal = 2
    swViewportTwoViewVertical = 3
    swViewportFourView = 4

class swVisibilityState_e(IntEnum):
    """swVisibilityState_e (3 constants, from SwConst)."""
    swVisibilityStateHide = 1
    swVisibilityStateShown = 2
    swVisibilityStateUnknown = 3

class swVrmlOutputVersion_e(IntEnum):
    """swVrmlOutputVersion_e (2 constants, from SwConst)."""
    swVrmlOutputVersion_97 = 1
    swVrmlOutputVersion_01 = 2

class swWeldBeadSide_e(IntEnum):
    """swWeldBeadSide_e (2 constants, from SwConst)."""
    swWeldBeadArrowSide = 0
    swWeldBeadOtherSide = 1

class swWeldBeadType_e(IntEnum):
    """swWeldBeadType_e (3 constants, from SwConst)."""
    swWeldBeadTypeFull = 0
    swWeldBeadTypeIntermittent = 1
    swWeldBeadTypeStaggered = 2

class swWeldSymbolContourTypes_e(IntEnum):
    """swWeldSymbolContourTypes_e (4 constants, from SwConst)."""
    swWeldContourNone = 1
    swWeldContourFlat = 2
    swWeldContourConvex = 3
    swWeldContourConcave = 4

class swWeldSymbolField_e(IntEnum):
    """swWeldSymbolField_e (3 constants, from SwConst)."""
    swFieldWeldNone = 1
    swFieldWeldUp = 2
    swFieldWeldDown = 3

class swWeldSymbolSymmetric_e(IntEnum):
    """swWeldSymbolSymmetric_e (3 constants, from SwConst)."""
    swWeldSymmetric = 1
    swWeldDashedLineOnTop = 2
    swWeldDashedLineOnBottom = 3

class swWeldSymbolTextTypes_e(IntEnum):
    """swWeldSymbolTextTypes_e (9 constants, from SwConst)."""
    swWeldLeftTextAbove = 1
    swWeldSymbolTextAbove = 2
    swWeldRightTextAbove = 3
    swWeldStaggerTextAbove = 4
    swWeldLeftTextBelow = 5
    swWeldSymbolTextBelow = 6
    swWeldRightTextBelow = 7
    swWeldStaggerTextBelow = 8
    swWeldProcessText = 9

class swWeldmentTrimExtendOptionType_e(IntEnum):
    """swWeldmentTrimExtendOptionType_e (4 constants, from SwConst)."""
    swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim = 1
    swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim = 2
    swWeldmentTrimExtendOption_CopedCut = 4
    swWeldmentTrimExtendOption_WeldGap = 8

class swWindowState_e(IntEnum):
    """swWindowState_e (3 constants, from SwConst)."""
    swWindowNormal = 0
    swWindowMaximized = 1
    swWindowMinimized = 2

class swWireRouteError_e(IntEnum):
    """swWireRouteError_e (9 constants, from SWRoutingLib)."""
    swWireRouteError_WireNotRouted = 1
    swWireRouteError_WireSegmentsBranching = 2
    swWireRouteError_WireSegmentsDisjoint = 3
    swWireRouteError_WireMissingFromToComponent = 4
    swWireRouteError_WireMismatchedFromComponent = 5
    swWireRouteError_WireMismatchedToComponent = 6
    swWireRouteError_WireMismatchedFromPin = 7
    swWireRouteError_WireMismatchedToPin = 8
    swWireRouteError_WirePathViolatesBendRadius = 9

class swWitnessLineVisibility_e(IntEnum):
    """swWitnessLineVisibility_e (4 constants, from SwConst)."""
    swWitnessLineBoth = 0
    swWitnessLineFirst = 1
    swWitnessLineSecond = 2
    swWitnessLineNone = 3

class swWrapMethods_e(IntEnum):
    """swWrapMethods_e (2 constants, from SwConst)."""
    swWrapMethods_Analytical = 0
    swWrapMethods_SplineSurface = 1

class swWrapSketchType_e(IntEnum):
    """swWrapSketchType_e (3 constants, from SwConst)."""
    swWrapSketchType_Emboss = 0
    swWrapSketchType_Engrave = 1
    swWrapSketchType_Scribe = 2

class swWzdGeneralHoleTypes_e(IntEnum):
    """swWzdGeneralHoleTypes_e (9 constants, from SwConst)."""
    swWzdCounterBore = 0
    swWzdCounterSink = 1
    swWzdHole = 2
    swWzdPipeTap = 3
    swWzdTap = 4
    swWzdLegacy = 5
    swWzdCounterBoreSlot = 6
    swWzdCounterSinkSlot = 7
    swWzdHoleSlot = 8

class swWzdHoleAuxiliaryConstants_e(IntEnum):
    """swWzdHoleAuxiliaryConstants_e (3 constants, from SwConst)."""
    NUM_HOLE_GENERIC_TYPES = 9
    NUM_HOLE_TYPES = 91
    NUM_HOLE_STANDARD_TYPES = 249

class swWzdHoleCosmeticThreadTypes_e(IntEnum):
    """swWzdHoleCosmeticThreadTypes_e (3 constants, from SwConst)."""
    swCosmeticThreadNone = 0
    swCosmeticThreadWithCallout = 1
    swCosmeticThreadWithoutCallout = 2

class swWzdHoleCounterSinkHeadClearanceTypes_e(IntEnum):
    """swWzdHoleCounterSinkHeadClearanceTypes_e (2 constants, from SwConst)."""
    swHeadClearanceIncreasedCsink = 0
    swHeadClearanceAddToCbore = 1

class swWzdHoleHcoilTapTypes_e(IntEnum):
    """swWzdHoleHcoilTapTypes_e (2 constants, from SwConst)."""
    swTapTypePlug = 0
    swTapTypeBottom = 1

class swWzdHoleScrewClearanceTypes_e(IntEnum):
    """swWzdHoleScrewClearanceTypes_e (3 constants, from SwConst)."""
    swScrewClearanceClose = 0
    swScrewClearanceNormal = 1
    swScrewClearanceLoose = 2

class swWzdHoleStandardFastenerTypes_e(IntEnum):
    """swWzdHoleStandardFastenerTypes_e (404 constants, from SwConst)."""
    swStandardAnsiInchBinding = 0
    swStandardAnsiInchButton = 1
    swStandardAnsiInchFillister = 2
    swStandardAnsiInchHexBolt = 3
    swStandardAnsiInchHexBoltFinished = 4
    swStandardAnsiInchHexBoltHeavy = 5
    swStandardAnsiInchHexScrew = 6
    swStandardAnsiInchHexWasherScrew = 7
    swStandardAnsiInchPan = 8
    swStandardAnsiInchSocketCapScrew = 9
    swStandardAnsiInchSocketShoulderScrew = 10
    swStandardAnsiInchSquare = 11
    swStandardAnsiInchTruss = 12
    swStandardAnsiInchFlatSocket82 = 13
    swStandardAnsiInchFlatHead100 = 14
    swStandardAnsiInchFlatHead82 = 15
    swStandardAnsiInchOval = 16
    swStandardAnsiInchHcoilTapDrills = 17
    swStandardAnsiInchAllDrillSizes = 18
    swStandardAnsiInchFractionalDrillSizes = 19
    swStandardAnsiInchLetterDrillSizes = 20
    swStandardAnsiInchPipeTapDrills = 21
    swStandardAnsiInchScrewClearances = 22
    swStandardAnsiInchTapDrills = 23
    swStandardAnsiInchNumberDrillSizes = 24
    swStandardAnsiInchTaperedPipeTap = 25
    swStandardAnsiInchBottomingTappedHole = 26
    swStandardAnsiInchTappedHole = 27
    swStandardAnsiMetricButton = 28
    swStandardAnsiMetricHexBolt = 29
    swStandardAnsiMetricHexCapScrew = 30
    swStandardAnsiMetricHexScrewFormed = 31
    swStandardAnsiMetricPan = 32
    swStandardAnsiMetricSocketHeadCapScrew = 33
    swStandardAnsiMetricSocketShoulderScrew = 34
    swStandardAnsiMetricFlatSocket82 = 35
    swStandardAnsiMetricFlatHead82 = 36
    swStandardAnsiMetricOval = 37
    swStandardAnsiMetricHcoilTapDrills = 38
    swStandardAnsiMetricDrillSizes = 39
    swStandardAnsiMetricScrewClearances = 40
    swStandardAnsiMetricTapDrills = 41
    swStandardAnsiMetricBottomingTappedHole = 42
    swStandardAnsiMetricTappedHole = 43
    swStandardBSICheese = 44
    swStandardBSIHexBolt = 45
    swStandardBSIHexCapScrew = 46
    swStandardBSIHexMachineScrew = 47
    swStandardBSIPanHead = 48
    swStandardBSISocketCapScrew = 49
    swStandardBSIFlatSocketCap = 50
    swStandardBSIFlatHead = 51
    swStandardBSIOvalHead = 52
    swStandardBSIHcoilTapDrills = 53
    swStandardBSIDrillSizes = 54
    swStandardBSIScrewClearances = 55
    swStandardBSITapDrills = 56
    swStandardBSITappedHoleBottoming = 57
    swStandardBSITappedHole = 58
    swStandardBSITaperedPipeTap = 59
    swStandardDINHeavyHexBolt = 60
    swStandardDINHexFlangeBolt = 61
    swStandardDINCheeseHead = 62
    swStandardDINHexBolt = 63
    swStandardDINHexCapScrew = 64
    swStandardDINHexMachineScrew = 65
    swStandardDINPan = 66
    swStandardDINSocketHeadCap = 67
    swStandardDINSocketCTSKFlatHead = 68
    swStandardDINCTSKFlatHead = 69
    swStandardDINCTSKRaisedHead = 70
    swStandardDINHcoilTapDrills = 71
    swStandardDINDrillSizes = 72
    swStandardDINScrewClearances = 73
    swStandardDINTapDrills = 74
    swStandardDINTappedHoleBottoming = 75
    swStandardDINTappedHole = 76
    swStandardDINTaperedPipeTap = 77
    swStandardDMECCorePins = 78
    swStandardDMECXCorePins = 79
    swStandardDMETHXEjectorPins = 80
    swStandardDMEStandardLeaderPins = 81
    swStandardDMEReturnPins = 82
    swStandardDMESocketCapScrew = 83
    swStandardDMESupportPillarSHCS = 84
    swStandardDMESpruPullerPins = 85
    swStandardDMEStripperBolt = 86
    swStandardDMEFlatSocket82 = 87
    swStandardDMEFlatHead100 = 88
    swStandardDMEFlatHead82 = 89
    swStandardDMEOval = 90
    swStandardDMESupportPillarClearance = 91
    swStandardDMEFractionalDrillSizes = 92
    swStandardDMEHcoilTapDrills = 93
    swStandardDMEAllDrillSizes = 94
    swStandardDMELetterDrillSizes = 95
    swStandardDMENumberDrillSizes = 96
    swStandardDMEPipeTapDrills = 97
    swStandardDMEScrewClearances = 98
    swStandardDMECCorePinClearances = 99
    swStandardDMECXCorePinClearances = 100
    swStandardDMETHXEjectorPinClearances = 101
    swStandardDMELeaderPinClearances = 102
    swStandardDMEReturnPinClearances = 103
    swStandardDMESpruPullerPinClearances = 104
    swStandardDMETapDrills = 105
    swStandardDMEBottomingTappedHole = 106
    swStandardDMETappedHole = 107
    swStandardDMETaperedPipeTap = 108
    swStandardHascoMetricCCorePins = 109
    swStandardHascoMetricGuideBushings = 110
    swStandardHascoMetricGuidePillars = 111
    swStandardHascoMetricLocatingGuideBushings = 112
    swStandardHascoMetricLocatingGuidePillars = 113
    swStandardHascoMetricSocketCapScrew = 114
    swStandardHascoMetricShoulderScrew = 115
    swStandardHascoMetricCTSKFlatHead = 116
    swStandardHascoMetricDrillSizes = 117
    swStandardHascoMetricScrewClearances = 118
    swStandardHascoMetricCorePinClearances = 119
    swStandardHascoMetricCenteringSleeve = 120
    swStandardHascoMetricEjectorRodClearances = 121
    swStandardHascoMetricBottomingTappedHole = 122
    swStandardHascoMetricTappedHole = 123
    swStandardHcoilInchInsert10Dia = 124
    swStandardHcoilInchInsert15Dia = 125
    swStandardHcoilInchInsert20Dia = 126
    swStandardHcoilInchInsert25Dia = 127
    swStandardHcoilInchInsert30Dia = 128
    swStandardHcoilMetricInsert10Dia = 129
    swStandardHcoilMetricInsert15Dia = 130
    swStandardHcoilMetricInsert20Dia = 131
    swStandardHcoilMetricInsert25Dia = 132
    swStandardHcoilMetricInsert30Dia = 133
    swStandardISOCheeseHead = 134
    swStandardISOHexBolt = 135
    swStandardISOHexCapScrew = 136
    swStandardISOHexMachineScrew = 137
    swStandardISOPan = 138
    swStandardISOSocketHeadCap = 139
    swStandardISOSocketCTSKFlatHead = 140
    swStandardISOCTSKFlatHead = 141
    swStandardISOCTSKRaisedHead = 142
    swStandardISODrillSizes = 143
    swStandardISOScrewClearances = 144
    swStandardISOTapDrills = 145
    swStandardISOTappedHoleBottoming = 146
    swStandardISOTappedHole = 147
    swStandardISOTaperedPipeTap = 148
    swStandardJISCheeseHead = 149
    swStandardJISFillisterHead = 150
    swStandardJISButton = 151
    swStandardJISHexBolt = 152
    swStandardJISHexCapScrew = 153
    swStandardJISHexMachineScrew = 154
    swStandardJISPan = 155
    swStandardJISSocketHeadCap = 156
    swStandardJISSocketShoulderScrew = 157
    swStandardJISFlatCTSKHead = 158
    swStandardJISRaisedCTSKHead = 159
    swStandardJISDrillSizes = 160
    swStandardJISScrewClearances = 161
    swStandardJISTapDrills = 162
    swStandardJISTappedHoleBottoming = 163
    swStandardJISTappedHole = 164
    swStandardJISTaperedPipeTap = 165
    swStandardPCSReturnPins = 166
    swStandardPCSCorePins = 167
    swStandardPCSEjectorPins = 168
    swStandardPCSStandardLeaderPins = 169
    swStandardPCSSocketCapScrew = 170
    swStandardPCSStripperBolt = 171
    swStandardPCSSupportPillarSHCS = 172
    swStandardPCSFlatHead100 = 173
    swStandardPCSFlatHead82 = 174
    swStandardPCSOval = 175
    swStandardPCSFlatSocket82 = 176
    swStandardPCSHcoilTapDrills = 177
    swStandardPCSFractionalDrillSizes = 178
    swStandardPCSNumberDrillSizes = 179
    swStandardPCSPipeTapDrills = 180
    swStandardPCSScrewClearances = 181
    swStandardPCSAllDrillSizes = 182
    swStandardPCSEjectorPinClearances = 183
    swStandardPCSLetterDrillSizes = 184
    swStandardPCSSupportPillarClearances = 185
    swStandardPCSCorePinClearances = 186
    swStandardPCSLeaderPinClearances = 187
    swStandardPCSReturnPinClearances = 188
    swStandardPCSTapDrills = 189
    swStandardPCSBottomingTappedHole = 190
    swStandardPCSTappedHole = 191
    swStandardPCSTaperedPipeTap = 192
    swStandardProgressiveSocketCapScrew = 193
    swStandardProgressiveReturnPins = 194
    swStandardProgressiveCorePins = 195
    swStandardProgressiveEjectorPins = 196
    swStandardProgressiveSpruePullerPins = 197
    swStandardProgressiveSupportPillarSHCS = 198
    swStandardProgressiveStripperBolt = 199
    swStandardProgressiveStandardLeaderPins = 200
    swStandardProgressiveFlatSocket82 = 201
    swStandardProgressiveOval = 202
    swStandardProgressiveFlatHead100 = 203
    swStandardProgressiveFlatHead82 = 204
    swStandardProgressiveHcoilTapDrills = 205
    swStandardProgressiveFractionalDrillSizes = 206
    swStandardProgressiveNumberDrillSizes = 207
    swStandardProgressivePipeTapDrills = 208
    swStandardProgressiveScrewClearances = 209
    swStandardProgressiveAllDrillSizes = 210
    swStandardProgressiveEjectorPinClearances = 211
    swStandardProgressiveLetterDrillSizes = 212
    swStandardProgressiveSupportPillarClearances = 213
    swStandardProgressiveCorePinClearances = 214
    swStandardProgressiveLeaderPinClearances = 215
    swStandardProgressiveSpruePullerPinClearances = 216
    swStandardProgressiveReturnPinClearances = 217
    swStandardProgressiveTapDrills = 218
    swStandardProgressiveTappedHole = 219
    swStandardProgressiveBottomingTappedHole = 220
    swStandardProgressiveTaperedPipeTap = 221
    swStandardSuperiorReturnPins = 222
    swStandardSuperiorEjectorPins = 223
    swStandardSuperiorSpruePullerPins = 224
    swStandardSuperiorSupportPillarSHCS = 225
    swStandardSuperiorStripperBolt = 226
    swStandardSuperiorSocketCapScrew = 227
    swStandardSuperiorStandardLeaderPins = 228
    swStandardSuperiorFlatHead100 = 229
    swStandardSuperiorFlatHead82 = 230
    swStandardSuperiorOval = 231
    swStandardSuperiorFlatSocket82 = 232
    swStandardSuperiorHcoilTapDrills = 233
    swStandardSuperiorFractionalDrillSizes = 234
    swStandardSuperiorNumberDrillSizes = 235
    swStandardSuperiorPipeTapDrills = 236
    swStandardSuperiorScrewClearances = 237
    swStandardSuperiorAllDrillSizes = 238
    swStandardSuperiorEjectorPinClearances = 239
    swStandardSuperiorLetterDrillSizes = 240
    swStandardSuperiorSupportPillarClearances = 241
    swStandardSuperiorLeaderPinClearances = 242
    swStandardSuperiorSpruePullerPinClearances = 243
    swStandardSuperiorReturnPinClearances = 244
    swStandardSuperiorTapDrills = 245
    swStandardSuperiorTappedHole = 246
    swStandardSuperiorBottomingTappedHole = 247
    swStandardSuperiorTappedHole2 = 247
    swStandardSuperiorBottomingTappedHole2 = 249
    swStandardSuperiorTaperedPipeTap = 248
    swStandardDINHexSocketHead6912 = 249
    swStandardDINStraightPipeTappedHole = 250
    swStandardDINConduitTappedHole = 351
    swStandardDINEnsatTappedHoleforAL = 352
    swStandardDINEnsatTappedHoleforCU = 353
    swStandardDINEnsatTappedHoleforST = 354
    swStandardGBDrillSizes = 355
    swStandardGBScrewClearances = 356
    swStandardGBTapDrills = 357
    swStandardGBTappedHoleBottoming = 358
    swStandardGBTappedHole = 359
    swStandardGBTaperedPipeTap = 360
    swStandardGBHexagonSocketHeadCapScrews = 361
    swStandardGBHexagonLobularSocketCountersunkHeadScrews = 362
    swStandardGBHexagonLobularSocketRaisedCountersunkHeadScrews = 363
    swStandardGBHexagonLobularSocketHeadCapScrewsPropertyClass = 364
    swStandardGBSlottedRaisedCountersunkHeadScrews = 365
    swStandardGBSlottedCountersinkHeadWoodScrews = 366
    swStandardGBSlottedRaisedCountersunkHeadWoodScrews = 367
    swStandardGBCrossRecessedCountersunkHeadWoodScrews = 368
    swStandardGBCrossRecessedRaisedCountersunkHeadWoodScrews = 369
    swStandardGBSlottedCountersunkHeadTappingScrews = 370
    swStandardGBSlottedRaisedCountersunkHeadTappingScrews = 371
    swStandardGBCrossRecessedCountersunkHeadTappingScrews = 372
    swStandardGBCrossRecessedRaisedCountersunkHeadTappingScrews = 373
    swStandardGBSlottedCheeseHeadScrews = 374
    swStandardGBHexagonLobularSocketHeadCapScrewsPropertyClass4 = 375
    swStandardGBHexagonHeadBoltsGB = 376
    swStandardGBHexagonHeadBoltsFullThreadProductGradeC = 377
    swStandardGBHexagonHeadBoltsFullThreadProductGradesAB = 378
    swStandardGBHexagonHeadBoltsProductGradeC = 379
    swStandardKSDrillSizes = 450
    swStandardKSScrewClearances = 451
    swStandardKSTapDrills = 452
    swStandardKSTaperedPipeTap = 453
    swStandardKSBottomingTappedHole = 454
    swStandardKSTappedHole = 455
    swStandardKSFlatCrossHeadScrew = 456
    swStandardKSRaisedCrossHeadScrew = 457
    swStandardKSSocketHeadCapScrew = 458
    swStandardKSHexHeadBoltA = 459
    swStandardKSHexHeadBoltB = 460
    swStandardKSHexHeadBoltC = 461
    swStandardKSCheeseSlottedHead = 462
    swStandardISDrillSizes = 550
    swStandardISScrewClearances = 551
    swStandardISTapDrills = 552
    swStandardISTaperedPipeTap = 553
    swStandardISBottomingTappedHole = 554
    swStandardISTappedHole = 555
    swStandardISCrossRecessFlatHeadScrew = 556
    swStandardISCrossRecessPanHeadScrew = 557
    swStandardISCrossRecessRaisedHeadScrew = 558
    swStandardISHexagonHeadBoltC = 559
    swStandardISHexagonHeadScrewA = 560
    swStandardISHexagonHeadScrewB = 561
    swStandardISHexagonHeadScrewC = 562
    swStandardISSlottedCheeseHeadScrew = 563
    swStandardISSocketHeadCapScrew = 564
    swStandardASDrillSizes = 650
    swStandardASScrewClearances = 651
    swStandardASTapDrills = 652
    swStandardASTaperedPipeTap = 653
    swStandardASBottomingTappedHole = 654
    swStandardASTappedHole = 655
    swStandardASCrossCountersunkHeadScrew = 657
    swStandardASRaisedCrossCountersunkHeadScrew = 658
    swStandardASPanCrossHeadScrew = 659
    swStandardASPanSlottedHeadScrew = 660
    swStandardASCheeseHeadScrew = 661
    swStandardASMushroomHeadScrew = 662
    swStandardASSocketHeadCapScrew = 663
    swStandardASHexBoltGradesAB = 664
    swStandardASUnifiedHexBolt = 665
    swStandardASHexStructuralBolt = 666
    swStandardASUnifiedHexScrew = 667
    swStandardASHexScrewGradesAB = 668
    swStandardASHexBoltGradeC = 669
    swStandardASHexScrewGradeC = 670
    swStandardDINHexSocketHeadFine912 = 701
    swStandardDINHexSocketHeadThin7984 = 702
    swStandardAnsiInchDowelHole = 703
    swStandardAnsiMetricDowelHole = 704
    swStandardASDowelHole = 705
    swStandardBSIDowelHole = 706
    swStandardDINDowelHole = 707
    swStandardGBDowelHole = 708
    swStandardISDowelHole = 709
    swStandardISODowelHole = 710
    swStandardJISDowelHole = 711
    swStandardKSDowelHole = 712
    swStandardPEMInch300SCNuts = 906
    swStandardPEMInchAluminumSCNuts = 901
    swStandardPEMInchNon_lockingNuts = 905
    swStandardPEMInchSelf_clinchingNuts = 909
    swStandardPEMInchSelf_lockingNuts = 910
    swStandardPEMInchThinSheet = 912
    swStandardPEMInchTRI_DENT = 913
    swStandardPEMInchWeldNuts = 908
    swStandardPEMInchBlindFasteners = 902
    swStandardPEMInchFloating = 903
    swStandardPEMInchMiniature = 904
    swStandardPEMInchPEMHEXFasteners = 914
    swStandardPEMInchPEMSERTFlushFasteners = 907
    swStandardPEMInchSelf_lockingFasteners = 911
    swStandardPEMInchBlindSO = 947
    swStandardPEMInchConcealedStandoffs = 948
    swStandardPEMInchKEYHOLEStandoffs = 949
    swStandardPEMInchSNAP_TOPSBStandoffs = 950
    swStandardPEMInchSNAP_TOPSCStandoffs = 951
    swStandardPEMInchTHStandoffs = 952
    swStandardPEMInchTSStandoffs = 953
    swStandardPEMInchUStandoffs = 954
    swStandardPEMInchConcealedStuds = 929
    swStandardPEMInchFHDogPointStuds = 932
    swStandardPEMInchFlushheadStuds = 931
    swStandardPEMInchHigh_strengthStuds = 934
    swStandardPEMInchHSDogPointStuds = 935
    swStandardPEMInchLow_displacementStuds = 936
    swStandardPEMInchNon_flushheadStuds = 937
    swStandardPEMInchFlushheadPins = 930
    swStandardPEMInchFlushPilotPins = 933
    swStandardPEMMetric300SCNuts = 920
    swStandardPEMMetricAluminumSCNuts = 915
    swStandardPEMMetricNon_lockingNuts = 919
    swStandardPEMMetricSelf_clinchingNuts = 923
    swStandardPEMMetricSelf_lockingNuts = 924
    swStandardPEMMetricThinSheet = 926
    swStandardPEMMetricTRI_DENT = 927
    swStandardPEMMetricWeldNuts = 922
    swStandardPEMMetricBlindFasteners = 916
    swStandardPEMMetricFloating = 917
    swStandardPEMMetricMiniature = 918
    swStandardPEMMetricPEMHEXFasteners = 928
    swStandardPEMMetricPEMSERTFlushFasteners = 921
    swStandardPEMMetricSelf_lockingFasteners = 925
    swStandardPEMMetricBlindSO = 955
    swStandardPEMMetricConcealedStandoffs = 956
    swStandardPEMMetricKEYHOLEStandoffs = 957
    swStandardPEMMetricSNAP_TOPSBStandoffs = 958
    swStandardPEMMetricSNAP_TOPSCStandoffs = 959
    swStandardPEMMetricTHStandoffs = 961
    swStandardPEMMetricTSStandoffs = 960
    swStandardPEMMetricUStandoffs = 962
    swStandardPEMMetricConcealedStuds = 938
    swStandardPEMMetricFHDogPointStuds = 941
    swStandardPEMMetricFlushheadStuds = 940
    swStandardPEMMetricHigh_strengthStuds = 943
    swStandardPEMMetricHSDogPointStuds = 944
    swStandardPEMMetricLow_displacementStuds = 945
    swStandardPEMMetricNon_flushheadStuds = 946
    swStandardPEMMetricFlushheadPins = 939
    swStandardPEMMetricFlushPilotPins = 942

class swWzdHoleStandards_e(IntEnum):
    """swWzdHoleStandards_e (19 constants, from SwConst)."""
    swStandardAnsiInch = 0
    swStandardAnsiMetric = 1
    swStandardBSI = 2
    swStandardDME = 3
    swStandardDIN = 4
    swStandardHascoMetric = 5
    swStandardHelicoilInch = 6
    swStandardHelicoilMetric = 7
    swStandardISO = 8
    swStandardJIS = 9
    swStandardPCS = 10
    swStandardProgressive = 11
    swStandardSuperior = 12
    swStandardGB = 13
    swStandardKS = 14
    swStandardIS = 15
    swStandardAS = 16
    swStandardPEMInch = 17
    swStandardPEMMetric = 18

class swWzdHoleThreadEndCondition_e(IntEnum):
    """swWzdHoleThreadEndCondition_e (3 constants, from SwConst)."""
    swEndThreadTypeBLIND = 0
    swEndThreadTypeTHROUGH_ALL = 1
    swEndThreadTypeTHROUGH_NEXT = 2

class swWzdHoleTypes_e(IntEnum):
    """swWzdHoleTypes_e (81 constants, from SwConst)."""
    swSimple = 0
    swTapered = 1
    swCounterBored = 2
    swCounterSunk = 3
    swCounterDrilled = 4
    swSimpleDrilled = 5
    swTaperedDrilled = 6
    swCounterBoredDrilled = 7
    swCounterSunkDrilled = 8
    swCounterDrilledDrilled = 9
    swCounterBoreBlind = 10
    swCounterBoreBlindCounterSinkMiddle = 11
    swCounterBoreBlindCounterSinkTop = 12
    swCounterBoreBlindCounterSinkTopmiddle = 13
    swCounterBoreThru = 14
    swCounterBoreThruCounterSinkBottom = 15
    swCounterBoreThruCounterSinkMiddle = 16
    swCounterBoreThruCounterSinkMiddleBottom = 17
    swCounterBoreThruCounterSinkTop = 18
    swCounterBoreThruCounterSinkTopBottom = 19
    swCounterBoreThruCounterSinkTopMiddle = 20
    swCounterBoreThruCounterSinkTopMiddleBottom = 21
    swHoleBlind = 22
    swHoleBlindCounterSinkTop = 23
    swCounterSinkBlind = 24
    swHoleThru = 25
    swHoleThruCounterSinkBottom = 26
    swHoleThruCounterSinkTop = 27
    swHoleThruCounterSinkTopBottom = 28
    swCounterSinkThru = 29
    swCounterSinkThruCounterSinkBottom = 30
    swTapBlind = 31
    swTapBlindCounterSinkTop = 32
    swTapThru = 33
    swTapThruCounterSinkBottom = 34
    swTapThruCounterSinkTop = 35
    swTapThruCounterSinkTopBottom = 36
    swPipeTapBlind = 37
    swPipeTapBlindCounterSinkTop = 38
    swPipeTapThru = 39
    swPipeTapThruCounterSinkBottom = 40
    swPipeTapThruCounterSinkTop = 41
    swPipeTapThruCounterSinkTopBottom = 42
    swCounterSinkBlindWithoutHeadClearance = 43
    swCounterSinkThruWithoutHeadClearance = 44
    swCounterSinkThruCounterSinkBottomWithoutHeadClearance = 45
    swTapBlindCosmeticThread = 46
    swTapBlindCosmeticThreadCounterSinkTop = 47
    swTapThruCosmeticThread = 48
    swTapThruCosmeticThreadCounterSinkTop = 49
    swTapThruCosmeticThreadCounterSinkBottom = 50
    swTapThruCosmeticThreadCounterSinkTopBottom = 51
    swTapThruThreadThru = 52
    swTapThruThreadThruCounterSinkTop = 53
    swTapThruThreadThruCounterSinkBottom = 54
    swTapThruThreadThruCountersinkTopBottom = 55
    swTapBlindRemoveThread = 56
    swCounterBoreSlotBlind = 57
    swCounterBoreSlotBlindCounterSinkMiddle = 58
    swCounterBoreSlotBlindCounterSinkTop = 59
    swCounterBoreSlotBlindCounterSinkTopMiddle = 60
    swCounterBoreSlotThru = 61
    swCounterBoreSlotThruCounterSinkBottom = 62
    swCounterBoreSlotThruCounterSinkMiddle = 63
    swCounterBoreSlotThruCounterSinkMiddleBottom = 64
    swCounterBoreSlotThruCounterSinkTop = 65
    swCounterBoreSlotThruCounterSinkTopBottom = 66
    swCounterBoreSlotThruCounterSinkTopMiddle = 67
    swCounterBoreSlotThruCounterSinkTopMiddleBottom = 68
    swSlotBlind = 69
    swSlotBlindCounterSinkTop = 70
    swCounterSinkSlotBlind = 71
    swSlotThru = 72
    swSlotThruCounterSinkBottom = 73
    swSlotThruCounterSinkTop = 74
    swSlotThruCounterSinkTopBottom = 75
    swCounterSinkSlotThru = 76
    swCounterSinkSlotThruCounterSinkBottom = 77
    swCounterSinkSlotBlindWithoutHeadClearance = 78
    swCounterSinkSlotThruWithoutHeadClearance = 79
    swCounterSinkSlotThruCounterSinkBottomWithoutHeadClearance = 90

class swZeroQuantityDisplay_e(IntEnum):
    """swZeroQuantityDisplay_e (3 constants, from SwConst)."""
    swZeroQuantityDashed = 1
    swZeroQuantityZero = 2
    swZeroQuantityBlank = 3

class swZonalSectionViewZones_e(IntEnum):
    """swZonalSectionViewZones_e (8 constants, from SwConst)."""
    swZonalSectionViewZones_swZonalSectionViewZone_1 = 1
    swZonalSectionViewZones_swZonalSectionViewZone_2 = 2
    swZonalSectionViewZones_swZonalSectionViewZone_3 = 4
    swZonalSectionViewZones_swZonalSectionViewZone_4 = 8
    swZonalSectionViewZones_swZonalSectionViewZone_5 = 16
    swZonalSectionViewZones_swZonalSectionViewZone_6 = 32
    swZonalSectionViewZones_swZonalSectionViewZone_7 = 64
    swZonalSectionViewZones_swZonalSectionViewZone_8 = 128

class swZoneMargin_e(IntEnum):
    """swZoneMargin_e (4 constants, from SwConst)."""
    swZoneTopMargin = 0
    swZoneBottomMargin = 1
    swZoneRightMargin = 2
    swZoneLeftMargin = 3

class swZoneSizeDistribution_e(IntEnum):
    """swZoneSizeDistribution_e (2 constants, from SwConst)."""
    swZoneSizeDistribution_50mmFromCenter = 0
    swZoneSizeDistribution_EvenlySized = 1

class swZoomLevelOnOpenType_e(IntEnum):
    """swZoomLevelOnOpenType_e (3 constants, from SwConst)."""
    swZoomLevelOnOpenType_LastSave = 0
    swZoomLevelOnOpenType_ToFit = 1
    swZoomLevelOnOpenType_ToSheet = 2

class swcActivateBodyResult_e(IntEnum):
    """swcActivateBodyResult_e (2 constants, from SldCostingAPI)."""
    swcActivateBodyResult_Success = 0
    swcActivateBodyResult_GenericFailure = 1

class swcBodyStatus_e(IntEnum):
    """swcBodyStatus_e (4 constants, from SldCostingAPI)."""
    swcBodyStatus_NotAnalysed = 0
    swcBodyStatus_Analysed = 1
    swcBodyStatus_Excluded = 2
    swcBodyStatus_AssignedCustomCost = 3

class swcBodyType_e(IntEnum):
    """swcBodyType_e (6 constants, from SldCostingAPI)."""
    swcBodyType_SheetMetal = 0
    swcBodyType_Machined = 1
    swcBodyType_Custom = 2
    swcBodyType_Structural = 3
    swcBodyType_Undefined = 4
    swcBodyType_GeneralBody = 5

class swcCostFeatureType_e(IntEnum):
    """swcCostFeatureType_e (71 constants, from SldCostingAPI)."""
    swcMachinedBodiesFolderType = 0
    swcSheetMetalBodiesFolderType = 1
    swcSetupBodyFolderType = 2
    swcStructuralBodiesFolderType = 3
    swcCustomBodiesFolderType = 4
    swcWeldingFolderType = 5
    swcCustomOperationsFolderType = 6
    swcNoCostAssignedFolderType = 7
    swcMachinedBodyItemType = 8
    swcSheetMetalBodyItemType = 9
    swcCustomBodyItemType = 10
    swcMultiBodySetupCostItem = 11
    swcSheetMetalCutPathItemType = 12
    swcSheetMetalBendsFolderType = 13
    swcSheetMetalCustomOperationsFolderType = 14
    swcSheetMetalCutPathesFolderType = 15
    swcSheetMetalLibraryFeaturesFolderType = 16
    swcSheetMetalLibraryNoCostAssignedFolderType = 17
    swcSheetMetalSetupCostFolderType = 18
    swcSheetMetalItemFeatureType = 19
    swcSheetMetalItemSetupCost = 20
    swcSheetMetalItemCustomOperation = 21
    swcMachiningChamferFeatureItemType = 22
    swcMachiningChamferOperationItemType = 23
    swcMachiningFaceAdditionalOperationItem = 24
    swcMachiningFaceFeatureItemType = 25
    swcMachiningFaceOperationItemType = 26
    swcMachiningMillFeatureItemType = 27
    swcMachiningLocalSetupCostItemType = 28
    swcMachiningMillAdditionalOperationItemType = 29
    swcMachiningMillOperationItemType = 30
    swcMachiningPatternedHoleFeatureItemType = 31
    swcMachiningPatternedHoleSubFeatureItemType = 32
    swcMachiningSetupCostFeatureItem = 33
    swcMachiningSetupCostItemType = 34
    swcMachiningSetupCostOperationItemType = 35
    swcMachiningItemCustomOperation = 36
    swcMachiningPlateCutpathItem = 37
    swcMachiningHoleFeatureItem = 38
    swcMachiningOperationHoleDrill = 39
    swcMachiningOperationHoleCDrill = 40
    swcMachiningOperationHoleTapping = 41
    swcMachiningPlateCutpathFolderType = 42
    swcMachiningCustomOperationFolderType = 43
    swcMachiningHoleOperationsFolderType = 44
    swcMachiningLibraryFeaturesFolderType = 45
    swcMachiningMillOperationsFolderType = 46
    swcMachiningTurnOperationsFolderType = 47
    swcMachiningNCAFolderType = 48
    swcMachiningSetupCostFolderType = 49
    swcMachiningVolumeFeatureItemType = 50
    swcMachiningVolumeOperationItemType = 51
    swcMachiningVolumeAdditionalOperationItem = 52
    swcMachiningLibraryFeatureType = 53
    swcMachiningEndProfileFeatureItem = 54
    swcMachiningGrooveFeatureItem = 55
    swcNoCostAssignedBody = 56
    swcMachiningFilletFeatureItem = 57
    swcMachineSetupCostSubFolderType = 58
    swcMachineOperationSetupCostSubFolderType = 59
    swcMachineCustomSetupCostSubFolderType = 60
    swcMachineSetupCostItemType = 61
    swcMachiningItemBendFeatureType = 62
    swcAdditiveFeatureType = 63
    swcWeldFeatureItemType = 64
    swcWeldOperationItemType = 65
    swcEndCutFeaturesFolderType = 66
    swcEndCutFeatureItemType = 67
    swcStructuralBodyItemType = 68
    swcGussetsFolderType = 69
    swcEndcapFolderType = 70

class swcCostingType_e(IntEnum):
    """swcCostingType_e (4 constants, from SldCostingAPI)."""
    swcCostingType_Common = 0
    swcCostingType_SheetMetal = 1
    swcCostingType_Machining = 2
    swcCostingType_Structural = 3

class swcCustomStockCostInfoType_e(IntEnum):
    """swcCustomStockCostInfoType_e (4 constants, from SldCostingAPI)."""
    swcCustomStockCostType_Unknown = 0
    swcCustomStockCostType_SavedCostingData = 1
    swcCustomStockCostType_Volume = 2
    swcCustomStockCostType_CustomCost = 3

class swcCustomStockImportType_e(IntEnum):
    """swcCustomStockImportType_e (3 constants, from SldCostingAPI)."""
    swcCustomStockImportType_Unknown = 0
    swcCustomStockImportType_Configuration = 1
    swcCustomStockImportType_ReferencePart = 2

class swcDefaultMachiningTool_e(IntEnum):
    """swcDefaultMachiningTool_e (7 constants, from SldCostingAPI)."""
    swcDefaultMachiningTool_FlatEndMill = 0
    swcDefaultMachiningTool_BallEndMill = 1
    swcDefaultMachiningTool_FaceMill = 2
    swcDefaultMachiningTool_HSSDrill = 3
    swcDefaultMachiningTool_CarbideDrill = 4
    swcDefaultMachiningTool_ODTurning = 5
    swcDefaultMachiningTool_IDTurning = 6

class swcFinishingOperationType_e(IntEnum):
    """swcFinishingOperationType_e (3 constants, from SldCostingAPI)."""
    swcFinishingOperationType_Roughing = 0
    swcFinishingOperationType_Semifinishing = 1
    swcFinishingOperationType_Finishing = 2

class swcLengthUnit_e(IntEnum):
    """swcLengthUnit_e (2 constants, from SldCostingAPI)."""
    swcLengthUnit_mm = 0
    swcLengthUnit_inch = 1

class swcMarkUpType_e(IntEnum):
    """swcMarkUpType_e (3 constants, from SldCostingAPI)."""
    swcMarkUpType_TotalCost = 0
    swcMarkUpType_MaterialCost = 1
    swcMarkUpType_None = 2

class swcMassUnit_e(IntEnum):
    """swcMassUnit_e (2 constants, from SldCostingAPI)."""
    swcMassUnit_kg = 0
    swcMassUnit_lb = 1

class swcMethodType_e(IntEnum):
    """swcMethodType_e (7 constants, from SldCostingAPI)."""
    swcMethodType_Sheetmetal = 0
    swcMethodType_Machining = 1
    swcMethodType_Structural = 2
    swcMethodType_Plastic = 3
    swcMethodType_Casting = 4
    swcMethodType_3dPrinting = 5
    swcMethodType_MachinedPlate = 6

class swcMoldCalculationMethod_e(IntEnum):
    """swcMoldCalculationMethod_e (2 constants, from SldCostingAPI)."""
    swcMoldCalculationMethod_WallThickness = 0
    swcMoldCalculationMethod_CycleTime = 1

class swcPlane_e(IntEnum):
    """swcPlane_e (3 constants, from SldCostingAPI)."""
    swcPlane_XY = 0
    swcPlane_YZ = 1
    swcPlane_XZ = 2

class swcRemovedMaterialProcessingType_e(IntEnum):
    """swcRemovedMaterialProcessingType_e (2 constants, from SldCostingAPI)."""
    swcProcessingType_Standard = 0
    swcProcessingType_Volume = 1

class swcRunnerSystem_e(IntEnum):
    """swcRunnerSystem_e (2 constants, from SldCostingAPI)."""
    swcRunnerSystem_HotRunner = 0
    swcRunnerSystem_ColdRunner = 1

class swcSheetMetalBlankSizeType_e(IntEnum):
    """swcSheetMetalBlankSizeType_e (4 constants, from SldCostingAPI)."""
    swcSheetMetalBlankSizeType_BoundingBox = 0
    swcSheetMetalBlankSizeType_FlatPattern = 1
    swcSheetMetalBlankSizeType_CustomSize = 2
    swcSheetMetalBlankSizeType_CustomArea = 3

class swcSlotFeatureRecognitionType_e(IntEnum):
    """swcSlotFeatureRecognitionType_e (2 constants, from SldCostingAPI)."""
    swcSlotFeatureRecognitionType_Slot = 0
    swcSlotFeatureRecognitionType_Volume = 1

class swcStockType_e(IntEnum):
    """swcStockType_e (5 constants, from SldCostingAPI)."""
    swcStockType_Unknown = 0
    swcStockType_Block = 1
    swcStockType_Plate = 2
    swcStockType_Cylinder = 3
    swcStockType_Custom = 4

class swcStructuralStockCostType_e(IntEnum):
    """swcStructuralStockCostType_e (3 constants, from SldCostingAPI)."""
    swcStructuralStockCostType_Unknown = 0
    swcStructuralStockCostType_PerLength = 1
    swcStructuralStockCostType_PerUnitLength = 2

class swcUnitSystem_e(IntEnum):
    """swcUnitSystem_e (2 constants, from SldCostingAPI)."""
    swcUnitSystem_mm_kg = 0
    swcUnitSystem_inch_lb = 1

class swcUpdateCostError_e(IntEnum):
    """swcUpdateCostError_e (3 constants, from SldCostingAPI)."""
    swcUpdateCostError_None = 0
    swcUpdateCostError_TemplateUnavailable = 1
    swcUpdateCostError_MaterialUnavailable = 2

class swcVolumeFeatureCalculationType_e(IntEnum):
    """swcVolumeFeatureCalculationType_e (2 constants, from SldCostingAPI)."""
    swcVolumeFeatureCalculationType_MachiningOperation = 0
    swcVolumeFeatureCalculationType_CostPerVolume = 1

class swsAccelerationComponent_e(IntEnum):
    """swsAccelerationComponent_e (8 constants, from CosmosWorksLib)."""
    swsAccelerationComponentAX = 0
    swsAccelerationComponentAY = 1
    swsAccelerationComponentAZ = 2
    swsAccelerationComponentARES = 3
    swsAccelerationComponentBX = 4
    swsAccelerationComponentBY = 5
    swsAccelerationComponentBZ = 6
    swsAccelerationComponentANG = 7

class swsAccelerationUnit_e(IntEnum):
    """swsAccelerationUnit_e (4 constants, from CosmosWorksLib)."""
    swsAccelerationUnit_MetersPerSquareSec = 0
    swsAccelerationUnit_InchesPerSquareSec = 1
    swsAccelerationUnit_CentimetersPerSquareSec = 2
    swsAccelerationUnit_g = 3

class swsAddDefaultDropTestStudyPlotResultError_e(IntEnum):
    """swsAddDefaultDropTestStudyPlotResultError_e (6 constants, from CosmosWorksLib)."""
    swsDropTestResultNoError = 0
    swsDropTestResultRangeError = 1
    swsDropTestResultNodalStressRangeError = 2
    swsDropTestResultElementalStressRangeError = 3
    swsDropTestResultDisplacementRangeError = 4
    swsDropTestResultElementalStrainRangeError = 5

class swsAddDefaultFatigueStudyPlotResultError_e(IntEnum):
    """swsAddDefaultFatigueStudyPlotResultError_e (2 constants, from CosmosWorksLib)."""
    swsFatigueResultNoError = 0
    swsFatigueResultRangeError = 1

class swsAddDefaultFrequencyOrBucklingStudyPlotResultError_e(IntEnum):
    """swsAddDefaultFrequencyOrBucklingStudyPlotResultError_e (3 constants, from CosmosWorksLib)."""
    swsFrequencyResultNoError = 0
    swsFrequencyMaxModeShapeValueRangeError = 1
    swsFrequencyResultDisplacementRangeError = 2

class swsAddDefaultNonLinearStudyPlotResultError_e(IntEnum):
    """swsAddDefaultNonLinearStudyPlotResultError_e (7 constants, from CosmosWorksLib)."""
    swsNonLinearResultNoError = 0
    swsNonLinearResultRangeError = 1
    swsNonLinearResultNodalStressComponentRangeError = 2
    swsNonLinearResultElementalStressComponentRangeError = 3
    swsNonLinearResultDisplacementComponentRangeError = 4
    swsNonLinearResultNodalStrainComponentRangeError = 5
    swsNonLinearResultElementalStrainComponentRangeError = 6

class swsAddDefaultOptimizationDesignStudyPlotResultError_e(IntEnum):
    """swsAddDefaultOptimizationDesignStudyPlotResultError_e (2 constants, from CosmosWorksLib)."""
    swsOptimizationDesignResultNoError = 0
    swsOptimizationDesignResultDesignValueRangeError = 1

class swsAddDefaultStaticStudyPlotResultError_e(IntEnum):
    """swsAddDefaultStaticStudyPlotResultError_e (7 constants, from CosmosWorksLib)."""
    swsStaticResultNoErrror = 0
    swsStaticResultTypeRangeError = 1
    swsStaticResultElementalStressComponentRangeError = 2
    swsStaticResultDisplacementComponentRangeError = 3
    swsStaticResultNodalStrainRangeError = 4
    swsStaticResultElementalStrainRangeError = 5
    swsStaticResultNodalStressComponentRangeError = 6

class swsAddDefaultThermalStudyPlotResultError_e(IntEnum):
    """swsAddDefaultThermalStudyPlotResultError_e (2 constants, from CosmosWorksLib)."""
    swsThermalResultNoError = 0
    swsThermalResultRangeError = 1

class swsAnalysisStudyType_e(IntEnum):
    """swsAnalysisStudyType_e (14 constants, from CosmosWorksLib)."""
    swsAnalysisStudyTypeStatic = 0
    swsAnalysisStudyTypeFrequency = 1
    swsAnalysisStudyTypeBuckling = 2
    swsAnalysisStudyTypeThermal = 3
    swsAnalysisStudyTypeOptimization = 4
    swsAnalysisStudyTypeNonlinear = 5
    swsAnalysisStudyTypeDropTest = 6
    swsAnalysisStudyTypeFatigue = 7
    swsAnalysisStudyTypeDynamic = 8
    swsAnalysisStudyTypePressureVessel = 9
    swsAnalysisStudyTypeReserved1 = 10
    swsAnalysisStudyTypeReserved2 = 11
    swsAnalysisStudyTypeReserved3 = 12
    swsAnalysisStudyTypeTopology_Static = 13

class swsAngularAccelerationUnit_e(IntEnum):
    """swsAngularAccelerationUnit_e (3 constants, from CosmosWorksLib)."""
    swsAngularAccelerationUnit_RadiansPerSquareSec = 0
    swsAngularAccelerationUnit_HertzPerSec = 1
    swsAngularAccelerationUnit_RPMSquare = 2

class swsAngularVelocityUnit_e(IntEnum):
    """swsAngularVelocityUnit_e (3 constants, from CosmosWorksLib)."""
    swsAngularVelocityUnit_RadiansPerSec = 0
    swsAngularVelocityUnit_Hertz = 1
    swsAngularVelocityUnit_RPM = 2

class swsBaseExcitationEndEditError_e(IntEnum):
    """swsBaseExcitationEndEditError_e (12 constants, from CosmosWorksLib)."""
    swsBaseExcitationError_NoError = 0
    swsBaseExcitationError_NotAvailableForThisStudy = 1
    swsBaseExcitationError_InvalidExcitationType = 2
    swsBaseExcitationError_ExcitationTypeNotAvailable = 3
    swsBaseExcitationError_NoProperFixtures = 4
    swsBaseExcitationError_InvalidFixtureNameOrEntity = 5
    swsBaseExcitationError_ImproperUnits = 6
    swsBaseExcitationError_SelectAtleastOneDirection = 7
    swsBaseExcitationError_SelectOnlyOneDirection = 8
    swsBaseExcitationError_SelectOnlyThirdDirection = 9
    swsBaseExcitationError_SelectAtleastOneDirectionOfThatInRestraint = 10
    swsBaseExcitationError_InvalidValue = 11

class swsBaseExcitationType_e(IntEnum):
    """swsBaseExcitationType_e (3 constants, from CosmosWorksLib)."""
    swsBaseExcitationType_Displacement = 0
    swsBaseExcitationType_Velocity = 1
    swsBaseExcitationType_Acceleration = 2

class swsBeamBodyConnectionType_e(IntEnum):
    """swsBeamBodyConnectionType_e (4 constants, from CosmosWorksLib)."""
    swsBeamBodyConnectionRigid = 0
    swsBeamBodyConnectionPin = 1
    swsBeamBodyConnectionSlide = 2
    swsBeamBodyConnectionManual = 3

class swsBeamBodyManualConnectionType_e(IntEnum):
    """swsBeamBodyManualConnectionType_e (6 constants, from CosmosWorksLib)."""
    swsBeamBodyManualConnectionHinge1stDirection = 0
    swsBeamBodyManualConnectionHinge2ndDirection = 1
    swsBeamBodyManualConnectionHingeAlongBeam = 2
    swsBeamBodyManualConnectionSlide1stDireciton = 3
    swsBeamBodyManualConnectionSlide2ndDirection = 4
    swsBeamBodyManualConnectionSlideAlongBeam = 5

class swsBeamForceType_e(IntEnum):
    """swsBeamForceType_e (6 constants, from CosmosWorksLib)."""
    swsBeamForceAxial = 0
    swsBeamForceShearDirection1 = 1
    swsBeamForceShearDirection2 = 2
    swsBeamForceMomentDirection1 = 3
    swsBeamForceMomentDirection2 = 4
    swsBeamForceTorque = 5

class swsBeamNonUniformLoadDef_e(IntEnum):
    """swsBeamNonUniformLoadDef_e (3 constants, from CosmosWorksLib)."""
    swsTotalLoad = 0
    swsCentralLoad = 1
    swsTableDrivenLoad = 2

class swsBeamNonUniformLoadType_e(IntEnum):
    """swsBeamNonUniformLoadType_e (3 constants, from CosmosWorksLib)."""
    swsTriangularLoad = 0
    swsParabolicLoad = 1
    swsEllipticalLoad = 2

class swsBeamStressComponent_e(IntEnum):
    """swsBeamStressComponent_e (4 constants, from CosmosWorksLib)."""
    swsBeamStressComponentAxial = 0
    swsBeamStressComponentBendingLocalDir1 = 1
    swsBeamStressComponentBendingLocalDir2 = 2
    swsBeamStressComponentWorstCase = 3

class swsBeamStressType_e(IntEnum):
    """swsBeamStressType_e (5 constants, from CosmosWorksLib)."""
    swsBeamStressAxial = 0
    swsBeamStressBendingDirection1 = 1
    swsBeamStressBendingDirection2 = 2
    swsBeamStressTorsional = 3
    swsBeamStressWorstCase = 4

class swsBeamType_e(IntEnum):
    """swsBeamType_e (2 constants, from CosmosWorksLib)."""
    swsBeamTypeBeam = 0
    swsBeamTypeTruss = 1

class swsBearingConnectionType_e(IntEnum):
    """swsBearingConnectionType_e (3 constants, from CosmosWorksLib)."""
    swsDistributedConnType = 0
    swsRigidConnType = 1
    swsSpringConnType = 2

class swsBearingConnectorErrors_e(IntEnum):
    """swsBearingConnectorErrors_e (18 constants, from CosmosWorksLib)."""
    swsBearingConnectorErrCode_Successful = 0
    swsBearingConnectorErrCode_NoActiveDoc = 1
    swsBearingConnectorErrCode_NoActiveStudy = 2
    swsBearingConnectorErrCode_SetOperationNotSupported = 3
    swsBearingConnectorErrCode_InvalidSelectionForHousing = 4
    swsBearingConnectorErrCode_InvalidSelectionForShaft = 5
    swsBearingConnectorErrCode_SourceAndTargetSelectionsSwitched = 6
    swsBearingConnectorErrCode_InvalidUnitType = 7
    swsBearingConnectorErrCode_OutOfRangeLateralStiffness = 8
    swsBearingConnectorErrCode_OutOfRangeAxialStiffness = 9
    swsBearingConnectorErrCode_OutOfRangeTiltStiffness = 10
    swsBearingConnectorErrCode_OutOfRangeShaftStabilizeStiffness = 11
    swsBearingConnectorErrCode_InadequateEntitiesSelection = 12
    swsBearingConnectorErrCode_MoreThanOneFaceSelectedForShaft = 13
    swsBearingConnectorErrCode_MoreThanOneFaceOrEdgeSelectedForHousing = 14
    swsBearingConnectorErrCode_FacesOrEdgesSelectedFromSingleComponent = 15
    swsBearingConnectorErrCode_LenByDiamRatioGreaterThan2ForShaft = 16
    swsBearingConnectorErrCode_InvalidConnectionType = 17

class swsBearingLoadDistributionType_e(IntEnum):
    """swsBearingLoadDistributionType_e (2 constants, from CosmosWorksLib)."""
    swsBearingLoadDistributionTypeSinusoidal = 0
    swsBearingLoadDistributionTypeParabolic = 1

class swsBearingLoadEndEditError_e(IntEnum):
    """swsBearingLoadEndEditError_e (18 constants, from CosmosWorksLib)."""
    swsBearingLoadEndEditErrorSuccessful = 0
    swsBearingLoadEndEditErrorCoordinateSystemCylindricalFaces = 1
    swsBearingLoadEndEditErrorIncorrectOrNullEntity = 2
    swsBearingLoadEndEditErrorEntityExists = 3
    swsBearingLoadEndEditErrorSelectFace = 4
    swsBearingLoadEndEditErrorNoEntityAtIndex = 5
    swsBearingLoadEndEditErrorSpecifyValue = 6
    swsBearingLoadEndEditErrorSelectFaceWithCylindricalSurface = 7
    swsBearingLoadEndEditErrorHasMassElement = 8
    swsBearingLoadEndEditErrorHasBeamBody = 9
    swsBearingLoadEndEditErrorIndexExceedsNumberOfEntities = 10
    swsBearingLoadEndEditErrorNoEntity = 11
    swsBearingLoadEndEditErrorSelectOneForceDirection = 12
    swsBearingLoadEndEditErrorSelectForceDirection = 13
    swsBearingLoadEndEditErrorSetXDirection = 14
    swsBearingLoadEndEditErrorSetYDirection = 15
    swsBearingLoadEndEditErrorNullEntity = 16
    swsBearingLoadEndEditErrorBodyExcludedFromAnalysis = 17

class swsBearingStiffnessShaftStabilizeType_e(IntEnum):
    """swsBearingStiffnessShaftStabilizeType_e (2 constants, from CosmosWorksLib)."""
    swsBearingStiffnessShaftStabilizeAuto = 0
    swsBearingStiffnessShaftStabilizeUserDef = 1

class swsBearingStiffnessType_e(IntEnum):
    """swsBearingStiffnessType_e (2 constants, from CosmosWorksLib)."""
    swsBearingStiffnessRigid = 0
    swsBearingStiffnessFlexible = 1

class swsBoltConnectorEndEditError_e(IntEnum):
    """swsBoltConnectorEndEditError_e (45 constants, from CosmosWorksLib)."""
    swsBoltConnectorEndEditErrorSuccessful = 0
    swsBoltConnectorEndEditErrorSelectFace = 1
    swsBoltConnectorEndEditErrorSelectConicalSurface = 2
    swsBoltConnectorEndEditErrorIncorrectHeadDiameter = 3
    swsBoltConnectorEndEditErrorSelectEdge = 4
    swsBoltConnectorEndEditErrorSelectCircularEdge = 5
    swsBoltConnectorEndEditErrorSelectCylindricalThreadFace = 6
    swsBoltConnectorEndEditErrorIncorrectShankDiameter = 7
    swsBoltConnectorEndEditErrorSelectMass = 8
    swsBoltConnectorEndEditErrorSelectConcentricEntities = 9
    swsBoltConnectorEndEditErrorSpecifyYoungModulus = 10
    swsBoltConnectorEndEditErrorSpecifyTemperatureCoefficient = 11
    swsBoltConnectorEndEditErrorSpecifyPoissonsRatio = 12
    swsBoltConnectorEndEditErrorDefineMaterial = 13
    swsBoltConnectorEndEditErrorSpecifyPreloadValue = 14
    swsBoltConnectorEndEditErrorSpecifyFrictionValue = 15
    swsBoltConnectorEndEditErrorSelectPlanarFace = 16
    swsBoltConnectorEndEditErrorSelectBoltHeadAndNut = 17
    swsBoltConnectorEndEditErrorSelectFaceForHeadNutFaceForThread = 18
    swsBoltConnectorEndEditErrorSelectConicalFaceAndBoltNut = 19
    swsBoltConnectorEndEditErrorSelectConicalFaceAndFaceForThread = 20
    swsBoltConnectorEndEditErrorSelectReferencePlane = 21
    swsBoltConnectorEndEditErrorSelectFacesFromMultilayerBolt = 22
    swsBoltConnectorEndEditErrorSelectCoaxialCylindricalSurfaces = 23
    swsBoltConnectorEndEditErrorSelectConcentricCylindricalFaces = 24
    swsBoltConnectorEndEditErrorBoltDiameterBiggerShankContactFaceDiameter = 25
    swsBoltConnectorEndEditErrorSelectBoltNut = 26
    swsBoltConnectorEndEditErrorEntityAlreadyExits = 27
    swsBoltConnectorEndEditErrorNoEntity = 28
    swsBoltConnectorEndEditErrorIncorrectNutDiameter = 29
    swsBoltConnectorEndEditErrorDocumentIsPart = 30
    swsBoltConnectorEndEditErrorSelectNutOrHead = 31
    swsBoltConnectorEndEditErrorSelectEdgesOnShells = 32
    swsBoltConnectorEndEditErrorNoObjectAtIndex = 33
    swsBoltConnectorEndEditErrorEntitySelectionBoxesEmpty = 34
    swsBoltConnectorEndEditErrorSelectOneEntity = 35
    swsBoltConnectorEndEditErrorTooManyEntities = 36
    swsBoltConnectorEndEditErrorNoShearEffectSelected = 37
    swsBoltConnectorEndEditErrorNoMultiBoltSelected = 38
    swsBoltConnectorEndEditErrorBodyHasMassElement = 39
    swsBoltConnectorEndEditErrorBodyExcludedFromAnalysis = 40
    swsBoltConnectorEndEditErrorNullEntity = 41
    swsBoltConnectorEndEditErrorBodyHasBeamElement = 42
    swsBoltConnectorEndEditErrorInvalidForAnalysis = 43
    swsBoltConnectorEndEditErrorInvalidConnectionType = 44

class swsBoltConnectorError_e(IntEnum):
    """swsBoltConnectorError_e (22 constants, from CosmosWorksLib)."""
    swsBoltConnectorErrorSuccessful = 0
    swsBoltConnectorErrorInvalidMesh = 1
    swsBoltConnectorErrorNonLinearStudyAndPartDocument = 2
    swsBoltConnectorErrorInvalidStudy = 3
    swsBoltConnectorErrorSelectEntity = 4
    swsBoltConnectorErrorSelectFaceWithConicalSurface = 5
    swsBoltConnectorErrorSelectEdgeWithCircularLine = 6
    swsBoltConnectorErrorSelectFaceWithCylindricalSurface = 7
    swsBoltConnectorErrorSelectCylindricalThreadFace = 8
    swsBoltConnectorErrorSelectConcentricEntities = 9
    swsBoltConnectorErrorSelectDatumPlane = 10
    swsBoltConnectorErrorSelectEdge = 11
    swsBoltConnectorErrorSelectFace = 12
    swsBoltConnectorErrorSameEntityHeadAndNut = 13
    swsBoltConnectorErrorSelectAssemblyDocument = 14
    swsBoltConnectorErrorNoObjectForNutOrHead = 15
    swsBoltConnectorErrorSelectNutOrHead = 16
    swsBoltConnectorErrorArrayEmpty = 17
    swsBoltConnectorErrorSelectCircularEdgeOnShells = 18
    swsBoltConnectorErrorBoltDiameterTooLarge = 19
    swsBoltConnectorErrorBodyExcludedFromAnalysis = 20
    swsBoltConnectorErrorEdgeFromSameFace = 21

class swsBoltMaterialSource_e(IntEnum):
    """swsBoltMaterialSource_e (3 constants, from CosmosWorksLib)."""
    swsBoltMaterialSourceSolidWorks = 0
    swsBoltMaterialSourceCustomDefined = 1
    swsBoltMaterialSourceLibraryFiles = 2

class swsBoltMaterialType_e(IntEnum):
    """swsBoltMaterialType_e (2 constants, from CosmosWorksLib)."""
    swsBoltMaterialTypeCustom = 0
    swsBoltMaterialTypeLibrary = 1

class swsBoltType_e(IntEnum):
    """swsBoltType_e (5 constants, from CosmosWorksLib)."""
    swsBoltTypeStandardOrCounterboreNut = 0
    swBoltTypeCountersinkWithNut = 1
    swsBoltTypeStandardOrCounterboreScrew = 2
    swsBoltTypeCountersinkScrew = 3
    swsBoltTypeFoundationBolt = 4

class swsCRSectionType_e(IntEnum):
    """swsCRSectionType_e (4 constants, from CosmosWorksLib)."""
    swsSolidCircular = 0
    swsHollowCircular = 1
    swsSolidRectangular = 2
    swsHollowRectangular = 3

class swsCableEndEditErrors_e(IntEnum):
    """swsCableEndEditErrors_e (22 constants, from CosmosWorksLib)."""
    swsCableErrCode_Successful = 0
    swsCableErrCode_NoActiveDoc = 1
    swsCableErrCode_NoActiveStudy = 2
    swsCableErrCode_SetOperationNotSupported = 3
    swsCableErrCode_InvalidSelection = 4
    swsCableErrCode_InvalidNonCoAxialSelection = 5
    swsCableErrCode_InvalidCoAxialSelection = 6
    swsCableErrCode_InvalidNonConcentricSelection = 7
    swsCableErrCode_OffsetOptionNotAvailable = 9
    swsCableErrCode_ZeroDiameterValue = 14
    swsCableErrCode_InvalidUnitType = 15
    swsCableErrCode_InvalidMaterialSourceType = 16
    swsCableErrCode_SetMaterialPropertyNA = 17
    swsCableErrCode_SetLibraryMaterialNA = 18
    swsCableErrCode_InvalidLibraryMaterialDetails = 19
    swsCableErrCode_OutOfRangeYoungsModulus = 20
    swsCableErrCode_OutOfRangeShearModulus = 21
    swsCableErrCode_OutOfRangeThermalCoefficient = 22
    swsCableErrCode_OutOfRangeDensity = 23
    swsCableErrCode_InadequateEntitiesSelection = 24
    swsCableErrCode_OutOfRangeAxialStrengthValue = 25
    swsCableErrCode_OutOfRangePreLoadForceValue = 26

class swsCentrifugalForceEndEditError_e(IntEnum):
    """swsCentrifugalForceEndEditError_e (2 constants, from CosmosWorksLib)."""
    swsCentrifugalForceEndEditErrorSuccessful = 0
    wsCentrifugalForceEndEditErrorSpecifyAxisEdgeOrCylindricalFace = 1

class swsCentrifugalForceError_e(IntEnum):
    """swsCentrifugalForceError_e (6 constants, from CosmosWorksLib)."""
    swsCentrifugalForceErrorSuccessful = 0
    swsCentrifugalForceErrorSelectAxisEdgeOrCylindricalFace = 1
    swsCentrifugalForceErrorFaceNotCylindrical = 2
    swsCentrifugalForceErrorEdgeNotLinear = 3
    swsCentrifugalForceErrorAlreadyDefined = 4
    swsCentrifugalForceErrorInvalidStudyType = 5

class swsColorChartNumberFormatOptionValue_e(IntEnum):
    """swsColorChartNumberFormatOptionValue_e (3 constants, from CosmosWorksLib)."""
    swsColorChartNumberFormatScientific = 0
    swsColorChartNumberFormatFloating = 1
    swsColorChartNumberFormatGeneral = 2

class swsColorChartOptionLegendTypeValue_e(IntEnum):
    """swsColorChartOptionLegendTypeValue_e (6 constants, from CosmosWorksLib)."""
    swsColorChartOptionLegendDefault = 0
    swsColorChartOptionLegendRainbow = 1
    swsColorChartOptionLegendGrayScale = 2
    swsColorChartOptionLegendUserDefined = 3
    swsColorChartOptionLegendUnsupported = 4
    swsColorChartOptionLegendColorBlindFriendly = 5

class swsColorChartPositionValue_e(IntEnum):
    """swsColorChartPositionValue_e (2 constants, from CosmosWorksLib)."""
    swsColorChartPredefinedPosition = 0
    swsColorChartUserDefined = 1

class swsColorChartWidthOptionValue_e(IntEnum):
    """swsColorChartWidthOptionValue_e (3 constants, from CosmosWorksLib)."""
    swsColorChartWidthWide = 0
    swsColorChartWidthNormal = 1
    swsColorChartWidthThin = 2

class swsColorNumberFormatUseDiffNumberFormatOptionValue_e(IntEnum):
    """swsColorNumberFormatUseDiffNumberFormatOptionValue_e (2 constants, from CosmosWorksLib)."""
    swsColorChartNumberFormatUseDiffNoFormatFloating = 0
    swsColorChartNumberFormatUseDiffNoFormatGeneral = 1

class swsCompositeShellOptionsError_e(IntEnum):
    """swsCompositeShellOptionsError_e (12 constants, from CosmosWorksLib)."""
    swsCompositeShellOptionsErrorNoError = 0
    swsCompositeShellOptionsErrorPlyOutRange = 1
    swsCompositeShellOptionsErrorSandwich3Plies = 2
    swsCompositeShellOptionsErrorIncompatibleToMappingType = 3
    swsCompositeShellOptionsErrorUnitOutRange = 4
    swsCompositeShellOptionsErrorWrongEntity = 5
    swsCompositeShellOptionsErrorMaterialUndefined = 6
    swsCompositeShellOptionsErrorNotCompositeShell = 7
    swsCompositeShellOptionsErrorWrongInput = 8
    swsCompositeShellOptionsErrorThicknessInvalid = 9
    swsCompositeShellOptionsErrorMaterialInvalid = 10
    swsCompositeShellOptionsErrorFailed = 11

class swsCompositeShellOptionsMappingType_e(IntEnum):
    """swsCompositeShellOptionsMappingType_e (2 constants, from CosmosWorksLib)."""
    swsCompositeShellOptionsSurfaceMapping = 0
    swsCompositeShellOptionsPlanarMapping = 1

class swsConnectAnalysisDatabaseError_e(IntEnum):
    """swsConnectAnalysisDatabaseError_e (4 constants, from CosmosWorksLib)."""
    swsConnectAnalysisDatabaseErrorSuccess = 0
    swsConnectAnalysisDatabaseErrorFailed = 1
    swsConnectAnalysisDatabaseErrorInvalidPath = 2
    swsConnectAnalysisDatabaseErrorInvalidResults = 3

class swsConnectorConnectionType_e(IntEnum):
    """swsConnectorConnectionType_e (2 constants, from CosmosWorksLib)."""
    swsConnectorConnectionType_Rigid = 0
    swsConnectorConnectionType_Distributed = 1

class swsContactComponentEndEditError_e(IntEnum):
    """swsContactComponentEndEditError_e (9 constants, from CosmosWorksLib)."""
    swsContactComponentEndEditErrorSuccessful = 0
    swsContactComponentEndEditErrorContactComponentCannotBeCreated = 1
    swsContactComponentEndEditErrorInvalidContactType = 2
    swsContactComponentEndEditErrorSelectComponentOrBody = 3
    swsContactComponentEndEditErrorIncorrectCoefficientOfFriction = 4
    swsContactComponentEndEditErrorSelectSolidBodyOrComponent = 5
    swsContactComponentEndEditErrorTooManyBodiesOrComponents = 6
    swsContactComponentEndEditErrorCannotSpecifyFreeContact = 7
    swsContactComponentEndEditErrorBodiesNotTouchingBodies = 8

class swsContactSetEndEditError_e(IntEnum):
    """swsContactSetEndEditError_e (17 constants, from CosmosWorksLib)."""
    swsContactSetEndEditErrorSuccessful = 0
    swsContactSetEndEditErrorNoEntityAtIndex = 1
    swsContactSetEndEditErrorEntityAlreadySpecified = 2
    swsContactSetEndEditErrorInvalidContactSetType = 3
    swsContactSetEndEditErrorInvalidOption = 4
    swsContactSetEndEditErrorSpecifyFacesEdgesOrVerticesForSource = 5
    swsContactSetEndEditErrorSpecifyOneTargetPlaneForVirtualWall = 6
    swsContactSetEndEditErrorOnlyFacesAllowedForTarget = 7
    swsContactSetEndEditErrorStiffnessCannotBeNegative = 8
    swsContactSetEndEditErrorStiffnessMustBePositive = 9
    swsContactSetEndEditErrorIncorrectCoefficientFriction = 10
    swsContactSetEndEditErrorVerticesAndEdgesForBondingAndSurfaceContacts = 11
    swsContactSetEndEditErrorThermalResistanceMustBePositive = 12
    swsContactSetEndEditErrorContactSetsMustBeUnique = 13
    swsContactSetEndEditErrorNodeToNodeContactAndSourceTargetFaces = 14
    swsContactSetEndEditErrorBondTouchingFacesInDropTestStudies = 15
    swsContactSetEndEditErrorShrinkFitAndnterferingSourceTargetBodies = 16

class swsContactSetError_e(IntEnum):
    """swsContactSetError_e (13 constants, from CosmosWorksLib)."""
    swsContactSetErrorSuccess = 0
    swsContactSetErrorInvalidArray = 1
    swsContactSetErrorNoEntities = 2
    swsContactSetErrorInvalidType = 3
    swsContactSetErrorSpecifyFacesEdgesOrVertices = 4
    swsContactSetErrorSelectOneTargetPlane = 5
    swsContactSetErrorSelectOnlyFaces = 6
    swsContactSetErrorFaceForSourceAndTarget = 7
    swsContactSetErrorVerticesEdgesForBondingSurfaceContacts = 8
    swsContactSetErrorSourceTargetFacesMustTouch = 9
    swsContactSetErrorBondedContactForTouchingFaces = 10
    swsContactSetErrorShrinkFitNeedsIntereference = 11
    swsContactSetErrorCannotCreateContactPair = 12

class swsContactSetTypeStaticNonLinear_e(IntEnum):
    """swsContactSetTypeStaticNonLinear_e (5 constants, from CosmosWorksLib)."""
    swsContactSetTypeStaticNonLinearNoPenetration = 0
    swsContactSetTypeStaticNonLinearBonded = 1
    swsContactSetTypeStaticNonLinearShrinkFit = 2
    swsContactSetTypeStaticNonLinearFree = 3
    swsContactSetTypeStaticNonLinearVirtualWall = 4

class swsContactSetTypeThermal_e(IntEnum):
    """swsContactSetTypeThermal_e (3 constants, from CosmosWorksLib)."""
    swsContactSetTypeThermalResistance = 0
    swsContactSetTypeThermalBonded = 1
    swsContactSetTypeThermalInsulated = 2

class swsContactSuppressUnsuppressError_e(IntEnum):
    """swsContactSuppressUnsuppressError_e (3 constants, from CosmosWorksLib)."""
    swsContactSuppressUnsuppressErrorSuccessful = 0
    swsContactSuppressUnsuppressErrorContactNotFound = 1
    swsContactSuppressUnsuppressErrorInvalidName = 2

class swsContactType_e(IntEnum):
    """swsContactType_e (4 constants, from CosmosWorksLib)."""
    swsContactTypeBonded = 0
    swsContactTypeFreeOrInsulated = 1
    swsContactTypeAllowPenetration = 1
    swsContactTypeStaticNoPenetration = 2

class swsConvectionEndEditError_e(IntEnum):
    """swsConvectionEndEditError_e (6 constants, from CosmosWorksLib)."""
    swsConvectionEndEditErrorSuccessful = 0
    swsConvectionEndEditErrorNoEntityAtIndex = 1
    swsConvectionEndEditErrorEntityAlreadyAdded = 2
    swsConvectionEndEditErrorNoEntitySelected = 3
    swsConvectionEndEditErrorSelectFace = 4
    swsConvectionEndEditErrorSelectFaceOrEdge = 5

class swsConvectionError_e(IntEnum):
    """swsConvectionError_e (6 constants, from CosmosWorksLib)."""
    swsConvectionErrorSuccessful = 0
    swsConvectionErrorFacesAndShellEdgesAllowed = 1
    swsConvectionErrorSelectFacesOrShellEdge = 2
    swsConvectionErrorInvalidStudyType = 3
    swsConvectionErrorInvalidArray = 4
    swsConvectionErrorEmptyArray = 5

class swsCoordinateType_e(IntEnum):
    """swsCoordinateType_e (3 constants, from CosmosWorksLib)."""
    swsCoordinateTypeCartesian = 1
    swsCoordinateTypeSpherical = 2
    swsCoordinateTypeCylindrical = 3

class swsCopyItemsError_e(IntEnum):
    """swsCopyItemsError_e (10 constants, from CosmosWorksLib)."""
    swsCopyItem_Success = 0
    swsCopyItem_CopyFailure = 1
    swsCopyItem_DifferentJointVersion = 2
    swsCopyItem_InstanceAlreadyDefined = 3
    swsCopyItem_SourceTargetStudyPairInvalid = 4
    swsCopyItem_SourceItemNotFound = 5
    swsCopyItem_TargetStudyNotFound = 6
    swsCopyItem_SourceStudyNotActive = 7
    swsCopyItem_InvalidArray = 8
    swsCopyItem_UnknownError = 9

class swsCosmosExportOption_e(IntEnum):
    """swsCosmosExportOption_e (2 constants, from CosmosWorksLib)."""
    swsExportFEMOnly = 1
    swsExportGeometryOnly = 2

class swsCreateAnalysisDatabaseError_e(IntEnum):
    """swsCreateAnalysisDatabaseError_e (24 constants, from CosmosWorksLib)."""
    swsCreateAnalysisDBSuccessful = 0
    swsCreateAnalysisDBUseHighQualityMesh = 1
    swsCreateAnalysisDBDefineRigidVirtualWallContact = 2
    swsCreateAnalysisDBDefineInitialTemperature = 3
    swsCreateAnalysisDBMultipleLoadsUseSameTimeCurve = 4
    swsCreateAnalysisDBSetUpDropTestStudy = 5
    swsCreateAnalysisDBNeedOneOrMoreStaticStudies = 6
    swsCreateAnalysisDBNoFatigueEvent = 7
    swsCreateAnalysisDBTimeDependentOrAmplitideOnlyLoads = 8
    swsCreateAnalysisDBNoSNCurve = 9
    swsCreateAnalysisDBMeshNotIdentical = 11
    swsCreateAnalysisDBNoValidShell = 12
    swsCreateAnalysisDBEXMaterialPropertyNotDefined = 13
    swsCreateAnalysisDBEXValue = 14
    swsCreateAnalysisDBPoissonsRatio = 15
    swsCreateAnalysisDBThermalConductivityNotDefined = 16
    swsCreateAnalysisDBRemoveOrChangeCreep = 17
    swsCreateAnalysisDBMaterialNotDefinedForShells = 18
    swsCreateAnalysisDBMaterialNotDefined = 19
    swsCreateAnalysisDBMaterialNotDefinedForComponents = 20
    swsCreateAnalysisDBNoSolidBody = 21
    swsCreateAnalysisDBAuthorizationFailed = 22
    swsCreateAnalysisDBMeshFailed = 23
    swsCreateAnalysisDBFailed = 24

class swsCreateDeformedBodyAdvancedOption_e(IntEnum):
    """swsCreateDeformedBodyAdvancedOption_e (4 constants, from CosmosWorksLib)."""
    swsCreateDeformedBodyAdvanced_OutputBodyOnly = 1
    swsCreateDeformedBodyAdvanced_OutputTessellation = 2
    swsCreateDeformedBodyAdvanced_OutputSurfaces = 4
    swsCreateDeformedBodyAdvanced_OutputMesh = 8

class swsCreateDeformedBodyError_e(IntEnum):
    """swsCreateDeformedBodyError_e (11 constants, from CosmosWorksLib)."""
    swsCreateDeformedBody_CorruptData = 1
    swsCreateDeformedBody_UnfitFace = 2
    swsCreateDeformedBody_FailToSew = 3
    swsCreateDeformedBody_DisjointBodies = 4
    swsCreateDeformedBody_FailedToSubtractBody = 5
    swsCreateDeformedBody_IncorrectParameters = 6
    swsCreateDeformedBody_Failed = 7
    swsCreateDeformedBody_IncorrectStepNumber = 8
    swsCreateDeformedBody_NoActiveStudy = 9
    swsCreateDeformedBody_NonSupportedStudy = 10
    swsCreateDeformedBody_InvalidPath = 11

class swsCreateDeformedBodyFailedSewOption_e(IntEnum):
    """swsCreateDeformedBodyFailedSewOption_e (4 constants, from CosmosWorksLib)."""
    swsCreateDeformedBodyFailedSewAsDefault = 1
    swsCreateDeformedBodyFailedSewAsTessellation = 2
    swsCreateDeformedBodyFailedSewAsSurfaces = 3
    swsCreateDeformedBodyFailedSewCancel = 4

class swsCreateDeformedBodyOption_e(IntEnum):
    """swsCreateDeformedBodyOption_e (2 constants, from CosmosWorksLib)."""
    swsCreateDeformedBodyAsPart = 1
    swsCreateDeformedBodyAsConfiguration = 2

class swsCyclicRestraintError_e(IntEnum):
    """swsCyclicRestraintError_e (7 constants, from CosmosWorksLib)."""
    swsCyclicRestraintErrorSuccessful = 0
    swsCyclicRestraintErrorInvalidStudyType = 1
    swsCyclicRestraintErrorNotApplicableForBeams = 2
    swsCyclicRestraintErrorNoFirstFace = 3
    swsCyclicRestraintErrorNoSecondFace = 4
    swsCyclicRestraintErrorNoAxis = 5
    swsCyclicRestraintErrorUnSuccessful = 6

class swsDampingType_e(IntEnum):
    """swsDampingType_e (2 constants, from CosmosWorksLib)."""
    swsDampingType_Modal = 0
    swsDampingType_Rayleigh = 1

class swsDefaultStaticResultTypes_e(IntEnum):
    """swsDefaultStaticResultTypes_e (7 constants, from CosmosWorksLib)."""
    swsStaticResultNodalStress = 0
    swsStaticResultElementalStress = 1
    swsStaticResultDisplacement = 2
    swsStaticResultNodalStrain = 3
    swsStaticResultElementalStrain = 4
    swsStaticResultFactorOfSafety = 5
    swsStaticResultBoltPinCheck = 6

class swsDeformType_e(IntEnum):
    """swsDeformType_e (3 constants, from CosmosWorksLib)."""
    swsAutomatic = 0
    swsTrueScale = 1
    swsUserDefined = 2

class swsDeleteStudyPlotsResultTypes_e(IntEnum):
    """swsDeleteStudyPlotsResultTypes_e (2 constants, from CosmosWorksLib)."""
    swsDeleteStudyPlotsNoError = 0
    swsDeleteStudyPlotsError = 1

class swsDisplacementComponent_e(IntEnum):
    """swsDisplacementComponent_e (15 constants, from CosmosWorksLib)."""
    swsDisplacementComponentUX = 0
    swsDisplacementComponentUY = 1
    swsDisplacementComponentUZ = 2
    swsDisplacementComponentURES = 3
    swsDisplacementComponentRFX = 4
    swsDisplacementComponentRFY = 5
    swsDisplacementComponentRFZ = 6
    swsDisplacementComponentRFRES = 7
    swsDisplacementComponentRX = 8
    swsDisplacementComponentRY = 9
    swsDisplacementComponentRZ = 10
    swsDisplacementComponentRMX = 11
    swsDisplacementComponentRMY = 12
    swsDisplacementComponentRMZ = 13
    swsDisplacementComponentRMRES = 14

class swsDisplayOption_e(IntEnum):
    """swsDisplayOption_e (2 constants, from CosmosWorksLib)."""
    swsShowSolidAndShells = 0
    swsShowBeam = 1

class swsDistributedMassError_e(IntEnum):
    """swsDistributedMassError_e (6 constants, from CosmosWorksLib)."""
    swsDistributedMassError_NoError = 0
    swsDistributedMassError_NotAvailable = 1
    swsDistributedMassError_ImproperEntities = 2
    swsDistributedMassError_SelectOnlyFaces = 3
    swsDistributedMassError_InvalidUnits = 4
    swsDistributedMassError_InvalidMass = 5

class swsDistributedSimulationError_e(IntEnum):
    """swsDistributedSimulationError_e (8 constants, from CosmosWorksLib)."""
    swsDistributedSimulation_NoError = 0
    swsDistributedSimulation_NetSimulationNotSupport = 1
    swsDistributedSimulation_NetComputerNotAvailable = 2
    swsDistributedSimulation_EmptyNetComputerNames = 3
    swsDistributedSimulation_UnaccessNetComputerNames = 4
    swsDistributedSimulation_NetComputerNameWrongType = 5
    swsDistributedSimulation_NoStudySupportNetSimulation = 6
    swsDistributedSimulation_UnknownError = 7

class swsDropHeightType_e(IntEnum):
    """swsDropHeightType_e (2 constants, from CosmosWorksLib)."""
    swsDropHeightType_FromCentroid = 0
    swsDropHeightType_FromLowestPoint = 1

class swsDropTargetOrientationType_e(IntEnum):
    """swsDropTargetOrientationType_e (2 constants, from CosmosWorksLib)."""
    swsDropTargetOrientationType_NormalToGravity = 0
    swsDropTargetOrientationType_ParallelToRefPlane = 1

class swsDropTargetStiffnessType_e(IntEnum):
    """swsDropTargetStiffnessType_e (2 constants, from CosmosWorksLib)."""
    swsDropTargetStiffnessType_RigidTarget = 0
    swsDropTargetStiffnessType_FlexibleTarget = 1

class swsDropTestSetUpError_e(IntEnum):
    """swsDropTestSetUpError_e (7 constants, from CosmosWorksLib)."""
    swsDropTestSetUpError_NoError = 0
    swsDropTestSetUpError_AvailableOnlyForDropTestStudy = 1
    swsDropTestSetUpError_SetUpAlreadyAdded = 2
    swsDropTestSetUpError_GravityEntityIsNULL = 3
    swsDropTestSetUpError_GravityEntityShouldBeEdgeFaceOrPlane = 4
    swsDropTestSetUpError_ShouldBeStraightEdgeOrPlaneFace = 5
    swsDropTestSetUpError_SetupNotExists = 6

class swsDropTestStudyResultType_e(IntEnum):
    """swsDropTestStudyResultType_e (4 constants, from CosmosWorksLib)."""
    swsDropTestResultNodalStress = 0
    swsDropTestResultElementalStress = 1
    swsDropTestResultDisplacement = 2
    swsDropTestResultElementalStrain = 3

class swsDropType_e(IntEnum):
    """swsDropType_e (2 constants, from CosmosWorksLib)."""
    swsDropType_DropHeight = 0
    swsDropType_VelocityAtImpact = 1

class swsDuplicateStudyError_e(IntEnum):
    """swsDuplicateStudyError_e (2 constants, from CosmosWorksLib)."""
    swsDuplicateStudyErrorNoError = 0
    swsDuplicateStudyErrorFailed = 1

class swsDynamicAnalysisSubType_e(IntEnum):
    """swsDynamicAnalysisSubType_e (4 constants, from CosmosWorksLib)."""
    swsDynamicAnalysisSubTypeTransient = 0
    swsDynamicAnalysisSubTypeHarmonic = 1
    swsDynamicAnalysisSubTypeRandom = 2
    swsDynamicAnalysisSubTypeResponse = 3

class swsDynamicExtraFrequenciesError_e(IntEnum):
    """swsDynamicExtraFrequenciesError_e (6 constants, from CosmosWorksLib)."""
    swsDynamicExtraFrequenciesError_NoError = 0
    swsDynamicExtraFrequenciesError_NotAvailable = 1
    swsDynamicExtraFrequenciesError_NotAvailableForSubType = 2
    swsDynamicExtraFrequenciesError_DynamicParamEmpty = 3
    swsDynamicExtraFrequenciesError_OutOfRange = 4
    swsDynamicExtraFrequenciesError_InvalidInput = 5

class swsDynamicInitialConditionError_e(IntEnum):
    """swsDynamicInitialConditionError_e (15 constants, from CosmosWorksLib)."""
    swsDynamicInitialConditionError_NoError = 0
    swsDynamicInitialConditionError_NotAvailable = 1
    swsDynamicInitialConditionError_InvalidEntityArray = 2
    swsDynamicInitialConditionError_SelectOnlyJoints = 3
    swsDynamicInitialConditionError_SelectOnlyBeams = 4
    swsDynamicInitialConditionError_NoFacesOnBeamsAllowed = 5
    swsDynamicInitialConditionError_SelectOnlyFaceBodyOrComps = 6
    swsDynamicInitialConditionError_InvalidRefGeom = 7
    swsDynamicInitialConditionError_RefGeomAlreadySelected = 8
    swsDynamicInitialConditionError_OnlyEdgePlaneOrFaceForReference = 9
    swsDynamicInitialConditionError_OnlyFlatFaceOrStraightEdge = 10
    swsDynamicInitialConditionError_InvalidType = 11
    swsDynamicInitialConditionError_CheckAtleastOneComp = 12
    swsDynamicInitialConditionError_AllValuesZero = 13
    swsDynamicInitialConditionError_CheckOnlyThirdComp = 14

class swsDynamicInitialConditionType_e(IntEnum):
    """swsDynamicInitialConditionType_e (3 constants, from CosmosWorksLib)."""
    swsDynamicInitialConditionType_Displacement = 0
    swsDynamicInitialConditionType_Velocity = 1
    swsDynamicInitialConditionType_Acceleration = 2

class swsEdgeWeldConnectorSafetyFactorLiftOption_e(IntEnum):
    """swsEdgeWeldConnectorSafetyFactorLiftOption_e (2 constants, from CosmosWorksLib)."""
    swsEdgeWeldConnectorSafetyFactorLiftOption_USAutomotiveLifts = 0
    swsEdgeWeldConnectorSafetyFactorLiftOption_UnderTheHookLifting = 1

class swsEdgeWeldConnectorTypes_e(IntEnum):
    """swsEdgeWeldConnectorTypes_e (4 constants, from CosmosWorksLib)."""
    swsEdgeWeldConnectorFilletDoubleSided = 0
    swsEdgeWeldConnectorFilletSingleSided = 1
    swsEdgeWeldConnectorGrooveDoubleSided = 2
    swsEdgeWeldConnectorGrooveSingleSided = 3

class swsEdgeWeldCreationErrorCode_e(IntEnum):
    """swsEdgeWeldCreationErrorCode_e (6 constants, from CosmosWorksLib)."""
    swsEdgeWeldCreationError_NoError = 0
    swsEdgeWeldCreationError_InvalidModelDoc = 1
    swsEdgeWeldCreationError_InvalidOrNullFace = 2
    swsEdgeWeldCreationError_InvalidWeldStyle = 3
    swsEdgeWeldCreationError_NoEdgeSelection = 4
    swsEdgeWeldCreationError_WrongEdgeSelection = 5

class swsEdgeWeldSolverCode_e(IntEnum):
    """swsEdgeWeldSolverCode_e (2 constants, from CosmosWorksLib)."""
    swsEdgeWeldSolverCodeAWS = 0
    swsEdgeWeldSolverCodeEURO = 1

class swsElasticConnectorEndEditError_e(IntEnum):
    """swsElasticConnectorEndEditError_e (12 constants, from CosmosWorksLib)."""
    swsElasticConnectorEndEditErrorSuccessful = 0
    swsElasticConnectorEndEditErrorNoEntityAtIndex = 1
    swsElasticConnectorEndEditErrorEntityAlreadyAdded = 2
    swsElasticConnectorEndEditErrorSelectFace = 3
    swsElasticConnectorEndEditErrorSelectPlanarFace = 4
    swsElasticConnectorEndEditErrorSelectNonNegativeValueForNormalOrShearStiffness = 5
    swsElasticConnectorEndEditErrorSelectNonZeroValueForNormalOrShearStiffness = 6
    swsElasticConnectorEndEditErrorSelectEntity = 7
    swsElasticConnectorEndEditErrorHasBeamBody = 8
    swsElasticConnectorEndEditErrorHasMassElement = 9
    swsElasticConnectorEndEditErrorBodyExcludedFromAnalysis = 10
    swsElasticConnectorEndEditErrorNullEntity = 11

class swsElasticConnectorError_e(IntEnum):
    """swsElasticConnectorError_e (11 constants, from CosmosWorksLib)."""
    swsElasticConnectorErrorSuccessful = 0
    swsElasticConnectorErrorInvalidMesh = 1
    swsElasticConnectorErrorNonlinearStudyAndPartDocument = 2
    swsElasticConnectorErrorInvalidStudy = 3
    swsElasticConnectorErrorInvalidArray = 4
    swsElasticConnectorErrorSelectFace = 5
    swsElasticConnectorErrorSelectPlanarFace = 6
    swsElasticConnectorErrorNoEntityNoObject = 7
    swsElasticConnectorErrorNullOrEmptyArray = 8
    swsElasticConnectorErrorFaceHasRemoteMassOrBeamBody = 9
    swsElasticConnectorErrorBodyExcludedFromAnalysis = 10

class swsElectrodeMaterialTypes_e(IntEnum):
    """swsElectrodeMaterialTypes_e (14 constants, from CosmosWorksLib)."""
    swsElectrodeMaterialE60 = 0
    swsElectrodeMaterialE70 = 1
    swsElectrodeMaterialE80 = 2
    swsElectrodeMaterialE90 = 3
    swsElectrodeMaterialE100 = 4
    swsElectrodeMaterialCustomSteel = 5
    swsElectrodeMaterial1100 = 6
    swsElectrodeMaterial4043 = 7
    swsElectrodeMaterial5183 = 8
    swsElectrodeMaterial5356 = 9
    swsElectrodeMaterial5554 = 10
    swsElectrodeMaterial5556 = 11
    swsElectrodeMaterial5654 = 12
    swsElectrodeMaterialCustomAl = 13

class swsEnvelopePlotType_e(IntEnum):
    """swsEnvelopePlotType_e (3 constants, from CosmosWorksLib)."""
    swsEnvelopePlotType_Maximum = 0
    swsEnvelopePlotType_Minimum = 1
    swsEnvelopePlotType_AbsoluteMaximum = 2

class swsEstimatedWeldSizeUnits_e(IntEnum):
    """swsEstimatedWeldSizeUnits_e (11 constants, from CosmosWorksLib)."""
    swsEstimatedWeldSizeUnits_mm = 0
    swsEstimatedWeldSizeUnits_cm = 1
    swsEstimatedWeldSizeUnits_m = 2
    swsEstimatedWeldSizeUnits_in = 3
    swsEstimatedWeldSizeUnits_ft = 4
    swsEstimatedWeldSizeUnits_ft_in = 5
    swsEstimatedWeldSizeUnits_am = 6
    swsEstimatedWeldSizeUnits_nm = 7
    swsEstimatedWeldSizeUnits_micron = 8
    swsEstimatedWeldSizeUnits_mil = 9
    swsEstimatedWeldSizeUnits_microIn = 10

class swsExportSmoothedMeshError_e(IntEnum):
    """swsExportSmoothedMeshError_e (10 constants, from CosmosWorksLib)."""
    swsExportSmoothedMesh_Succeeded = 0
    swsExportSmoothedMesh_IncorrectParameters = 1
    swsExportSmoothedMesh_Failed = 2
    swsExportSmoothedMesh_NoActiveStudy = 3
    swsExportSmoothedMesh_NonSupportedStudy = 4
    swsExportSmoothedMesh_InvalidPath = 5
    swsExportSmoothedMesh_PlotDataUnavailable = 6
    swsExportSmoothedMesh_ConfigurationNameAlreadyExist = 7
    swsExportSmoothedMesh_CorruptedInputData = 8
    swsExportSmoothedMesh_PlotDoesNotExist = 9

class swsExportSmoothedMeshOption_e(IntEnum):
    """swsExportSmoothedMeshOption_e (3 constants, from CosmosWorksLib)."""
    swsSaveSmoothedMeshIntoCurrentActiveConfiguration = 0
    swsSaveSmoothedMeshIntoNewConfiguration = 1
    swsSaveSmoothedMeshIntoNewPart = 2

class swsFOS_CompositeCriterion_e(IntEnum):
    """swsFOS_CompositeCriterion_e (4 constants, from CosmosWorksLib)."""
    swsFOSCompositeCriterion_Tsai_Hill = 0
    swsFOSCompositeCriterion_Tsai_Wu = 1
    swsFOSCompositeCriterion_Max_Normal_Stress = 2
    swsFOSCompositeCriterion_Automatic = 3

class swsFOS_DistributionOpt_e(IntEnum):
    """swsFOS_DistributionOpt_e (2 constants, from CosmosWorksLib)."""
    swsFOS_DistributionOpt_Distribution = 1
    swsFOS_DistributionOpt_AreaBelowFOS = 2

class swsFOS_ErrorCode_e(IntEnum):
    """swsFOS_ErrorCode_e (9 constants, from CosmosWorksLib)."""
    swsFOS_ErrorCode_NoError = 0
    swsFOS_ErrorCode_NullPostApp = 1
    swsFOS_ErrorCode_PlyNumExceeded = 2
    swsFOS_ErrorCode_NoSolidBodiesSel = 3
    swsFOS_ErrorCode_InvalidSelEntityArr = 4
    swsFOS_ErrorCode_NoPersistID = 5
    swsFOS_ErrorCode_InvalidSolidMgr = 6
    swsFOS_ErrorCode_InvalidSel = 7
    swsFOS_ErrorCode_FailureFrmGetPlotData = 8

class swsFOS_NonCompositeCriterion_e(IntEnum):
    """swsFOS_NonCompositeCriterion_e (5 constants, from CosmosWorksLib)."""
    swsFOSNonCompositeCriterion_VonMisesHencky = 0
    swsFOSNonCompositeCriterion_Tresca = 1
    swsFOSNonCompositeCriterion_MohrCoulomb = 2
    swsFOSNonCompositeCriterion_Coulomb = 3
    swsFOSNonCompositeCriterion_Automatic = 4

class swsFOS_NormalShellFaceOption_e(IntEnum):
    """swsFOS_NormalShellFaceOption_e (4 constants, from CosmosWorksLib)."""
    swsFOS_NormalShellFaceOption_Top = 1
    swsFOS_NormalShellFaceOption_Bottom = 2
    swsFOS_NormalShellFaceOption_Min = 3
    swsFOS_NormalShellFaceOption_Max = 4

class swsFOS_ShellFaceOption_e(IntEnum):
    """swsFOS_ShellFaceOption_e (4 constants, from CosmosWorksLib)."""
    swsFOS_ShellFaceOption_TopFace = 1
    swsFOS_ShellFaceOption_BottomFace = 2
    swsFOS_ShellFaceOption_MinAmongTopAndBottomFace = 3
    swsFOS_ShellFaceOption_MaxAmongTopAndBottomFace = 4

class swsFactorOfSafetyStressLimitOption_e(IntEnum):
    """swsFactorOfSafetyStressLimitOption_e (3 constants, from CosmosWorksLib)."""
    swsFactorOfSafetyStressLimitOption_YieldStrength = 0
    swsFactorOfSafetyStressLimitOption_UltimateStrength = 1
    swsFactorOfSafetyStressLimitOption_UserDefined = 2

class swsFatigueAlternatingStressOption_e(IntEnum):
    """swsFatigueAlternatingStressOption_e (3 constants, from CosmosWorksLib)."""
    swsFatigueAlternatingStressOption_StressIntensity = 0
    swsFatigueAlternatingStressOption_EquivalentStress = 1
    swsFatigueAlternatingStressOption_MaxAbsPrincipal = 2

class swsFatigueCalculationsOption_e(IntEnum):
    """swsFatigueCalculationsOption_e (2 constants, from CosmosWorksLib)."""
    swsFatigueCalculationsOption_WholeModel = 0
    swsFatigueCalculationsOption_SurfaceOnly = 1

class swsFatigueCalculations_e(IntEnum):
    """swsFatigueCalculations_e (2 constants, from CosmosWorksLib)."""
    swsFatigueCalculations_WholeModel = 0
    swsFatigueCalculations_SurfaceOnly = 1

class swsFatigueComponent_e(IntEnum):
    """swsFatigueComponent_e (4 constants, from CosmosWorksLib)."""
    swsFatigueComponent_Life = 0
    swsFatigueComponent_Damage = 1
    swsFatigueComponent_LoadFactor = 2
    swsFatigueComponent_BiaxialityIndicator = 3

class swsFatigueEventEndEditError_e(IntEnum):
    """swsFatigueEventEndEditError_e (22 constants, from CosmosWorksLib)."""
    swsFatigueEventError_NoError = 0
    swsFatigueEventError_ImproperStudy = 1
    swsFatigueEventError_ImproperEvent = 2
    swsFatigueEventError_ImproperStudyNames = 3
    swsFatigueEventError_LoadHistoryCurveTypeImproper = 4
    swsFatigueEventError_XCurveDataImproper = 5
    swsFatigueEventError_YCurveDataImproper = 6
    swsFatigueEventError_XAndYPointsNotSameInNumber = 7
    swsFatigueEventError_NoOfPointsShouldBeMoreThan3 = 8
    swsFatigueEventError_XPointsShouldBeInIncreasingOrder = 9
    swsFatigueEventError_ImproperNoOfCycles = 10
    swsFatigueEventError_InvalidLoadingtype = 11
    swsFatigueEventError_CannotApplyLoadingRatio = 12
    swsFatigueEventError_CannotApplyRepeats = 13
    swsFatigueEventError_InvalidRepeats = 14
    swsFatigueEventError_CannotApplyStartTime = 15
    swsFatigueEventError_InvalidStartTime = 16
    swsFatigueEventError_StudyNamesScalesAndStepsDifferentInNumber = 17
    swsFatigueEventError_ImproperVarNamesOrVarScalesOrVarSteps = 18
    swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast1 = 19
    swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast2 = 20
    swsFatigueEventError_AssociatedStudyShouldBeStaticNonlinearOrDynamicModalTimeHistory = 21

class swsFatigueEventInteraction_e(IntEnum):
    """swsFatigueEventInteraction_e (2 constants, from CosmosWorksLib)."""
    swsFatigueEventInteraction_Random = 0
    swsFatigueEventInteraction_NoInteraction = 1

class swsFatigueLoadHistoryCurveType_e(IntEnum):
    """swsFatigueLoadHistoryCurveType_e (3 constants, from CosmosWorksLib)."""
    swsFatigueLoadHistoryCurveType_AmplitudeOnly = 0
    swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude = 1
    swsFatigueLoadHistoryCurveType_TimeAndAmplitude = 2

class swsFatigueLoadingType_e(IntEnum):
    """swsFatigueLoadingType_e (4 constants, from CosmosWorksLib)."""
    swsFatigueLoadingType_FullyReversed = 0
    swsFatigueLoadingType_ZeroBased = 1
    swsFatigueLoadingType_LoadingRatio = 2
    swsFatigueLoadingType_NonProportional = 3

class swsFatigueMeanStressCorrectionType_e(IntEnum):
    """swsFatigueMeanStressCorrectionType_e (4 constants, from CosmosWorksLib)."""
    swsFatigueMeanStressCorrectionType_None = 0
    swsFatigueMeanStressCorrectionType_Goodman = 1
    swsFatigueMeanStressCorrectionType_Gerber = 2
    swsFatigueMeanStressCorrectionType_Soderberg = 3

class swsFatiguePlotType_e(IntEnum):
    """swsFatiguePlotType_e (4 constants, from CosmosWorksLib)."""
    swsFatiguePlotType_Life = 0
    swsFatiguePlotType_Damage = 1
    swsFatiguePlotType_LoadFactor = 2
    swsFatiguePlotType_BiaxialityIndicator = 3

class swsFatigueRandomVibrationComputationalMethod_e(IntEnum):
    """swsFatigueRandomVibrationComputationalMethod_e (3 constants, from CosmosWorksLib)."""
    swsFatigue_NarrowBand = 0
    swsFatigue_Steinberg = 1
    swsFatigue_Wirsching = 2

class swsFatigueStudyResultType_e(IntEnum):
    """swsFatigueStudyResultType_e (4 constants, from CosmosWorksLib)."""
    swsFatigueStudy_LifePlot = 0
    swsFatigueStudy_DamagePlot = 1
    swsFatigueStudy_LoadFactor = 2
    swsFatigueStudy_BiAxialityIndicatorPlot = 3

class swsFatigueStudySubOption_e(IntEnum):
    """swsFatigueStudySubOption_e (4 constants, from CosmosWorksLib)."""
    swsFatigueConstantAmplitude = 0
    swsFatigueVariableAmplitude = 1
    swsFatigueHarmonic = 2
    swsFatigueRandomVibration = 3

class swsFlipOffsetDir_e(IntEnum):
    """swsFlipOffsetDir_e (2 constants, from CosmosWorksLib)."""
    swsNegativeDir = 0
    swsPositiveDir = 1

class swsForceEndEditError_e(IntEnum):
    """swsForceEndEditError_e (13 constants, from CosmosWorksLib)."""
    swsForceEndEditErrorSuccessful = 0
    swsForceEndEditErrorNoEntityAtIndex = 1
    swsForceEndEditErrorEntityAlreadyExists = 2
    swsForceEndEditErrorNoEntitiesSelected = 3
    swsForceEndEditErrorSelectFaceEdgeOrVertex = 4
    swsForceEndEditErrorReferenceGeometryEntityNotSelected = 5
    swsForceEndEditErrorSelectFaceEdgePlaneOrAxisForReferenceGeometry = 6
    swsForceEndEditErrorSelectFace = 7
    swsForceEndEditErrorSelectCoordinateSystem = 8
    swsForceEndEditErrorVariableForceCannotBeAppliedToVerticesOrEdges = 9
    swsForceEndEditErrorSelectReferenceAxisOrCylindricalFaceForTorque = 10
    swsForceEndEditErrorMagnitudeForceMustBeLargerZero = 11
    swsForceEndEditErrorVariableForceCannotBeAppliedToVertices = 12

class swsForceError_e(IntEnum):
    """swsForceError_e (16 constants, from CosmosWorksLib)."""
    swsForceErrorSuccessful = 0
    swsForceErrorSelectFacesEdgesVerticesOrPoints = 1
    swsForceErrorSelectFaceEdgePlaneOrAxis = 2
    swsForceErrorApplyNormalForceToFacesAndShellEdges = 3
    swsForceErrorSelectReferenceAxisOrCylindricalFace = 4
    swsForceErrorInvalidStudyType = 5
    swsForceErrorInvalidArray = 6
    swsForceErrorInvalidForceType = 7
    swsForceErrorNoEntities = 8
    swsForceErrorCannotApplyNonuniformForce = 9
    swsForceErrorCannotApplyForce = 10
    swsForceErrorCannotApplyNonuniformLoadOnMultipleBeam = 18
    swsForceErrorCannotApplyZeroLoading = 19
    swsForceErrorInvalidSelectionType = 20
    swsForceErrorNonUniformBeamLoadInvalidTableData = 21
    swsForceErrorNonUniformBeamLoadInvalidTableDistData = 22

class swsForceType_e(IntEnum):
    """swsForceType_e (3 constants, from CosmosWorksLib)."""
    swsForceTypeForceOrMoment = 0
    swsForceTypeNormal = 1
    swsForceTypeTorque = 2

class swsForceUnit_e(IntEnum):
    """swsForceUnit_e (3 constants, from CosmosWorksLib)."""
    swsForceUnitNOrNm = 0
    swsForceUnitlbOrlbin = 1
    swsForceUnitkgfOrkgfcm = 2

class swsFosPlotErrorCode_e(IntEnum):
    """swsFosPlotErrorCode_e (17 constants, from CosmosWorksLib)."""
    swsFos_NoError = 0
    swsFos_NoView = 1
    swsFos_NullPostApp = 2
    swsFos_NoDatabase = 3
    swsFos_NoPostFile = 4
    swsFos_APIExists = 5
    swsFos_InvalidComponent = 6
    swsFos_InvalidResults = 7
    swsFos_NoMaterialFound = 8
    swsFos_ComponentsHidden = 9
    swsFos_AllMaterialFailed = 10
    swsFos_InvalidShellOption = 11
    swsFos_InvalidSelEntityArr = 12
    swsFos_NoPersistID = 13
    swsFos_InvalidSolidMgr = 14
    swsFos_InvalidSel = 15
    swsFos_FailureFrmGetPlotData = 16

class swsFrequencyBucklingResultDisplacementComponentTypes_e(IntEnum):
    """swsFrequencyBucklingResultDisplacementComponentTypes_e (4 constants, from CosmosWorksLib)."""
    swsFrequencyBucklingDisplacement_UX = 0
    swsFrequencyBucklingDisplacement_UY = 1
    swsFrequencyBucklingDisplacement_UZ = 2
    swsFrequencyBucklingDisplacement_URES = 3

class swsFrequencyCapOption_e(IntEnum):
    """swsFrequencyCapOption_e (2 constants, from CosmosWorksLib)."""
    swsFrequencyCapAutomatic = 0
    swsFrequencyCapUserDefined = 1

class swsFrequencyStudyOption_e(IntEnum):
    """swsFrequencyStudyOption_e (2 constants, from CosmosWorksLib)."""
    swsFrequencyStudyOptionNumberFrequencies = 0
    swsFrequencyStudyOptionUseUpperBoundFrequency = 1

class swsFrequencyUnit_e(IntEnum):
    """swsFrequencyUnit_e (2 constants, from CosmosWorksLib)."""
    swsFrequencyUnit_RadiansPerSec = 0
    swsFrequencyUnit_CyclesPerSec = 1

class swsGapType_e(IntEnum):
    """swsGapType_e (2 constants, from CosmosWorksLib)."""
    swsGapTypeAlwaysIgnoreClearance = 0
    swsGapTypeIgnoreIfSmallerThanSpecifiedClearance = 1

class swsGaussIntegrationOrder_e(IntEnum):
    """swsGaussIntegrationOrder_e (2 constants, from CosmosWorksLib)."""
    swsGaussIntegrationOrder_2Pt = 0
    swsGaussIntegrationOrder_3Pt = 1

class swsGeneralSpringError_e(IntEnum):
    """swsGeneralSpringError_e (20 constants, from CosmosWorksLib)."""
    swsGeneralSpringErrorSuccessful = 0
    swsGeneralSpringErrorInvalidMesh = 1
    swsGeneralSpringErrorInvalidStudy = 2
    swsGeneralSpringErrorSelectFace = 3
    swsGeneralSpringErrorSelectCoordSys = 4
    swsGeneralSpringErrorSelectTwoFaces = 5
    swsGeneralSpringErrorSourceTargetEntitiesSame = 6
    swsGeneralSpringErrorNumberFacesLessThanTwo = 7
    swsGeneralSpringErrorNoObjectForSourceOrTarget = 8
    swsGeneralSpringErrorSelectionsOnSameComponent = 9
    swsGeneralSpringErrorHasRemoteMass = 10
    swsGeneralSpringErrorBodyExcludedFromAnalysis = 11
    swsGeneralSpringErrorFaceDispNull = 12
    swsGeneralSpringErrorFaceOnBeam = 13
    swsGeneralSpringErrorNegativeStiffness = 14
    swsGeneralSpringErrorNegativePreloadForce = 15
    swsGeneralSpringErrorStiffnessAllZero = 16
    swsGeneralSpringErrorFeatureNotReady = 17
    swsGeneralSpringErrorFeatureNotSupported = 18
    swsGeneralSpringErrorFeatureNotLicensed = 19

class swsGenerateReportError_e(IntEnum):
    """swsGenerateReportError_e (6 constants, from CosmosWorksLib)."""
    swsGenerateReportErrorNoError = 0
    swsGenerateReportErrorWrongPath = 1
    swsGenerateReportErrorWrongConfiguration = 2
    swsGenerateReportErrorInvalidModelDoc = 3
    swsGenerateReportErrorInactiveStudy = 4
    swsGenerateReportErrorFailed = 5

class swsGeoStarExportUnit_e(IntEnum):
    """swsGeoStarExportUnit_e (5 constants, from CosmosWorksLib)."""
    swsGeoStarExportUnit_mm = 0
    swsGeoStarExportUnit_cm = 1
    swsGeoStarExportUnit_m = 2
    swsGeoStarExportUnit_in = 3
    swsGeoStarExportUnit_ft = 4

class swsGravityEndEditError_e(IntEnum):
    """swsGravityEndEditError_e (3 constants, from CosmosWorksLib)."""
    swsGravityEndEditErrorSuccessful = 0
    swsGravityEndEditErrorSpecifyReferencePlaneFaceOrEdge = 1
    swsGravityEndEditErrorValuesCannotBeZeros = 2

class swsGravityError_e(IntEnum):
    """swsGravityError_e (6 constants, from CosmosWorksLib)."""
    swsGravityErrorSuccessful = 0
    swsGravityErrorSelectFaceEdgeOrPlane = 1
    swsGravityErrorFaceNotPlanar = 2
    swsGravityErrorEdgeNotStraight = 3
    swsGravityErrorGravityAlreadyDefined = 4
    swsGravityErrorInvalidStudy = 5

class swsHeatFluxEndEditError_e(IntEnum):
    """swsHeatFluxEndEditError_e (9 constants, from CosmosWorksLib)."""
    swsHeatFluxEndEditErrorSuccessful = 0
    swsHeatFluxEndEditErrorNoEntityAtIndex = 1
    swsHeatFluxEndEditErrorEntityAlreadyExists = 2
    swsHeatFluxEndEditErrorNoEntities = 3
    swsHeatFluxEndEditErrorSelectFace = 4
    swsHeatFluxEndEditErrorSelectFacesOrShellEdge = 5
    swsHeatFluxEndEditErrorSelectrVertexForSensorLocation = 6
    swsHeatFluxEndEditErrorLowerboundTemperatureHigherThanUpperbound = 7
    swsHeatFluxEndEditErrorThermostatForTransientStudiesOnly = 8

class swsHeatFluxError_e(IntEnum):
    """swsHeatFluxError_e (6 constants, from CosmosWorksLib)."""
    swsHeatFluxErrorSuccessful = 0
    swsHeatFluxErrorNoFaces = 1
    swsHeatFluxErrorNoFacesOrShellEdges = 2
    swsHeatFluxErrorInvalidStudy = 3
    swsHeatFluxErrorInvalidArray = 4
    swsHeatFluxErrorNoEntities = 5

class swsHeatPowerEndEditError_e(IntEnum):
    """swsHeatPowerEndEditError_e (10 constants, from CosmosWorksLib)."""
    swsHeatPowerEndEditErrorSuccessful = 0
    swsHeatPowerEndEditErrorNoEntityAtIndex = 1
    swsHeatPowerEndEditErrorEntityAlreadyExists = 2
    swsHeatPowerEndEditErrorNoEntitiesSelected = 3
    swsHeatPowerEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies = 4
    swsHeatPowerEndEditErrorSelectFaceEdgeOrVertex = 5
    swsHeatPowerEndEditErrorSelectVertexForThermostatLocation = 6
    swsHeatPowerEndEditErrorLowerboundTemperatureHigherThanUpperbound = 7
    swsHeatPowerEndEditErrorNotValidForSteadyStateAnalysis = 8
    swsHeatPowerEndEditErrorVertexCannotBeUsedForSensorLocation = 9

class swsHeatPowerError_e(IntEnum):
    """swsHeatPowerError_e (6 constants, from CosmosWorksLib)."""
    swsHeatPowerErrorSuccessful = 0
    swsHeatPowerErrorSelectFaceEdgeVertexComponentOrBody = 1
    swsHeatPowerErrorSelectFacesEdgesOrVertices = 2
    swsHeatPowerErrorInvalidStudy = 3
    swsHeatPowerErrorInvalidArray = 4
    swsHeatPowerErrorNoEntities = 5

class swsImportStudyFeaturesErrorCode_e(IntEnum):
    """swsImportStudyFeaturesErrorCode_e (8 constants, from CosmosWorksLib)."""
    swsImportStudyFeaturesError_NoError = 0
    swsImportStudyFeaturesError_ComponentNotFound = 1
    swsImportStudyFeaturesError_StudyToImportNotFoundOrInvalid = 2
    swsImportStudyFeaturesError_ConfigurationMismatch = 3
    swsImportStudyFeaturesError_Unknown = 4
    swsImportStudyFeaturesError_NotAssembly = 5
    swsImportStudyFeaturesError_StudyNotActive = 6
    swsImportStudyFeaturesError_NoPrePlotView = 7

class swsImportStudyFeaturesFilterType_e(IntEnum):
    """swsImportStudyFeaturesFilterType_e (6 constants, from CosmosWorksLib)."""
    swsImportStudyFeaturesFilterType_All = 0
    swsImportStudyFeaturesFilterType_AllBodyTypesMaterials = 1
    swsImportStudyFeaturesFilterType_AllConnectorsContacts = 2
    swsImportStudyFeaturesFilterType_AllFixtures = 4
    swsImportStudyFeaturesFilterType_AllExternalLoads = 8
    swsImportStudyFeaturesFilterType_AllMeshControls = 16

class swsIncompatibleBondingOption_e(IntEnum):
    """swsIncompatibleBondingOption_e (3 constants, from CosmosWorksLib)."""
    swsIncompatibleBondingOption_Automatic = 0
    swsIncompatibleBondingOption_Simplified = 1
    swsIncompatibleBondingOption_MoreAccurate = 2

class swsInterpolationType_e(IntEnum):
    """swsInterpolationType_e (2 constants, from CosmosWorksLib)."""
    swsInterpolationType_Logarithmic = 0
    swsInterpolationType_Linear = 1

class swsIsoClippingErrorCode_e(IntEnum):
    """swsIsoClippingErrorCode_e (9 constants, from CosmosWorksLib)."""
    swsIsoClippingNoError = 0
    swsIsoClippingCosworksViewNotPresent = 1
    swsIsoClippingIsoPlanesError = 2
    swsIsoClippingPlotNotFound = 3
    swsIsoClippingPostDataNotExist = 4
    swsIsoClippingIsoValueError = 5
    swsIsoClippingIsoVariantValueError = 6
    swsIsoClippingIsoInvalidVariantError = 7
    swsIsoClippingNotAvailable = 8

class swsJointType_e(IntEnum):
    """swsJointType_e (3 constants, from CosmosWorksLib)."""
    swsRigid = 0
    swsPivot = 1
    swsSpherical = 2

class swsLinearUnit_e(IntEnum):
    """swsLinearUnit_e (11 constants, from CosmosWorksLib)."""
    swsLinearUnitMillimeters = 0
    swsLinearUnitCentimeters = 1
    swsLinearUnitMeters = 2
    swsLinearUnitInches = 3
    swsLinearUnitFeet = 4
    swsLinearUnitFeetInches = 5
    swsLinearUnitAngstrom = 6
    swsLinearUnitNanoMeter = 7
    swsLinearUnitMicron = 8
    swsLinearUnitMil = 9
    swsLinearUnitMicronIn = 10

class swsLinkConnectorEndEditError_e(IntEnum):
    """swsLinkConnectorEndEditError_e (8 constants, from CosmosWorksLib)."""
    swsLinkConnectorEndEditErrorSuccessful = 0
    swsLinkConnectorEndEditErrorEntityAlreadyExists = 1
    swsLinkConnectorEndEditErrorSelectDatumPointOrVertices = 2
    swsLinkConnectorEndEditErrorSelectEntity = 3
    swsLinkConnectorEndEditErrorNullEntity = 4
    swsLinkConnectorEndEditErrorHasBeamBody = 5
    swsLinkConnectorEndEditErrorHasMassElement = 6
    swsLinkConnectorEndEditErrorBodyExcludedFromAnalysis = 7

class swsLinkConnectorError_e(IntEnum):
    """swsLinkConnectorError_e (9 constants, from CosmosWorksLib)."""
    swsLinkConnectorErrorSuccessful = 0
    swsLinkConnectorErrorInvalidMesh = 1
    swsLinkConnectorErrorNonlinearStudyPartDocument = 2
    swsLinkConnectorErrorInvalidStudy = 3
    swsLinkConnectorErrorSelectAssemblyDocument = 4
    swsLinkConnectorErrorEmptyEntity = 5
    swsLinkConnectorErrorSelectVertexOrDatumPoint = 6
    swsLinkConnectorErrorHasRemoteMassOrBeamBody = 7
    swsLinkConnectorErrorBodyExcludedFromAnalysis = 8

class swsLinkageRodEndEditErrors_e(IntEnum):
    """swsLinkageRodEndEditErrors_e (25 constants, from CosmosWorksLib)."""
    swsLinkageRodErrCode_Successful = 0
    swsLinkageRodErrCode_NoActiveDoc = 1
    swsLinkageRodErrCode_NoActiveStudy = 2
    swsLinkageRodErrCode_SetOperationNotSupported = 3
    swsLinkageRodErrCode_InvalidSelection = 4
    swsLinkageRodErrCode_InvalidNonCoAxialSelection = 5
    swsLinkageRodErrCode_InvalidCoAxialSelection = 6
    swsLinkageRodErrCode_InvalidNonConcentricSelection = 7
    swsLinkageRodErrCode_InvalidJointTypeSel = 8
    swsLinkageRodErrCode_OffsetOptionNotAvailable = 9
    swsLinkageRodErrCode_InvalidRodSectionType = 10
    swsLinkageRodErrCode_InvalidArray = 11
    swsLinkageRodErrCode_InvalidParamsCount = 12
    swsLinkageRodErrCode_InvalidParamDataType = 13
    swsLinkageRodErrCode_ZeroParamValue = 14
    swsLinkageRodErrCode_InvalidUnitType = 15
    swsLinkageRodErrCode_InvalidMaterialSourceType = 16
    swsLinkageRodErrCode_SetMaterialPropertyNA = 17
    swsLinkageRodErrCode_SetLibraryMaterialNA = 18
    swsLinkageRodErrCode_InvalidLibraryMaterialDetails = 19
    swsLinkageRodErrCode_OutOfRangeYoungsModulus = 20
    swsLinkageRodErrCode_OutOfRangePoissonRatio = 21
    swsLinkageRodErrCode_OutOfRangeThermalCoefficient = 22
    swsLinkageRodErrCode_InvalidMass = 23
    swsLinkageRodErrCode_InadequateEntitiesSelection = 24

class swsLoadCaseManagerError_e(IntEnum):
    """swsLoadCaseManagerError_e (14 constants, from CosmosWorksLib)."""
    swsLoadCaseManager_NoError = 0
    swsLoadCaseManager_LoadCaseManagerNotShown = 1
    swsLoadCaseManager_InvalidLoadName = 2
    swsLoadCaseManager_InvalidLoadCaseName = 3
    swsLoadCaseManager_InvalidCombinationName = 4
    swsLoadCaseManager_LoadIsSuppressed = 5
    swsLoadCaseManager_LoadCaseIsSuppressed = 6
    swsLoadCaseManager_CombinationIsSuppressed = 7
    swsLoadCaseManager_InvalidDataInput = 8
    swsLoadCaseManager_InvalidEquation = 9
    swsLoadCaseManager_NoLoadCasesToRun = 10
    swsLoadCaseManager_CannotRunStudy = 11
    swsLoadCaseManager_CannotCreateMesh = 12
    swsLoadCaseManager_UnknownError = 13

class swsLoadsAndRestraintsError_e(IntEnum):
    """swsLoadsAndRestraintsError_e (9 constants, from CosmosWorksLib)."""
    swsLoadsAndRestraintsErrorSuccessful = 0
    swsLoadsAndRestraintsErrorNotFoundAtIndex = 1
    swsLoadsAndRestraintsError_NotFoundWithGivenName = 2
    swsLoadsAndRestraintsError_InvalidComponentsCount = 3
    swsLoadsAndRestraintsError_InvalidSelection = 4
    swsLoadsAndRestraintsError_InvalidSelectionsMixedTogether = 5
    swsLoadsAndRestraintsError_InvalidOrNullFace = 6
    swsLoadsAndRestraintsError_InvalidLicense = 7
    swsLoadsAndRestraintsError_NoLBCDefined = 8

class swsLoadsAndRestraintsManagerBearingLoadError_e(IntEnum):
    """swsLoadsAndRestraintsManagerBearingLoadError_e (10 constants, from CosmosWorksLib)."""
    swsLoadsAndRestraintsManagerBearingLoadErrorSuccessful = 0
    swsLoadsAndRestraintsManagerBearingLoadErrorInvalidArray = 1
    swsLoadsAndRestraintsManagerBearingLoadErrorNoObjectForFace = 2
    swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemEmpty = 3
    swsLoadsAndRestraintsManagerBearingLoadErrorSelectFace = 4
    swsLoadsAndRestraintsManagerBearingLoadErrorSelectCoordinateSystem = 5
    swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemAndCylindricalFaces = 6
    swsLoadsAndRestraintsManagerBearingLoadErrorInvalidMesh = 7
    swsLoadsAndRestraintsManagerBearingLoadErrorInvalidStudy = 8
    swsLoadsAndRestraintsManagerBearingLoadErrorBodyExcludedFromAnalysis = 9

class swsLoadsAndRestraintsType_e(IntEnum):
    """swsLoadsAndRestraintsType_e (17 constants, from CosmosWorksLib)."""
    swsLoadsAndRestraintsTypePressure = 1
    swsLoadsAndRestraintsTypeRestraint = 2
    swsLoadsAndRestraintsTypeForce = 3
    swsLoadsAndRestraintsTypeGravity = 4
    swsLoadsAndRestraintsTypeCentrifugal = 5
    swsLoadsAndRestraintsTypeTemperature = 6
    swsLoadsAndRestraintsTypeConvection = 7
    swsLoadsAndRestraintsTypeHeatPower = 8
    swsLoadsAndRestraintsTypeHeatFlux = 9
    swsLoadsAndRestraintsTypeRadiation = 10
    swsLoadsAndRestraintsTypeRemoteLoad = 11
    swsLoadsAndRestraintsTypeConnectors = 12
    swsLoadsAndRestraintsTypeBearingLoads = 13
    swsLoadsAndRestraintsTypeVelocity = 14
    swsLoadsAndRestraintsTypeBaseExcitation = 15
    swsLoadsAndRestraintsTypeMeshControl = 21
    swsLoadsAndRestraintsTypeRemoteMass = 31

class swsMassUnits_e(IntEnum):
    """swsMassUnits_e (4 constants, from CosmosWorksLib)."""
    swsMassUnit_Milligram = 0
    swsMassUnit_Gram = 1
    swsMassUnit_Kilogram = 2
    swsMassUnit_Pound = 3

class swsMaterialDataCurveError_e(IntEnum):
    """swsMaterialDataCurveError_e (8 constants, from CosmosWorksLib)."""
    swsMaterialDataCurveErrorSuccessful = 0
    swsMaterialDataCurveErrorCannotBeDefined = 1
    swsMaterialDataCurveErrorIndexValues = 2
    swsMaterialDataCurveErrorIndexForMooneyRivlinAndOgeden = 3
    swsMaterialDataCurveErrorIndexForViscoElastic = 4
    swsMaterialDataCurveErrorInvalidArray = 5
    swsMaterialDataCurveErrorTemperatures = 6
    swsMaterialDataCurveErrorNeedDataPoints = 7

class swsMaterialErrorWarning_e(IntEnum):
    """swsMaterialErrorWarning_e (28 constants, from CosmosWorksLib)."""
    swsMaterialErrorWarningSuccessful = 0
    swsMaterialErrorWarningInvalidLinearElasticAnisotropicMaterialModel = 1
    swsMaterialErrorWarningInvalidMaterialModel = 2
    swsMaterialErrorWarningFatigueSNCurvesCycles = 3
    swsMaterialErrorWarningUniqueStressRatioForEachSNCurve = 4
    swsMaterialErrorWarningTooManyPointsSNCurve = 5
    swsMaterialErrorWarningDefineProperty = 6
    swsMaterialErrorWarningMaterialPropertyValue = 7
    swsMaterialErrorWarningEXNotDefined = 8
    swsMaterialErrorWarningEXValue = 9
    swsMaterialErrorWarningDefineCurveForEx = 10
    swsMaterialErrorWarningMaterialTemperatureCurveForNitinol = 11
    swsMaterialErrorWarningNUXYValue = 12
    swsMaterialErrorWarningDensityNotDefined = 13
    swsMaterialErrorWarningrKXNotDefined = 14
    swsMaterialErrorWarningDefineStressStrainCurve = 15
    swsMaterialErrorWarningDefinePointForStressStrainCurve = 16
    swsMaterialErrorWarningSIGT_S1_F1_S2_F2Values = 17
    swsMaterialErrorWarningSIGT_S1LessThanSIGT_F1 = 18
    swsMaterialErrorWarningSIGT_S2LessThanSIGT_F1 = 19
    swsMaterialErrorWarningSIGT_F2LessThanSIGT_S2 = 20
    swsMaterialErrorWarningSIGC_S1LessThanSIGC_F1 = 21
    swsMaterialErrorWarningSIGC_S2LessThanSIGC_F1 = 22
    swsMaterialErrorWarningSIGC_F2LessThanSIGC_S2 = 23
    swsMaterialErrorWarningCreepWithForceControl = 24
    swsMaterialErrorWarningMaterialTemperatureDependencyIgnored = 30
    swsMaterialErrorWarningOnlyBilinearPlasticityForDropTestStudies = 31
    swsMaterialErrorWarningNUXYNotDefined = 32

class swsMaterialFatigueSNCurveError_e(IntEnum):
    """swsMaterialFatigueSNCurveError_e (6 constants, from CosmosWorksLib)."""
    swsMaterialFatigueSNCurveErrorSuccessful = 0
    swsMaterialFatigueSNCurveErrorIndexValues = 1
    swsMaterialFatigueSNCurveErrorInvalidArray = 2
    swsMaterialFatigueSNCurveErrorCycles = 3
    swsMaterialFatigueSNCurveErrorCurveDataPoints = 4
    swsMaterialFatigueSNCurveErrorStressValuesMustBeUnique = 5

class swsMaterialModelType_e(IntEnum):
    """swsMaterialModelType_e (13 constants, from CosmosWorksLib)."""
    swsMaterialModelTypeLinearElasticIsotropic = 0
    swsMaterialModelTypeLinearElasticOrthtropic = 1
    swsMaterialModelTypeLinearElasticAnisotropic = 2
    swsMaterialModelTypeNonlinearElastic = 3
    swsMaterialModelTypeElastoPlasticvonMisesKinematic = 4
    swsMaterialModelTypeElastoPlasticTrescaKinematic = 5
    swsMaterialModelTypeElastoPlasticDruckerPrager = 6
    swsMaterialModelTypeHyperElasticMooneyRivlin = 7
    swsMaterialModelTypeHyperElasticOgden = 8
    swsMaterialModelTypeHyperElasticBlatzko = 9
    swsMaterialModelTypeViscoElastic = 10
    swsMaterialModelTypeNitinol = 11
    swsMaterialModelTypeCreepExponential = 12

class swsMaterialReferencePlaneError_e(IntEnum):
    """swsMaterialReferencePlaneError_e (2 constants, from CosmosWorksLib)."""
    swsMaterialReferencePlaneErrorSuccessful = 0
    swsMaterialReferencePlaneErrorSpecifyPlaneOrAxis = 1

class swsMaterialSNCurveSource_e(IntEnum):
    """swsMaterialSNCurveSource_e (4 constants, from CosmosWorksLib)."""
    swsMaterialSNCurveSourceUserDefined = 0
    swsMaterialSNCurveSourceASMEAustenticSteel = 1
    swsMaterialSNCurveSourceASMECarbonSteel = 2
    swsMaterialSNCurveSourceEquation = 3

class swsMaterialSourceType_e(IntEnum):
    """swsMaterialSourceType_e (2 constants, from CosmosWorksLib)."""
    swsMaterial_Custom = 0
    swsMaterial_Library = 1

class swsMaterialSource_e(IntEnum):
    """swsMaterialSource_e (4 constants, from CosmosWorksLib)."""
    swsMaterialSourceSolidWorks = 0
    swsMaterialSourceCustomDefined = 1
    swsMaterialSourceCentorLibrary = 2
    swsMaterialSourceLibraryFiles = 3

class swsMaterialStressStrainCurveError_e(IntEnum):
    """swsMaterialStressStrainCurveError_e (5 constants, from CosmosWorksLib)."""
    swsMaterialStressStrainCurveErrorSuccessful = 0
    swsMaterialStressStrainCurveErrorInvalidForMaterial = 1
    swsMaterialStressStrainCurveErrorInvalidArray = 2
    swsMaterialStressStrainCurveErrorTemperatures = 3
    swsMaterialStressStrainCurveErrorNeedDataPoints = 4

class swsMaterialTemperatureCurveForPropertyError_e(IntEnum):
    """swsMaterialTemperatureCurveForPropertyError_e (7 constants, from CosmosWorksLib)."""
    swsMaterialTemperatureCurveForPropertyErrorSuccessful = 0
    swsMaterialTemperatureCurveForPropertyErrorPropertyNotDefined = 1
    swsMaterialTemperatureCurveForPropertyErrorNotApplicable = 2
    swsMaterialTemperatureCurveForPropertyErrorNotAllowed = 3
    swsMaterialTemperatureCurveForPropertyErrorInvalidArray = 4
    swsMaterialTemperatureCurveForPropertyErrorNeedDataPoints = 5
    swsMaterialTemperatureCurveForPropertyErrorTermperatures = 6

class swsMaterialTemperature_e(IntEnum):
    """swsMaterialTemperature_e (2 constants, from CosmosWorksLib)."""
    swsMaterialTemperatureDependent = 0
    swsMaterialTemperatureNotDependent = 1

class swsMeshCompatibility_e(IntEnum):
    """swsMeshCompatibility_e (2 constants, from CosmosWorksLib)."""
    swsMeshCompatibilityCompatible = 0
    swsMeshCompatibiltyIncompatible = 1

class swsMeshControlError_e(IntEnum):
    """swsMeshControlError_e (8 constants, from CosmosWorksLib)."""
    swsMeshControlErrorSuccessful = 0
    swsMeshControlErrorNoEntityAtIndex = 1
    swsMeshControlErrorEntityAlreadyExists = 2
    swsMeshControlErrorNoEntities = 3
    swsMeshControlErrorSelectVerticesEdgesFacesBodiesOrComponents = 4
    swsMeshControlErrorSelectFaceEdgeOrVertex = 5
    swsMeshControlErrorElementSize = 6
    swsMeshControlErrorNumberOfLayers = 7

class swsMeshControlMeshingError_e(IntEnum):
    """swsMeshControlMeshingError_e (4 constants, from CosmosWorksLib)."""
    swsMeshControlMeshingErrorSuccessful = 0
    swsMeshControlMeshingErrorInvalidMeshControlName = 1
    swsMeshControlMeshingErrorMeshControlNotFound = 2
    swsMeshControlMeshingErrorMeshControlUnsuccessful = 3

class swsMeshControlWeightFactor_e(IntEnum):
    """swsMeshControlWeightFactor_e (2 constants, from CosmosWorksLib)."""
    swsMeshControlWeightFactorDefault = 0
    swsMeshControlWeightFactorHighest = 1

class swsMeshCopyErrorCode_e(IntEnum):
    """swsMeshCopyErrorCode_e (6 constants, from CosmosWorksLib)."""
    swsMeshCopy_NoError = 0
    swsMeshCopy_StudyNotActive = 1
    swsMeshCopy_InvalidStudyName = 2
    swsMeshCopy_NotSupportedForBeamMesh = 3
    swsMeshCopy_MeshTypeDifferentForBothStudies = 4
    swsMeshCopy_UnSupportedStudies = 5

class swsMeshElementNodeLocation_e(IntEnum):
    """swsMeshElementNodeLocation_e (3 constants, from CosmosWorksLib)."""
    swsMeshElementNodeLocationSuccessful = 0
    swsMeshElementNodeLocationNoNode = 1
    swsMeshElementNodeLocationNoElement = 2

class swsMeshElementQualityKPI_e(IntEnum):
    """swsMeshElementQualityKPI_e (5 constants, from CosmosWorksLib)."""
    swsMeshElementQualityKPI_JacobianRatio = 0
    swsMeshElementQualityKPI_AspectRatio = 1
    swsMeshElementQualityKPI_Volume = 2
    swsMeshElementQualityKPI_Area = 3
    swsMeshElementQualityKPI_ElemSkewRatio = 4

class swsMeshFlipShellError_e(IntEnum):
    """swsMeshFlipShellError_e (6 constants, from CosmosWorksLib)."""
    swsMeshFlipShellErrorSuccessful = 0
    swsMeshFlipShellErrorInvalidArray = 1
    swsMeshFlipShellErrorEmptyArray = 2
    swsMeshFlipShellErrorNotShell = 3
    swsMeshFlipShellErrorSelectFaces = 4
    swsMeshFlipShellErrorMeshInformationNotFound = 5

class swsMeshKPIErrCode_e(IntEnum):
    """swsMeshKPIErrCode_e (6 constants, from CosmosWorksLib)."""
    swsMeshKPIErrCode_Success = 0
    swsMeshKPIErrCode_KPINotSupported = 1
    swsMeshKPIErrCode_ImproperInput = 2
    swsMeshKPIErrCode_InvalidMeshData = 3
    swsMeshKPIErrCode_ImproperGaussOrder = 4
    swsMeshKPIErrCode_InternalError = 5

class swsMeshQuality_e(IntEnum):
    """swsMeshQuality_e (2 constants, from CosmosWorksLib)."""
    swsMeshQualityDraft = 0
    swsMeshQualityHigh = 1

class swsMeshQueryErrorCode_e(IntEnum):
    """swsMeshQueryErrorCode_e (5 constants, from CosmosWorksLib)."""
    swsMeshQuery_NoError = 0
    swsMeshQuery_DataBaseNotAvailable = 1
    swsMeshQuery_NoElements = 2
    swsMeshQuery_NoNodes = 3
    swsMeshQuery_Failed = 10

class swsMeshShellNormal_e(IntEnum):
    """swsMeshShellNormal_e (3 constants, from CosmosWorksLib)."""
    swsMeshShellNormalNotFoundOrFaceNotSelected = -1
    swsMeshShellNormalTopFace = 0
    swsMeshShellNormalBottomFace = 1

class swsMeshState_e(IntEnum):
    """swsMeshState_e (5 constants, from CosmosWorksLib)."""
    swsMeshStateNoMesh = 0
    swsMeshStateExistsAndCurrent = 1
    swsMeshStateExistsAndNotCurrent = 2
    swsMeshStateFailed = 3
    swsMeshStateInterrupted = 4

class swsMeshType_e(IntEnum):
    """swsMeshType_e (5 constants, from CosmosWorksLib)."""
    swsMeshTypeSolid = 0
    swsMeshTypeMidSurface = 1
    swsMeshTypeSurfaces = 2
    swsMeshTypeMixed = 3
    swsMeshTypeBeam = 4

class swsMesherTypeNew_e(IntEnum):
    """swsMesherTypeNew_e (3 constants, from CosmosWorksLib)."""
    swsMesherType_Standard = 0
    swsMesherType_CB = 1
    swsMesherType_BCB = 2

class swsMesherType_e(IntEnum):
    """swsMesherType_e (3 constants, from CosmosWorksLib)."""
    swsMesherTypeStandard = 0
    swsMesherTypeAlternate = 1
    swsMesherTypeAlternateCB = 2

class swsModeCombinationMethod_e(IntEnum):
    """swsModeCombinationMethod_e (4 constants, from CosmosWorksLib)."""
    swsModeCombinationMethod_SRSS = 0
    swsModeCombinationMethod_AbsSum = 1
    swsModeCombinationMethod_CQC = 2
    swsModeCombinationMethod_NRL = 3

class swsMomentUnit_e(IntEnum):
    """swsMomentUnit_e (3 constants, from CosmosWorksLib)."""
    swsMomentUnit_NewtonMeter = 0
    swsMomentUnit_PoundForceInch = 1
    swsMomentUnit_KilogramForceCentimeter = 2

class swsMultipleContactsEditErrorCode_e(IntEnum):
    """swsMultipleContactsEditErrorCode_e (13 constants, from CosmosWorksLib)."""
    swsMultipleContactsEditErrorCode_Success = 0
    swsMultipleContactsEditErrorCode_NoTypeSelectedForMixedContactTypesSelection = 1
    swsMultipleContactsEditErrorCode_NoDefaultContactIsSelected = 2
    swsMultipleContactsEditErrorCode_GivenContactIsNotAddedYet = 3
    swsMultipleContactsEditErrorCode_NoSuchContactExists = 4
    swsMultipleContactsEditErrorCode_MultipleContactSetMgrIsNull = 5
    swsMultipleContactsEditErrorCode_InvalidPropertiesAreApplied = 6
    swsMultipleContactsEditErrorCode_GivenContactSetDidNotMeetMinCriteria = 7
    swsMultipleContactsEditErrorCode_GivenContactIsAlreadyAdded = 8
    swsMultipleContactsEditErrorCode_OperationNotSupported = 9
    swsMultipleContactsEditErrorCode_NoPenetrationSelfContactSetsCannotBeEditedWithOtherContactTypes = 10
    swsMultipleContactsEditErrorCode_VirtualWallContactSetsCannotBeEditedWithOtherContactTypes = 11
    swsMultipleContactsEditErrorCode_BondedContactsWithBeamsCannotBeEditedWithOtherNonBeamContactTypes = 12

class swsNForceType_e(IntEnum):
    """swsNForceType_e (3 constants, from CosmosWorksLib)."""
    swsNForceTypeNormal = 0
    swsNForceTypeFriction = 1
    swsNForceTypeTotal = 2

class swsNameViewOrientation_e(IntEnum):
    """swsNameViewOrientation_e (11 constants, from CosmosWorksLib)."""
    swsNameViewOrientation_NormalTo = 0
    swsNameViewOrientation_Front = 1
    swsNameViewOrientation_Back = 2
    swsNameViewOrientation_Left = 3
    swsNameViewOrientation_Right = 4
    swsNameViewOrientation_Top = 5
    swsNameViewOrientation_Bottom = 6
    swsNameViewOrientation_Isometric = 7
    swsNameViewOrientation_Trimetric = 8
    swsNameViewOrientation_Dimetric = 9
    swsNameViewOrientation_AssociateWithCurrView = 10

class swsNastranExportOption_e(IntEnum):
    """swsNastranExportOption_e (4 constants, from CosmosWorksLib)."""
    swsNastranExportOption_ShortFree = 0
    swsNastranExportOption_LongFree = 1
    swsNastranExportOption_ShortFixed = 2
    swsNastranExportOption_LongFixed = 3

class swsNastranExportUnit_e(IntEnum):
    """swsNastranExportUnit_e (3 constants, from CosmosWorksLib)."""
    swsNastranExportUnit_SI = 0
    swsNastranExportUnit_IPS = 1
    swsNastranExportUnit_MKS = 2

class swsNoPenetrationOption_e(IntEnum):
    """swsNoPenetrationOption_e (3 constants, from CosmosWorksLib)."""
    swsNoPenetrationOptionNodeToNode = 0
    swsNoPenetrationOptionNodeToSurface = 1
    swsNoPenetrationOptionSurfaceToSurface = 2

class swsNodalResultsOfElementError_e(IntEnum):
    """swsNodalResultsOfElementError_e (10 constants, from CosmosWorksLib)."""
    swsNodalResultsOfElementError_NoError = 0
    swsNodalResultsOfElementError_InvalidStudy = 1
    swsNodalResultsOfElementError_InvalidResultType = 2
    swsNodalResultsOfElementError_InvalidComponent = 3
    swsNodalResultsOfElementError_InvalidStep = 4
    swsNodalResultsOfElementError_InvalidUnits = 5
    swsNodalResultsOfElementError_InvalidShellFace = 6
    swsNodalResultsOfElementError_InvalidElements = 7
    swsNodalResultsOfElementError_InvalidElementGroup = 8
    swsNodalResultsOfElementError_ResultsNotAvailable = 9

class swsNonLinearOptionControlMethodType_e(IntEnum):
    """swsNonLinearOptionControlMethodType_e (3 constants, from CosmosWorksLib)."""
    swsNonLinearControl_Force = 0
    swsNonLinearControl_Displacement = 1
    swsNonLinearControl_ArcLength = 2

class swsNonLinearOptionIntegrationMethodType_e(IntEnum):
    """swsNonLinearOptionIntegrationMethodType_e (3 constants, from CosmosWorksLib)."""
    swsNonLinearIntegration_Newmark = 0
    swsNonLinearIntegration_WilsonTheta = 1
    swsNonLinearIntegration_CentralDifference = 2

class swsNonLinearOptionIterativeMethodType_e(IntEnum):
    """swsNonLinearOptionIterativeMethodType_e (2 constants, from CosmosWorksLib)."""
    swsNonLinearIterative_ModifiedNewtonRaphson = 0
    swsNonLinearIterative_NewtonRaphson = 1

class swsNonLinearStudyOptionsError_e(IntEnum):
    """swsNonLinearStudyOptionsError_e (21 constants, from CosmosWorksLib)."""
    swsNonLinearStudyOptionsErrorSuccessful = 0
    swsNonLinearStudyOptionsErrorStartEndStepsAndIncrement = 1
    swsNonLinearStudyOptionsErrorAutoSteppingParameters = 2
    swsNonLinearStudyOptionsErrorStartTimeLessThanEndTime = 3
    swsNonLinearStudyOptionsErrorSolutionSteps = 4
    swsNonLinearStudyOptionsErrorSelectVerticesOrDatumPoint = 5
    swsNonLinearStudyOptionsErrorSelectDisplacementControlType = 6
    swsNonLinearStudyOptionsErrorSelectArcLengthControlType = 7
    swsNonLinearStudyOptionsErrorSelectTimeCurve = 8
    swsNonLinearStudyOptionsErrorSelectDirectSolver = 9
    swsNonLinearStudyOptionsErrorSelectForceControl = 10
    swsNonLinearStudyOptionsErrorWrongArcLengthUnit = 11
    swsNonLinearStudyOptionsErrorEmptyDispatch = 12
    swsNonLinearStudyTimeCurveErrorInvalidStudyType = 13
    swsNonLinearStudyInvalidDisplaceComponentValue = 14
    swsNonLinearStudyInvalidDisplaceComponentUnitValue = 15
    swsNonLinearStudyInvalidArcLengthMultiplierValue = 16
    swsNonLinearStudyInvalidArcLengthMaximumDisplacementValue = 17
    swsNonLinearStudyInvalidArcLengthMaximumLoadValue = 18
    swsNonLinearStudyInvalidArcLengthStepsValue = 19
    swsNonLinearStudyInvalidSingularityEliminationfactorValue = 20

class swsNonlinearAnalysisSubType_e(IntEnum):
    """swsNonlinearAnalysisSubType_e (2 constants, from CosmosWorksLib)."""
    swsNonlinearAnalysisSubTypeStatic = 0
    swsNonlinearAnalysisSubTypeDynamic = 1

class swsNonlinearStudyResultTypes_e(IntEnum):
    """swsNonlinearStudyResultTypes_e (5 constants, from CosmosWorksLib)."""
    swsNonlinearResultNodalStress = 0
    swsNonlinearResultElementalStress = 1
    swsNonlinearResultDisplacement = 2
    swsNonlinearResultNodalStrain = 3
    swsNonlinearResultElementalStrain = 4

class swsOptimizationStudyResultType_e(IntEnum):
    """swsOptimizationStudyResultType_e (2 constants, from CosmosWorksLib)."""
    swsOptimizationStudyResult_InitialAndFinalIterations = 0
    swsOptimizationStudyResult_AllIterations = 1

class swsPVResultCombinationError_e(IntEnum):
    """swsPVResultCombinationError_e (17 constants, from CosmosWorksLib)."""
    swsPVResultCombinationError_NoError = 0
    swsPVResultCombinationError_NotAvailable = 1
    swsPVResultCombinationError_AtleastTwoItemsNeeded = 2
    swsPVResultCombinationError_StudyNamesNotProper = 3
    swsPVResultCombinationError_ItemsNotSameInNumber = 4
    swsPVResultCombinationError_InvalidFactors = 5
    swsPVResultCombinationError_InvalidStudy = 6
    swsPVResultCombinationError_CombineAnalysisNotDone = 7
    swsPVResultCombinationError_CombineIncompatibleResults = 8
    swsPVResultCombinationError_CombineIncompatibleMesh = 9
    swsPVResultCombinationError_CombineIncompatibleConfiguration = 10
    swsPVResultCombinationError_CombineIncompatibleRestraints = 11
    swsPVResultCombinationError_CombineIncompatibleSolidsMaterials = 12
    swsPVResultCombinationError_CombineIncompatibleShellsMaterials = 13
    swsPVResultCombinationError_CombineIncompatibleContact = 14
    swsPVResultCombinationError_CombineIncompatibleConnectors = 15
    swsPVResultCombinationError_CombineIncompatiblePlanarType = 16

class swsPVResultCombinationType_e(IntEnum):
    """swsPVResultCombinationType_e (2 constants, from CosmosWorksLib)."""
    swsPVResultCombinationType_Linear = 0
    swsPVResultCombinationType_SRSS = 1

class swsPhaseAngleUnit_e(IntEnum):
    """swsPhaseAngleUnit_e (2 constants, from CosmosWorksLib)."""
    swsPhaseAngleUnit_Deg = 0
    swsPhaseAngleUnit_Rad = 1

class swsPinConnectorEndEditError_e(IntEnum):
    """swsPinConnectorEndEditError_e (28 constants, from CosmosWorksLib)."""
    swsPinConnectorEndEditErrorSuccessful = 0
    swsPinConnectorEndEditErrorNoEntityAtIndex = 1
    swsPinConnectorEndEditErrorEntityAlreadyAdded = 2
    swsPinConnectorEndEditErrorSelectEntity = 3
    swsPinConnectorEndEditErrorSelectFace = 4
    swsPinConnectorEndEditErrorSelectFaceCylindricalSurface = 5
    swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnector = 6
    swsPinConnectorEndEditErrorRadiiNotEqual = 7
    swsPinConnectorEndEditErrorSelectAssemblyDocument = 8
    swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnection = 9
    swsPinConnectorEndEditErrorIndexTooBig = 10
    swsPinConnectorEndEditErrorHasBeamBody = 11
    swsPinConnectorEndEditErrorHasMassElement = 12
    swsPinConnectorEndEditErrorSelectCircularEdges = 13
    swsPinConnectorEndEditErrorSelectDifferentBody = 14
    swsPinConnectorEndEditErrorSelectFacesFromSameHole = 15
    swsPinConnectorEndEditErrorSpecifyPositiveValue = 16
    swsPinConnectorEndEditErrorPinMass = 17
    swsPinConnectorEndEditErrorTensileStressArea = 18
    swsPinConnectorEndEditErrorTesileStressAreaLarge = 19
    swsPinConnectorEndEditErrorPinBoltStrength = 20
    swsPinConnectorEndEditErrorSafetyFactor = 21
    swsPinConnectorEndEditErrorSelectCircularEdge = 22
    swsPinConnectorEndEditErrorBodyExcludedFromAnalysis = 23
    swsPinConnectorEndEditErrorNullEntity = 24
    swsPinConnectorEndEditErrorIncludeStrengthData = 25
    swsPinConnectorEndEditErrorInvalidForAnalysis = 26
    swsPinConnectorEndEditErrorInvalidConnectionType = 27

class swsPinConnectorError_e(IntEnum):
    """swsPinConnectorError_e (21 constants, from CosmosWorksLib)."""
    swsPinConnectorErrorSuccesful = 0
    swsPinConnectorErrorInvalidMesh = 1
    swsPinConnectorErrorNonlinearStudyPartDocument = 2
    swsPinConnectorErrorInvalidStudy = 3
    swsPinConnectorErrorNoObject = 4
    swsPinConnectorErrorSelectFace = 5
    swsPinConnectorErrorFaceNotCylindrical = 6
    swsPinConnectorErrorSelectConcentricCylindricalFacesForConnector = 7
    swsPinConnectorErrorComponentConcentricFacesRadiiNotEqual = 8
    swsPinConnectorErrorInvalidArray = 9
    swsPinConnectorErrorSelectAssemblyDocument = 10
    swsPinConnectorErrorSelectFacesFromSameHoleForSource = 11
    swsPinConnectorErrorSelectFaceFromSameHoleForTarget = 12
    swsPinConnectorErrorNullOrEmptyArray = 13
    swsPinConnectorErrorEntitySameForComponents = 14
    swsPinConnectorErrorSelectDifferentBody = 15
    swsPinConnectorErrorArrayEmtpy = 16
    swsPinConnectorErrorArrayHasBeamBody = 17
    swsPinConnectorErrorSelectConcentricCylindricalFacesForConnection = 18
    swsPinConnectorErrorSelectCircularEdgesOnShells = 19
    swsPinConnectorErrorBodyExcludedFromAnalysis = 20

class swsPinballUnit_e(IntEnum):
    """swsPinballUnit_e (11 constants, from CosmosWorksLib)."""
    swsPinballmm = 0
    swsPInballcm = 1
    swsPinballm = 2
    swsPinballin = 3
    swsPinballft = 4
    swsPinballftin = 5
    swsPinballam = 6
    swsPinaballnm = 7
    swsPinballmicron = 8
    swsPinballmil = 9
    swsPinballmicronIn = 10

class swsPlotBoundarySettingsOptionValue_e(IntEnum):
    """swsPlotBoundarySettingsOptionValue_e (5 constants, from CosmosWorksLib)."""
    swsPlotBoundaryNone = 0
    swsPlotBoundaryModel = 1
    swsPlotBoundaryMesh = 2
    swsPlotBoundaryTranslucentSingleColor = 3
    swsPlotBoundaryTranslucentPartColor = 4

class swsPlotDeformedShapeOptionScaleFactorContactValue_e(IntEnum):
    """swsPlotDeformedShapeOptionScaleFactorContactValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotDeformedShapeContactAutomatic = 0
    swsPlotDeformedShapeContactTrueValue = 1

class swsPlotDeformedShapeOptionScaleFactorLargeDispValue_e(IntEnum):
    """swsPlotDeformedShapeOptionScaleFactorLargeDispValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotDeformedShapeLargeDispAutomatic = 0
    swsPlotDeformedShapeLargeDispTrueValue = 1

class swsPlotDeformedShapeOptionScaleFactorOtherValue_e(IntEnum):
    """swsPlotDeformedShapeOptionScaleFactorOtherValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotDeformedShapeOtherAutomatic = 0
    swsPlotDeformedShapeOtherTrueValue = 1

class swsPlotDeformedShapeOptionSuperImposeValue_e(IntEnum):
    """swsPlotDeformedShapeOptionSuperImposeValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotDeformedShapeSuperImposeModel_TranslucentPartColor = 0
    swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor = 1

class swsPlotDeformedShapeOptionValue_e(IntEnum):
    """swsPlotDeformedShapeOptionValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotDeformedShapeShowResultsOnUnDeformedShape = 0
    swsPlotDeformedShapeShowResultsOnDeformedShape = 1

class swsPlotFringeSettingsOptionValue_e(IntEnum):
    """swsPlotFringeSettingsOptionValue_e (4 constants, from CosmosWorksLib)."""
    swsPlotFringePoint = 0
    swsPlotFringeLine = 1
    swsPlotFringeDiscrete = 2
    swsPlotFringeContinuous = 3

class swsPlotResultTypes_e(IntEnum):
    """swsPlotResultTypes_e (14 constants, from CosmosWorksLib)."""
    swsResultDisplacementOrAmplitude = 1
    swsResultStress = 2
    swsResultStrain = 3
    swsResultFactorOfSafety = 4
    swsResultThermal = 5
    swsResultFatigue = 12
    swsResultVelocity = 19
    swsResultAcceleration = 20
    swsResultDesignInsight = 22
    swsResultBeamDiagram = 54
    swsResultPinBoltBearing = 56
    swsResultEdgeWeldConnector = 58
    swsResultBeamStress = 59
    swsResultEquivalentStress = 67

class swsPlotSettingsErrorCode_e(IntEnum):
    """swsPlotSettingsErrorCode_e (12 constants, from CosmosWorksLib)."""
    swsPlotSettings_NoError = 0
    swsPlotSettings_InvalidPlotName = 1
    swsPlotSettings_InvalidNumberOfParameters = 2
    swsPlotSettings_InvalidParameters = 3
    swsPlotSettings_InvalidSelectionEntities = 4
    swsPlotSettings_UnableToFetchLegendData = 5
    swsPlotSettings_InvalidFringeOption = 6
    swsPlotSettings_WrongBoundaryOption = 7
    swsPlotSettings_FailToGetColors = 8
    swsPlotSettings_WrongRGBValues = 9
    swsPlotSettings_InvalidInput = 10
    swsPlotSettings_InvalidAlphaValue = 11

class swsPlotShowExcludedBodiesOptionValue_e(IntEnum):
    """swsPlotShowExcludedBodiesOptionValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotExcludedBodyTranslucentSingleColor = 0
    swsPlotExcludedBodyTranslucentPartColor = 1

class swsPlotShowHiddenBodiesOptionValue_e(IntEnum):
    """swsPlotShowHiddenBodiesOptionValue_e (2 constants, from CosmosWorksLib)."""
    swsPlotHiddenBodyTranslucentSingleColor = 0
    swsPlotHiddenBodyTranslucentPartColor = 1

class swsPreLoadForceType_e(IntEnum):
    """swsPreLoadForceType_e (2 constants, from CosmosWorksLib)."""
    swsPreLoadForceTypeCompression = 0
    swsPreLoadForceTypeTension = 1

class swsPreloadForce_e(IntEnum):
    """swsPreloadForce_e (2 constants, from CosmosWorksLib)."""
    swsPreloadForceAxial = 0
    swsPreloadForceTorque = 1

class swsPressureEndEditError_e(IntEnum):
    """swsPressureEndEditError_e (9 constants, from CosmosWorksLib)."""
    swsPressureEndEditErrorSuccessful = 0
    swsPressureEndEditErrorNoEntityAtIndex = 1
    swsPressureEndEditErrorEntityAlreadyAdded = 2
    swsPressureEndEditErrorNoEntities = 3
    swsPressureEndEditErrorSelectFacesOrShellEdges = 4
    swsPressureEndEditErrorSelectFaceOrShellEdge = 5
    swsPressureEndEditErrorRefGeomPreExist = 6
    swsPressureEndEditErrorSelectFaceEdgePlaneOrAxis = 7
    swsPressureEndEditErrorSelectCoordinateSystem = 8

class swsPressureError_e(IntEnum):
    """swsPressureError_e (8 constants, from CosmosWorksLib)."""
    swsPressureErrorSuccessful = 0
    swsPressureErrorSelectFaceOrFaces = 1
    swsPressureErrorSelectFacesOrShellEdges = 2
    swsPressureErrorSelectFaceEdgePlaneOrAxis = 3
    swsPressureErrorPressureType = 4
    swsPressureErrorInvalidStudy = 5
    swsPressureErrorInvalidArray = 6
    swsPressureErrorCannotApplyPressure = 7

class swsPressureReferenceGeometryCylindricalType_e(IntEnum):
    """swsPressureReferenceGeometryCylindricalType_e (3 constants, from CosmosWorksLib)."""
    swsPressureReferenceGeometryCylindricalTypeRadial = 1
    swsPressureReferenceGeometryCylindricalTypeCircumferential = 2
    swsPressureReferenceGeometryCylindricalTypeAxial = 3

class swsPressureReferenceGeometryEdgeType_e(IntEnum):
    """swsPressureReferenceGeometryEdgeType_e (1 constants, from CosmosWorksLib)."""
    swsPressureReferenceGeometryEdgeTypeAlongEdge = 3

class swsPressureReferenceGeometryPlanarType_e(IntEnum):
    """swsPressureReferenceGeometryPlanarType_e (3 constants, from CosmosWorksLib)."""
    swsPressureReferenceGeometryPlanarTypeAlongPlaneDir1 = 1
    swsPressureReferenceGeometryPlanarTypeAlongPlaneDir2 = 2
    swsPressureReferenceGeometryPlanarTypeNormalToPlane = 3

class swsPressureReferenceGeometryReferenceAxisType_e(IntEnum):
    """swsPressureReferenceGeometryReferenceAxisType_e (3 constants, from CosmosWorksLib)."""
    swsPressureReferenceGeometryReferenceAxisTypeRadial = 1
    swsPressureReferenceGeometryReferenceAxisTypeCircumferential = 2
    swsPressureReferenceGeometryReferenceAxisTypeAxial = 3

class swsPressureType_e(IntEnum):
    """swsPressureType_e (2 constants, from CosmosWorksLib)."""
    swsPressureTypeNormal = 0
    swsPressureTypeUseReferenceGeometry = 1

class swsPressureUnit_e(IntEnum):
    """swsPressureUnit_e (4 constants, from CosmosWorksLib)."""
    swsPressureUnit_NewtonsPerMeterSquared = 0
    swsPressureUnit_PSI = 1
    swsPressureUnit_KilogramForcePerCentimeterSquared = 2
    swsPressureUnit_NewtonsPerMillimeterSquared = 3

class swsProbePostResultErrorCode_e(IntEnum):
    """swsProbePostResultErrorCode_e (15 constants, from CosmosWorksLib)."""
    swsProbePostResultError_Success = 0
    swsProbePostResultError_NoActiveView = 1
    swsProbePostResultError_NoActiveStudy = 2
    swsProbePostResultError_ResultPlotActivationFailure = 3
    swsProbePostResultError_UsedBeforeCallingBeginProbing = 4
    swsProbePostResultError_InvalidOrEmptyInputArray = 5
    swsProbePostResultError_ActiveStudyIsNotRun = 6
    swsProbePostResultError_MeshDataLoadFailure = 7
    swsProbePostResultError_ProbingNotSupportedOnShellForSectionPlot = 8
    swsProbePostResultError_ProbingNotSupportedOnDeformationPlot = 9
    swsProbePostResultError_ProbingNotSupportedOnSectionPlotExplodedAfterClip = 10
    swsProbePostResultError_InitializationFailure = 11
    swsProbePostResultError_NoAssociatedStudyFoundForFatigueAnalysis = 12
    swsProbePostResultError_NoResultOrMeshPlotIsActivated = 13
    swsProbePostResultError_NotAllNodeElemsAreAnnotated = 14

class swsProbePostResultNodeElementSelectionWarning_e(IntEnum):
    """swsProbePostResultNodeElementSelectionWarning_e (4 constants, from CosmosWorksLib)."""
    swsProbePostResultNodeElemSelectionWarning_FewElemsLieOnBeamGaps = 1
    swsProbePostResultNodeElemSelectionWarning_FewNodeElemsNotOnSectionPlane = 2
    swsProbePostResultNodeElemSelectionWarning_FewNodeElemsOutOfRange = 4
    swsProbePostResultNodeElemSelectionWarning_FewNodeElemsLieOnNonRenderedBody = 8

class swsProbePostResultOption_e(IntEnum):
    """swsProbePostResultOption_e (5 constants, from CosmosWorksLib)."""
    swsProbePostResultOption_AtLocation = 0
    swsProbePostResultOption_FromSensors = 1
    swsProbePostResultOption_OnSelectedEntities = 2
    swsProbePostResultOption_AtDistance = 3
    swsProbePostResultOption_AtNodeElemNumber = 4

class swsRadiationEndEditError_e(IntEnum):
    """swsRadiationEndEditError_e (8 constants, from CosmosWorksLib)."""
    swsRadiationEndEditErrorSuccessful = 0
    swsRadiationEndEditErrorNoEntityAtIndex = 1
    swsRadiationEndEditErrorEntityAlreadyExists = 2
    swsRadiationEndEditErrorNoEntities = 3
    swsRadiationEndEditErrorSelectFace = 4
    swsRadiationEndEditErrorSelectFaceOrEdge = 5
    swsRadiationEndEditErrorEmissivity = 6
    swsRadiationEndEditErrorViewFactor = 7

class swsRadiationError_e(IntEnum):
    """swsRadiationError_e (7 constants, from CosmosWorksLib)."""
    swsRadiationErrorSuccessful = 0
    swsRadiationErrorSelectFaces = 1
    swsRadiationErrorSelectFaceOrShellEdge = 2
    swsRadiationErrorInvalidStudy = 3
    swsRadiationErrorRadiationType = 4
    swsRadiationErrorInvalidArray = 5
    swsRadiationErrorEmtpyArray = 6

class swsRadiationOpenSystem_e(IntEnum):
    """swsRadiationOpenSystem_e (2 constants, from CosmosWorksLib)."""
    swsRadiationOpenSystemClosed = 0
    swsRadiationOpenSystemOpen = 1

class swsRadiationType_e(IntEnum):
    """swsRadiationType_e (2 constants, from CosmosWorksLib)."""
    swsRadiationTypeSurfaceToAmbient = 0
    swsRadiationTypeSurfaceToSurface = 1

class swsRandomVibrationAnalysisMethod_e(IntEnum):
    """swsRandomVibrationAnalysisMethod_e (2 constants, from CosmosWorksLib)."""
    swsRandomVibrationAnalysisMethod_Standard = 0
    swsRandomVibrationAnalysisMethod_Approximate = 1

class swsRandomVibrationCorrelationOption_e(IntEnum):
    """swsRandomVibrationCorrelationOption_e (3 constants, from CosmosWorksLib)."""
    swsRandomVibrationCorrelationOption_FullyCorrelated = 0
    swsRandomVibrationCorrelationOption_FullyUnCorrelated = 1
    swsRandomVibrationCorrelationOption_PartiallyCorrelated = 2

class swsRefDispType_e(IntEnum):
    """swsRefDispType_e (4 constants, from CosmosWorksLib)."""
    swsNone = 0
    swsDatumPlane = 1
    swsCoordSys = 2
    swsDatumAxis = 3

class swsReferencePressureOption_e(IntEnum):
    """swsReferencePressureOption_e (2 constants, from CosmosWorksLib)."""
    swsReferencePressureOption_UseFld = 0
    swsReferencePressureOption_Define = 1

class swsRemoteLoadCheckCode_e(IntEnum):
    """swsRemoteLoadCheckCode_e (3 constants, from CosmosWorksLib)."""
    swsRemoteLoadCheckCode_None = 0
    swsRemoteLoadCheckCode_Load = 1
    swsRemoteLoadCheckCode_Displacement = 2

class swsRemoteLoadConnectionType_e(IntEnum):
    """swsRemoteLoadConnectionType_e (2 constants, from CosmosWorksLib)."""
    swsRemoteLoadConnectionType_Rigid = 0
    swsRemoteLoadConnectionType_Distributed = 1

class swsRemoteLoadEndEditError_e(IntEnum):
    """swsRemoteLoadEndEditError_e (17 constants, from CosmosWorksLib)."""
    swsRemoteLoadEndEditError_NoError = 0
    swsRemoteLoadEndEditError_SelectFaceEdgeOrVertex = 1
    swsRemoteLoadEndEditError_SelectCoordinateSystem = 2
    swsRemoteLoadEndEditError_InvalidLoadType = 3
    swsRemoteLoadEndEditError_InvalidStudyType = 4
    swsRemoteLoadEndEditError_InvalidArray = 5
    swsRemoteLoadEndEditError_EmptyArray = 6
    swsRemoteLoadEndEditError_EntityAlreadyAdded = 7
    swsRemoteLoadEndEditError_InvalidUnits = 8
    swsRemoteLoadEndEditError_InvalidMassArray = 9
    swsRemoteLoadEndEditError_InvalidMass = 10
    swsRemoteLoadEndEditError_CheckAtleastOneComp = 11
    swsRemoteLoadEndEditError_InvalidForAnalysis = 12
    swsRemoteLoadEndEditError_InvalidForNonSolid = 13
    swsRemoteLoadEndEditError_InvalidForRigid = 14
    swsRemoteLoadEndEditError_DisplacementMustBe0ForTopology = 15
    swsRemoteLoadEndEditError_InvalidConnectionType = 16

class swsRemoteLoadType_e(IntEnum):
    """swsRemoteLoadType_e (4 constants, from CosmosWorksLib)."""
    swsRemoteLoadType_DirectLoad = 0
    swsRemoteLoadType_RigidLoadOrMass = 1
    swsRemoteLoadType_RigidDisplacement = 2
    swsRemoteLoadType_DirectDisplacement = 3

class swsRemoteLoadWeightingFactor_e(IntEnum):
    """swsRemoteLoadWeightingFactor_e (4 constants, from CosmosWorksLib)."""
    swsRemoteLoadWeightingFactor_Default_Constant = 0
    swsRemoteLoadWeightingFactor_Linear = 1
    swsRemoteLoadWeightingFactor_Quadratic = 2
    swsRemoteLoadWeightingFactor_Cubic = 3

class swsReportFolderValue_e(IntEnum):
    """swsReportFolderValue_e (2 constants, from CosmosWorksLib)."""
    swsResultFolderAsReportFolder = 0
    swsUserDefinedReportFolder = 1

class swsResistanceType_e(IntEnum):
    """swsResistanceType_e (2 constants, from CosmosWorksLib)."""
    swsResistanceTypeTotal = 0
    swsResistanceTypeDistributed = 1

class swsRestraintEndEditError_e(IntEnum):
    """swsRestraintEndEditError_e (15 constants, from CosmosWorksLib)."""
    swsRestraintEndEditErrorSuccess = 0
    swsRestraintEndEditErrorNoIndex = 1
    swsRestraintEndEditErrorEntityExists = 2
    swsRestraintEndEditErrorNoEntity = 3
    swsRestraintEndEditErrorSelectFaceEdgeOrVertices = 4
    swsRestraintEndEditErrorSelectFaces = 5
    swsRestraintEndEditErrorSelectCylindricalFaces = 6
    swsRestraintEndEditErrorSelectSphericalFaces = 7
    swsRestraintEndEditErrorSelectFaceEdgeVertexOrFaces = 8
    swsRestraintEndEditErrorSelectPlaneAxisEdgeFaceOrCylinder = 9
    swsRestraintEndEditErrorCyclicSymmetryRestraint = 10
    swsRestraintEndEditErrorSelectTwoFaces = 11
    swsRestraintEndEditErrorSelectAxis = 12
    swsRestraintEndEditErrorDefineDisplacementComponent = 13
    swsRestraintEndEditErrorCannotRestrainRefGeometryEntity = 14

class swsRestraintError_e(IntEnum):
    """swsRestraintError_e (15 constants, from CosmosWorksLib)."""
    swsRestraintErrorSuccess = 0
    swsRestraintErrorSelectFacesEdgesOrVertices = 1
    swsRestraintErrorSelectPlanarFace = 2
    swsRestraintErrorSpecifyCylindricalFace = 3
    swsRestraintErrorSpecifySphericalFace = 4
    swsRestraintErrorSpecifyFaceEdgePlaneOrAxis = 6
    swsRestraintErrorSelectFace = 7
    swsRestraintErrorInMeshType = 8
    swsRestraintErrorInvalidStudyType = 9
    swsRestraintErrorNoEntities = 10
    swsRestraintErrorInvalidArray = 11
    swsRestraintErrorSpecifyTwoFacesOneAxis = 12
    swsRestraintErrorInvalidRestraintType = 13
    swsRestraintErrorCannotApplyRestraint = 14
    swsRestraintErrorInvalidMesh = 15

class swsRestraintType_e(IntEnum):
    """swsRestraintType_e (10 constants, from CosmosWorksLib)."""
    swsRestraintTypeFixed = 0
    swsRestraintTypeImmovable = 1
    swsRestraintTypeSymmetric = 2
    swsRestraintTypeRoller = 3
    swsRestraintTypeHinge = 4
    swsRestraintTypeReferenceGeometry = 5
    swsRestraintTypeFlatFace = 6
    swsRestraintTypeCylindricalFaces = 7
    swsRestraintTypeSphericalSurface = 8
    swsRestraintTypeCyclicSymmetry = 9

class swsResultEnvelopeBoundary(IntEnum):
    """swsResultEnvelopeBoundary (3 constants, from CosmosWorksLib)."""
    swsResultEnvelopeBoundary_Max = 0
    swsResultEnvelopeBoundary_Min = 1
    swsResultEnvelopeBoundary_AbsMax = 2

class swsResultFolderValue_e(IntEnum):
    """swsResultFolderValue_e (2 constants, from CosmosWorksLib)."""
    swsSolidWorksDocumentFolder = 0
    swsUserDefinedFolder = 1

class swsResultOptionsSensorOption_e(IntEnum):
    """swsResultOptionsSensorOption_e (3 constants, from CosmosWorksLib)."""
    swsResultOptionsSensorOption_None = -1
    swsResultOptionsSensorOption_AllTrackedDataSensors = 0
    swsResultOptionsSensorOption_SpecificSensor = 1

class swsResultPlotColorOption_ErrorCode_e(IntEnum):
    """swsResultPlotColorOption_ErrorCode_e (4 constants, from CosmosWorksLib)."""
    swsResultPlotColorOption_NoError = 0
    swsResultPlotColorOption_WrongBoundaryOption = 1
    swsResultPlotColorOption_FailToGetColors = 2
    swsResultPlotColorOption_WrongRGBValues = 3

class swsResultPlotDelete_ErrorCode_e(IntEnum):
    """swsResultPlotDelete_ErrorCode_e (4 constants, from CosmosWorksLib)."""
    swsResultPlotDelete_NoError = 0
    swsResultPlotDelete_InvalidResultType = 1
    swsResultPlotDelete_InvalidResultComponent = 2
    swsResultPlotDelete_FailToDelete = 3

class swsResultPlotErrorCode_e(IntEnum):
    """swsResultPlotErrorCode_e (21 constants, from CosmosWorksLib)."""
    swsResultPlot_NoError = 0
    swsResultPlot_InvalidStudy = 1
    swsResultPlot_FailedPlotCreation = 2
    swsResultPlot_InvalidSelectedEntities = 3
    swsResultPlot_InvalidInputArgInCombiWithTensorVectorFlag = 4
    swsResultPlot_InvalidResultType = 5
    swsResultPlot_InvalidComponentType = 6
    swsResultPlot_InvalidUnitType = 7
    swsResultPlot_IsAvailableOnlyForElements = 8
    swsResultPlot_InvalidMeshAppliedToStudy = 9
    swsResultPlot_TryingToSetInvalidProperty = 10
    swsResultPlot_IsAvailableOnlyForNodes = 11
    swsResultPlot_InvalidStudyType = 12
    swsResultPlot_ImproperResultsEquation = 13
    swsResultPlot_PlotDoesNotExist = 14
    swsResultPlot_EquivalentStressNotApplicable = 15
    swsResultPlot_CosworksViewNotPresent = 16
    swsResultPlot_InvalidExternalResultsFile = 17
    swsResultPlot_InvalidIsoValueRange = 18
    swsResultPlot_InvalidSmoothingCycleRange = 19
    swsResultPlot_MeshInformationNotFound = 20

class swsResultStressLinearizationErrors_e(IntEnum):
    """swsResultStressLinearizationErrors_e (14 constants, from CosmosWorksLib)."""
    swsStressLinearization_Success = 0
    swsStressLinearization_StudyNotSupported = 1
    swsStressLinearization_MeshTypeNotSupported = 2
    swsStressLinearization_InvalidReferencePlane = 3
    swsStressLinearization_DatabaseNotAvailable = 4
    swsStressLinearization_IncorrectNumberOfIntermediatePoints = 5
    swsStressLinearization_ElementsNotFoundForEndPoints = 6
    swsStressLinearization_ElementsFromDifferentComponents = 7
    swsStressLinearization_AllElementsNotFoundForIntermediatePoints = 8
    swsStressLinearization_SpecifiedPointsNotOnSectionPlane = 9
    swsStressLinearization_ElementalValuesNotSupported = 10
    swsStressLinearization_VectorPlotNotSupported = 11
    swsStressLinearization_InvalidResultComponent = 12
    swsStressLinearization_InvalidNumberOfPointsSelected = 13

class swsResultsDisplacementAndVelocityOption_e(IntEnum):
    """swsResultsDisplacementAndVelocityOption_e (3 constants, from CosmosWorksLib)."""
    swsResultsDisplacementAndVelocityOption_None = -1
    swsResultsDisplacementAndVelocityOption_Relative = 0
    swsResultsDisplacementAndVelocityOption_Absolute = 1

class swsResultsError_e(IntEnum):
    """swsResultsError_e (10 constants, from CosmosWorksLib)."""
    swsResultsErrorSuccessful = 0
    swsResultsErrorDatabaseNotAvailable = 1
    swsResultsErrorIncorrectStepNumber = 2
    swsResultsErrorIncorrectReferenceEntity = 3
    swsResultsErrorNoResultType = 4
    swsResultsErrorInvalidComponent = 5
    swsResultsErrorIncorrectCodeNumber = 6
    swsResultsErrorInvalidEntity = 7
    swsResultsErrorIncompatibleStudy = 8
    swsResultsErrorIncorrectModeShape = 9

class swsResultsRotationalDisplacementUnit_e(IntEnum):
    """swsResultsRotationalDisplacementUnit_e (4 constants, from CosmosWorksLib)."""
    swsResultsRotationalDisplacementUnitDeg = 0
    swsResultsRotationalDisplacementUnitDegMin = 1
    swsResultsRotationalDisplacementUnitDegMinSec = 2
    swsResultsRotationalDisplacementUnitRad = 3

class swsRigidConnectorEndEditError_e(IntEnum):
    """swsRigidConnectorEndEditError_e (11 constants, from CosmosWorksLib)."""
    swsRigidConnectorEndEditErrorSuccessful = 0
    swsRigidConnectorEndEditErrorNoEntityAtIndex = 1
    swsRigidConnectorEndEditErrorEntityAlreadyAdded = 2
    swsRigidConnectorEndEditErrorSelectTargetEntityOrFaces = 3
    swsRigidConnectorEndEditErrorSelectFace = 4
    swsRigidConnectorEndEditErrorIndexTooBig = 5
    swsRigidConnectorEndEditErrorHasBeamBody = 6
    swsRigidConnectorEndEditErrorHasMassBody = 7
    swsRigidConnectorEndEditErrorFacesOnSameComponent = 8
    swsRigidConnectorEndEditErrorBodyExcludedFromAnalysis = 9
    swsRigidConnectorEndEditErrorNullEntity = 10

class swsRigidConnectorError_e(IntEnum):
    """swsRigidConnectorError_e (15 constants, from CosmosWorksLib)."""
    swsRigidConnectorErrorSuccessful = 0
    swsRigidConnectorErrorInvalidMesh = 1
    swsRigidConnectorErrorNonlinearStudyPartDocument = 2
    swsRigidConnectorErrorInvalidStudy = 3
    swsRigidConnectorErrorSelectAssemblyDocument = 4
    swsRigidConnectorErrorInvalidSourceArray = 5
    swsRigidConnectorErrorNoObjectForFace = 6
    swsRigidConnectorErrorInvalidTargetArray = 7
    swsRigidConnectorErrorNoObjectForTarget = 8
    swsRigidConnectorErrorSelectFace = 9
    swsRigidConnectorErrorSameEntityAtFaceAndTargetArray = 10
    swsRigidConnectorErrorBodyHasRemoteMass = 11
    swsRigidConnectorErrorNullOrEmptyArray = 12
    swsRigidConnectorErrorFacesFromSameComponent = 13
    swsRigidConnectorErrorBodyExcludedFromAnalysis = 14

class swsRotationUnit_e(IntEnum):
    """swsRotationUnit_e (4 constants, from CosmosWorksLib)."""
    swsRotationUnit_Degrees = 0
    swsRotationUnit_DegreesMin = 1
    swsRotationUnit_DegreesMinSec = 2
    swsRotationUnit_Radians = 3

class swsRunAnalysisError_e(IntEnum):
    """swsRunAnalysisError_e (30 constants, from CosmosWorksLib)."""
    swsRunAnalysisErrorSuccessful = 0
    swsRunAnalysisErrorUseHighQualityMesh = 1
    swsRunAnalysisErrorDefineRigidVirtualWallContact = 2
    swsRunAnalysisDefineInitialTemperature = 3
    swsRunAnalysisErrorMultipleLoadsUseSameTimeCurve = 4
    swsRunAnalysisErrorSetUpDropTestStudy = 5
    swsRunAnalysisErrorNeedOneOrMoreStaticStudies = 6
    swsRunAnalysisErrorNoFatigueEvent = 7
    swsRunAnalysisErrorTimeDependentOrAmplitideOnlyLoads = 8
    swsRunAnalysisErrorNoSNCurve = 9
    swsRunAnalysisErrorMeshNotIdentical = 11
    swsRunAnalysisErrorNoValidShell = 12
    swsRunAnalysisErrorEXMaterialPropertyNotDefined = 13
    swsRunAnalysisErrorEXValue = 14
    swsRunAnalysisErrorPoissonsRatio = 15
    swsRunAnalysisErrorThermalConductivityNotDefined = 16
    swsRunAnalysisErrorRemoveOrChangeCreep = 17
    swsRunAnalysisErrorMaterialNotDefinedForShells = 18
    swsRunAnalysisErrorMaterialNotDefined = 19
    swsRunAnalysisErrorMaterialNotDefinedForComponents = 20
    swsRunAnalysisErrorNoSolidBody = 21
    swsRunAnalysisErrorAuthorizationFailed = 22
    swsRunAnalysisErrorMeshNotFound = 23
    swsRunAnalysisErrorAnalysisFailed = 24
    swsRunAnalysisErrorStudyNotExist = 25
    swsRunAnalysisErrorPadaptiveNotSupportLargeDisplacement = 26
    swsRunAnalysisErrorPadaptiveNotSupportCyclicSymmetry = 27
    swsRunAnalysisErrorPadaptiveNotSupportNoPenetration = 28
    swsRunAnalysisErrorPadaptiveNotSupportRemoteLoadMassGapContactConnector = 29
    swsRunAnalysisErrorInvalidLBC = 30

class swsRunStressHotSpotDiagnosticsError_e(IntEnum):
    """swsRunStressHotSpotDiagnosticsError_e (8 constants, from CosmosWorksLib)."""
    swsRunStressHotSpotDiagnostics_NoError = 0
    swsRunStressHotSpotDiagnostics_NotSupportedForThisStudy = 1
    swsRunStressHotSpotDiagnostics_ImproperSensitivityFactor = 2
    swsRunStressHotSpotDiagnostics_ResultsNotAvailable = 3
    swsRunStressHotSpotDiagnostics_ImproperMeshRefineLevels = 4
    swsRunStressHotSpotDiagnostics_ImproperReductionFactor = 5
    swsRunStressHotSpotDiagnostics_ImproperGrowthRatio = 6
    swsRunStressHotSpotDiagnostics_ImproperResultRestoreOption = 7

class swsRunStudiesErrorCode_e(IntEnum):
    """swsRunStudiesErrorCode_e (7 constants, from CosmosWorksLib)."""
    swsRunStudiesErrorCode_Success = 0
    swsRunStudiesErrorCode_NoStudyIsSelectedOrDefined = 1
    swsRunStudiesErrorCode_InvalidStudiesAreSelected = 2
    swsRunStudiesErrorCode_UnknownError = 3
    swsRunStudiesErrorCode_AllStudiesRunFailed = 4
    swsRunStudiesErrorCode_FewStudiesRunFailed = 5
    swsRunStudiesErrorCode_NoActiveStudy = 6

class swsRunStudiesResultsErrorCode_e(IntEnum):
    """swsRunStudiesResultsErrorCode_e (4 constants, from CosmosWorksLib)."""
    swsRunStudiesResultsErrorCode_Success = 0
    swsRunStudiesResultsErrorCode_InvalidInputArg = 1
    swsRunStudiesResultsErrorCode_ResultsNotAvailable = 2
    swsRunStudiesResultsErrorCode_ReachedEndOfResults = 3

class swsRunStudiesRunMeshOptionErrorCode_e(IntEnum):
    """swsRunStudiesRunMeshOptionErrorCode_e (5 constants, from CosmosWorksLib)."""
    swsRunStudiesRunMeshOptionErrorCode_Success = 0
    swsRunStudiesRunMeshOptionErrorCode_StudyAlreadyAdded = 1
    swsRunStudiesRunMeshOptionErrorCode_StudyIsNotAdded = 2
    swsRunStudiesRunMeshOptionErrorCode_OptionCannotBeReplaced = 3
    swsRunStudiesRunMeshOptionErrorCode_InvalidOptionApplied = 4

class swsRunStudiesRunMeshOptions_e(IntEnum):
    """swsRunStudiesRunMeshOptions_e (2 constants, from CosmosWorksLib)."""
    swsRunStudiesRunMeshOptions_MeshOnly = 0
    swsRunStudiesRunMeshOptions_MeshAndRun = 1

class swsRunStudiesStatusCode_e(IntEnum):
    """swsRunStudiesStatusCode_e (5 constants, from CosmosWorksLib)."""
    swsRunStudiesStatusCode_AnalysisSucceeded = 0
    swsRunStudiesStatusCode_MeshSucceeded = 1
    swsRunStudiesStatusCode_AnalysisFailed = 2
    swsRunStudiesStatusCode_MeshFailed = 3
    swsRunStudiesStatusCode_UnknownError = 4

class swsSaveResultsOption_e(IntEnum):
    """swsSaveResultsOption_e (2 constants, from CosmosWorksLib)."""
    swsSaveResultsOption_ForAllSolutionSteps = 0
    swsSaveResultsOption_ForSpecifiedSolutionSteps = 1

class swsSaveeDrawingsErrorCode_e(IntEnum):
    """swsSaveeDrawingsErrorCode_e (11 constants, from CosmosWorksLib)."""
    swsSaveeDrawings_NoError = 0
    swsSaveeDrawings_CosworksViewNotPresent = 1
    swsSaveeDrawings_PlotNotFoundError = 2
    swsSaveeDrawings_ResultFolderNotFound = 3
    swsSaveeDrawings_DatabaseNotFound = 4
    swsSaveeDrawings_PostFilesNull = 5
    swsSaveeDrawings_PlotNotActive = 6
    swsSaveeDrawings_NotAvailableForCurrentMesh = 7
    swsSaveeDrawings_PostDataFilesNotPresent = 8
    swsSaveeDrawings_NoPlots = 9
    swsSaveeDrawings_PlotSaveError = 10

class swsSelectionType_e(IntEnum):
    """swsSelectionType_e (3 constants, from CosmosWorksLib)."""
    swsSelectionFaceEdgeVertexPoint = 0
    swsSelectionBeamEndJoints = 1
    swsSelectionBeams = 2

class swsSetDampingRatiosError_e(IntEnum):
    """swsSetDampingRatiosError_e (6 constants, from CosmosWorksLib)."""
    swsSetDampingRatiosError_NoError = 0
    swsSetDampingRatiosError_NotAvailable = 1
    swsSetDampingRatiosError_InvalidRows = 2
    swsSetDampingRatiosError_InvalidArray = 3
    swsSetDampingRatiosError_InCorrectValues = 4
    swsSetDampingRatiosError_OptionsNotAvailable = 5

class swsShellEndEditError_e(IntEnum):
    """swsShellEndEditError_e (11 constants, from CosmosWorksLib)."""
    swsShellEndEditErrorSuccessful = 0
    swsShellEndEditErrorShellThickness = 1
    swsShellEndEditErrorFormulation = 2
    swsShellEndEditErrorNotEntityAtIndex = 3
    swsShellEndEditErrorSelectFace = 4
    swsShellEndEditErrorFaceAlreadyExists = 5
    swsShellEndEditErrorFaceAlreadyDefinedAsShell = 6
    swsShellEndEditErrorNoEntitySelected = 7
    swsShellEndEditErrorUnit = 8
    swsShellEndEditErrorOffsetOption = 9
    swsShellEndEditErrorOffsetValue = 10

class swsShellFace_e(IntEnum):
    """swsShellFace_e (4 constants, from CosmosWorksLib)."""
    swsShellFace_Top = 0
    swsShellFace_Bottom = 1
    swsShellFace_Membrane = 2
    swsShellFace_Bending = 3

class swsShellFormulation_e(IntEnum):
    """swsShellFormulation_e (3 constants, from CosmosWorksLib)."""
    swsShellFormulationThin = 0
    swsShellFormulationThick = 1
    swsShellFormulationComposite = 2

class swsShellManagerError_e(IntEnum):
    """swsShellManagerError_e (8 constants, from CosmosWorksLib)."""
    swsShellManagerErrorSuccessful = 0
    swsShellManagerErrorCannotApplyShellForStudy = 1
    swsShellManagerErrorCannotApplyShellForMesh = 2
    swsShellManagerErrorEmptyArray = 3
    swsShellManagerErrorInvalidArray = 4
    swsShellManagerErrorSelectFacesOnly = 5
    swsShellManagerErrorFaceAlreadyDefinedAsShell = 6
    swsShellManagerErrorFaceAlreadyExists = 7

class swsShellOffsetOption_e(IntEnum):
    """swsShellOffsetOption_e (4 constants, from CosmosWorksLib)."""
    swsShellOffsetOption_Middle = 0
    swsShellOffsetOption_Top = 1
    swsShellOffsetOption_Bottom = 2
    swsShellOffsetOption_SpecifyRatio = 3

class swsShrinkFitOption_e(IntEnum):
    """swsShrinkFitOption_e (2 constants, from CosmosWorksLib)."""
    swsShrinkFitOptionNodeToSurface = 0
    swsShrinkFitOptionSurfaceToSurface = 1

class swsSimAdaptiveMethodType_e(IntEnum):
    """swsSimAdaptiveMethodType_e (3 constants, from CosmosWorksLib)."""
    swsNoneMethod = 0
    swsHAdaptive = 1
    swsPAdative = 2

class swsSimMassPropertiesError_e(IntEnum):
    """swsSimMassPropertiesError_e (14 constants, from CosmosWorksLib)."""
    swsSimMassPropertiesErrorSuccessful = 0
    swsSimMassPropertiesErrorBodiesNotFound = 1
    swsSimMassPropertiesErrorBoltNotFound = 2
    swsSimMassPropertiesErrorPinNotFound = 3
    swsSimMassPropertiesErrorRemoteLoadNotFound = 4
    swsSimMassPropertiesErrorDistributedMassNotFound = 5
    swsSimMassPropertiesErrorBoltMassNotIncluded = 6
    swsSimMassPropertiesErrorPinMassNotIncluded = 7
    swsSimMassPropertiesErrorRemoteLoadMassNotIncluded = 8
    swsSimMassPropertiesErrorUnsuccessful = 9
    swsSimMassPropertiesErrorLinkageRodNotFound = 10
    swsSimMassPropertiesErrorLinkageRodMassNotIncluded = 11
    swsSimMassPropertiesErrorCableNotFound = 12
    swsSimMassPropertiesErrorCableMassNotIncluded = 13

class swsSimulationElementTypes_e(IntEnum):
    """swsSimulationElementTypes_e (4 constants, from CosmosWorksLib)."""
    swsSolidElement = 0
    swsShellElement = 1
    swsBeamElement = 2
    swsTrussElement = 3

class swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e(IntEnum):
    """swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e (2 constants, from CosmosWorksLib)."""
    swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh = 0
    swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_TranslucentSingleColor = 1

class swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e(IntEnum):
    """swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e (3 constants, from CosmosWorksLib)."""
    swsSimulationOptionDefaultPlotsBoundaryColorInRGBNoError = 0
    swsSimulationOptionDefaultPlotsBoundaryColorInRGBWrongBoundaryOption = 1
    swsSimulationOptionDefaultPlotsBoundaryColorInRGBGetColorUnsuccessful = 2

class swsSolverType_e(IntEnum):
    """swsSolverType_e (7 constants, from CosmosWorksLib)."""
    swsSolverTypeAutomatic = 0
    swsSolverTypeDirectSparse = 1
    swsSolverTypeFFEPlus = 2
    swsSolverTypeCASI = 5
    swsSolverTypeAbaqus = 6
    swsSolverTypeINTEL = 7
    swsSolverTypeINTELCluster = 8

class swsSpotWeldConnectorEndEditError_e(IntEnum):
    """swsSpotWeldConnectorEndEditError_e (18 constants, from CosmosWorksLib)."""
    swsSpotWeldConnectorEndEditErrorSuccessful = 0
    swsSpotWeldConnectorEndEditErrorNullEntity = 1
    swsSpotWeldConnectorEndEditErrorEntityAlreadyExists = 2
    swsSpotWeldConnectorEndEditErrorFaceIsEmpty = 3
    swsSpotWeldConnectorEndEditErrorSelectParallelFaces = 5
    swsSpotWeldConnectorEndEditErrorPlanesShouldTouch = 6
    swsSpotWeldConnectorEndEditErrorGapTooBig = 7
    swsSpotWeldConnectorEndEditErrorSelectDatumPoints = 8
    swsSpotWeldConnectorEndEditErrorPositiveStudDiameter = 9
    swsSpotWeldConnectorEndEditErrorStudDiameter = 10
    swsSpotWeldConnectorEndEditErrorHasBeamBody = 11
    swsSpotWeldConnectorEndEditErrorHasMassElement = 12
    swsSpotWeldConnectorEndEditErrorSpotWeldDiameter = 13
    swsSpotWeldConnectorEndEditErrorIndexTooBig = 14
    swsSpotWeldConnectorEndEditErrorNoEntityAtIndex = 15
    swsSpotWeldConnectorEndEditErrorSelectFace = 16
    swsSpotWeldConnectorEndEditErrorInvalidPoints = 17
    swsSpotWeldConnectorEndEditErrorBodyExcludedFromAnalysis = 18

class swsSpotWeldConnectorError_e(IntEnum):
    """swsSpotWeldConnectorError_e (17 constants, from CosmosWorksLib)."""
    swsSpotWeldConnectorErrorSuccessful = 0
    swsSpotWeldConnectorErrorInvalidMesh = 1
    swsSpotWeldConnectorErrorNonlinearStudyPartDocument = 2
    swsSpotWeldConnectorErrorInvalidStudy = 3
    swsSpotWeldConnectorErrorNullDispatch = 4
    swsSpotWeldConnectorErrorSelectAssemblyDocument = 5
    swsSpotWeldConnectorErrorSelectFace = 6
    SpotWeldConnectorErrorSelectVerticesOrDatumPoint = 7
    swsSpotWeldConnectorErrorPlanesNotParallel = 8
    swsSpotWeldConnectorErrorPlanesTouching = 9
    swsSpotWeldConnectorErrorGapTooBig = 10
    swsSpotWeldConnectorErrorSelectDatumPoints = 11
    swsSpotWeldConnectorErrorPostWeldInvalidPoints = 12
    swsSpotWeldConnectorErrorInvalidArray = 13
    swsSpotWeldConnectorErrorEmptyArray = 14
    swsSpotWeldConnectorErrorHasRemoteMass = 15
    swsSpotWeldConnectorErrorBodyExcludedFromAnalysis = 16

class swsSpringConnectorEndEditError_e(IntEnum):
    """swsSpringConnectorEndEditError_e (19 constants, from CosmosWorksLib)."""
    swsSpringConnectorEndEditErrorSuccessful = 0
    swsSpringConnectorEndEditErrorNoEntity = 1
    swsSpringConnectorEndEditErrorSelectFace = 2
    swsSpringConnectorEndEditErrorSelectPlanarFace = 3
    swsSpringConnectorEndEditErrorSelectTwoParallelPlanarFaces = 4
    swsSpringConnectorEndEditErrorSelectFaceWithCylindricalSurface = 5
    swsSpringConnectorEndEditErrorSelectConcentricCylindricalFaces = 6
    swsSpringConnectorEndEditErrorRadiiNotEqual = 7
    swsSpringConnectorEndEditErrorNormalTangentialOrRotationalStiffness = 8
    swsSpringConnectorEndEditErrorStiffness = 9
    swsSpringConnectorEndEditErrorSelectDatumPointOrVertex = 10
    swsSpringConnectorEndEditErrorEntityAlreadyExists = 11
    swsSpringConnectorEndEditErrorNoEntityAtIndex = 12
    swsSpringConnectorEndEditErrorIndexInvalidForRemovalOfEntity = 13
    swsSpringConnectorEndEditErrorHasBeamBody = 14
    swsSpringConnectorEndEditErrorHasMassElement = 15
    swsSpringConnectorEndEditErrorSelectionsBelongToSameBody = 16
    swsSpringConnectorEndEditErrorNullEntity = 17
    swsSpringConnectorEndEditErrorBodyExcludedFromAnalysis = 18

class swsSpringConnectorError_e(IntEnum):
    """swsSpringConnectorError_e (23 constants, from CosmosWorksLib)."""
    swsSpringConnectorErrorSuccessful = 0
    swsSpringConnectorErrorInvalidMesh = 1
    swsSpringConnectorErrorNonlinearStudyPartDocument = 2
    swsSpringConnectorErrorInvalidStudy = 3
    swsSpringConnectorErrorSelectEntities = 4
    swsSpringConnectorErrorSelectFace = 5
    swsSpringConnectorErrorSelectFaceWithCylindricalSurface = 6
    swsSpringConnectorErrorSelectTwoConcentricCylindricalFaces = 7
    swsSpringConnectorErrorCylindricalFacesRadiiNotEqual = 8
    swsSpringConnectorErrorSelectPlanarFace = 9
    swsSpringConnectorErrorSelectTwoPlanarFaces = 10
    swsSpringConnectorErrorSourceTargetEntitiesSame = 11
    swsSpringConnectorErrorStudyNonlinearAndSpringSubtypeValue = 12
    swsSpringConnectorErrorInvalidArray = 13
    swsSpringConnectorErrorNumberPlanarFacesLessThanTwo = 14
    swsSpringConnectorErrorNoObjectForSourceOrTarget = 15
    swsSpringConnectorErrorSelectDatumPoint = 16
    swsSpringConnectorErrorTooManyEntitiesForSpringType = 17
    swsSpringConnectorErrorSelectionsOnToSameComponent = 18
    swsSpringConnectorErrorHasRemoteMass = 19
    swsSpringConnectorErrorEmptyArray = 20
    swsSpringConnectorErrorSpringSubtypeInvalidForShellMesh = 21
    swsSpringConnectorErrorBodyExcludedFromAnalysis = 22

class swsSpringConnectorType_e(IntEnum):
    """swsSpringConnectorType_e (3 constants, from CosmosWorksLib)."""
    swsSpringConnectoryTypeFlatParallelFaces = 0
    swsSpringConnectoryTypeConcentricCylindricalFaces = 1
    swsSpringConnectoryTypeBetweenVertices = 2

class swsSpringSubType_e(IntEnum):
    """swsSpringSubType_e (3 constants, from CosmosWorksLib)."""
    swsSpringSubTypeFlatParallelFaces = 0
    swsSpringSubTypeConcentricCylindricalFaces = 1
    swsSpringSubTypeBetweenVertices = 2

class swsSpringType_e(IntEnum):
    """swsSpringType_e (3 constants, from CosmosWorksLib)."""
    swsSpringTypeCompressionExtension = 0
    swsSpringTypeCompression = 1
    swsSpringTypeExtension = 2

class swsStaticResultDisplacementComponentTypes_e(IntEnum):
    """swsStaticResultDisplacementComponentTypes_e (15 constants, from CosmosWorksLib)."""
    swsStaticDisplacement_UX = 0
    swsStaticDisplacement_UY = 1
    swsStaticDisplacement_UZ = 2
    swsStaticDisplacement_URES = 3
    swsStaticDisplacement_RFX = 4
    swsStaticDisplacement_RFY = 5
    swsStaticDisplacement_RFZ = 6
    swsStaticDisplacement_RFRES = 7
    swsStaticDisplacement_RX = 8
    swsStaticDisplacement_RY = 9
    swsStaticDisplacement_RZ = 10
    swsStaticDisplacement_RMX = 11
    swsStaticDisplacement_RMY = 12
    swsStaticDisplacement_RMZ = 13
    swsStaticDisplacement_RMRES = 14

class swsStaticResultElementalStrainComponentTypes_e(IntEnum):
    """swsStaticResultElementalStrainComponentTypes_e (12 constants, from CosmosWorksLib)."""
    swsStaticElementalStrain_EPSX = 0
    swsStaticElementalStrain_EPSY = 1
    swsStaticElementalStrain_EPSZ = 2
    swsStaticElementalStrain_GMXY = 3
    swsStaticElementalStrain_GMXZ = 4
    swsStaticElementalStrain_GMYZ = 5
    swsStaticElementalStrain_ESTRN = 6
    swsStaticElementalStrain_SEDENS = 7
    swsStaticElementalStrain_ENERGY = 8
    swsStaticElementalStrain_E1 = 9
    swsStaticElementalStrain_E2 = 10
    swsStaticElementalStrain_E3 = 11

class swsStaticResultElementalStressComponentTypes_e(IntEnum):
    """swsStaticResultElementalStressComponentTypes_e (14 constants, from CosmosWorksLib)."""
    swsStaticElementalStress_SX = 0
    swsStaticElementalStress_SY = 1
    swsStaticElementalStress_SZ = 2
    swsStaticElementalStress_TXY = 3
    swsStaticElementalStress_TXZ = 4
    swsStaticElementalStress_TYZ = 5
    swsStaticElementalStress_P1 = 6
    swsStaticElementalStress_P2 = 7
    swsStaticElementalStress_P3 = 8
    swsStaticElementalStress_VON = 9
    swsStaticElementalStress_INT = 10
    swsStaticElementalStress_TRI = 11
    swsStaticElementalStress_ERR = 12
    swsStaticElementalStress_CONTACTPRESS = 13

class swsStaticResultNodalStrainComponentTypes_e(IntEnum):
    """swsStaticResultNodalStrainComponentTypes_e (10 constants, from CosmosWorksLib)."""
    swsStaticNodalStrain_EPSX = 0
    swsStaticNodalStrain_EPSY = 1
    swsStaticNodalStrain_EPSZ = 2
    swsStaticNodalStrain_GMXY = 3
    swsStaticNodalStrain_GMXZ = 4
    swsStaticNodalStrain_GMYZ = 5
    swsStaticNodalStrain_ESTRN = 6
    swsStaticNodalStrain_E1 = 7
    swsStaticNodalStrain_E2 = 8
    swsStaticNodalStrain_E3 = 9

class swsStaticResultNodalStressComponentTypes_e(IntEnum):
    """swsStaticResultNodalStressComponentTypes_e (12 constants, from CosmosWorksLib)."""
    swsStaticNodalStress_SX = 0
    swsStaticNodalStress_SY = 1
    swsStaticNodalStress_SZ = 2
    swsStaticNodalStress_TXY = 3
    swsStaticNodalStress_TXZ = 4
    swsStaticNodalStress_TYZ = 5
    swsStaticNodalStress_P1 = 6
    swsStaticNodalStress_P2 = 7
    swsStaticNodalStress_P3 = 8
    swsStaticNodalStress_VON = 9
    swsStaticNodalStress_INT = 10
    swsStaticNodalStress_TRI = 11

class swsStiffnessType_e(IntEnum):
    """swsStiffnessType_e (2 constants, from CosmosWorksLib)."""
    swsStiffnessTypeDistributed = 0
    swsStiffnessTypeTotal = 1

class swsStrainComponent_e(IntEnum):
    """swsStrainComponent_e (12 constants, from CosmosWorksLib)."""
    swsStrainComponentEPSX = 0
    swsStrainComponentEPSY = 1
    swsStrainComponentEPSZ = 2
    swsStrainComponentGMXY = 3
    swsStrainComponentGMXZ = 4
    swsStrainComponentGMYZ = 5
    swsStrainComponentESTRN = 6
    swsStrainComponentSEDENS = 7
    swsStrainComponentENERGY = 8
    swsStrainComponentE1 = 9
    swsStrainComponentE2 = 10
    swsStrainComponentE3 = 11

class swsStrainEnergyDensityUnit_e(IntEnum):
    """swsStrainEnergyDensityUnit_e (3 constants, from CosmosWorksLib)."""
    swsStrainEnergyDensityUnit_NewtonMeterPerCubicMeter = 0
    swsStrainEnergyDensityUnit_FootPoundPerCubicFeet = 1
    swsStrainEnergyDensityUnit_CaloriesPerCubicMeter = 2

class swsStrainEnergyUnit_e(IntEnum):
    """swsStrainEnergyUnit_e (3 constants, from CosmosWorksLib)."""
    swsStrainEnergyUnit_NewtonMeter = 0
    swsStrainEnergyUnit_FootPound = 1
    swsStrainEnergyUnit_Calories = 2

class swsStrengthUnit_e(IntEnum):
    """swsStrengthUnit_e (5 constants, from CosmosWorksLib)."""
    swsStrengthUnitPascal = 0
    swsStrengthUnitPSI = 1
    swsStrengthUnitKilogramsPerSquareCentimeter = 2
    swsStrengthUnitNewtonPerSquareMillimeter = 3
    swsStrengthUnitKSI = 4

class swsStressComponent_e(IntEnum):
    """swsStressComponent_e (15 constants, from CosmosWorksLib)."""
    swsStressComponentSX = 0
    swsStressComponentSY = 1
    swsStressComponentSZ = 2
    swsStressComponentTXY = 3
    swsStressComponentTXZ = 4
    swsStressComponentTYZ = 5
    swsStressComponentP1 = 6
    swsStressComponentP2 = 7
    swsStressComponentP3 = 8
    swsStressComponentVON = 9
    swsStressComponentINT = 10
    swsStressComponentTRI = 11
    swsStressComponentERR = 12
    swsStressComponentCP = 13
    swsStressComponentVONDC = 100

class swsStressHotSpotPlotError_e(IntEnum):
    """swsStressHotSpotPlotError_e (3 constants, from CosmosWorksLib)."""
    swsStressHotSpotPlot_NoError = 0
    swsStressHotSpotPlot_NoHotSpotsToPlot = 1
    swsStressHotSpotPlot_NodalHotSpotsNotAvailable = 2

class swsStressHotSpotResultsRestoreOptions_e(IntEnum):
    """swsStressHotSpotResultsRestoreOptions_e (2 constants, from CosmosWorksLib)."""
    swsStressHotSpotResultsRestoreOption_OriginalMesh = 0
    swsStressHotSpotResultsRestoreOption_FinalMesh = 1

class swsStudyError_e(IntEnum):
    """swsStudyError_e (6 constants, from CosmosWorksLib)."""
    swsNewStudyErrorSuccessful = 0
    swsNewStudyErrorNoSolidBody = 1
    swsNewStudyErrorSameNameStudyExistsOrInvalidStudyName = 2
    swsNewStudyErrorTypeNotDefined = 3
    swsNewStudyErrorInvalidMeshType = 4
    swsNewStudyErrorInvalidStudySubOption = 5

class swsStudyExportError_e(IntEnum):
    """swsStudyExportError_e (13 constants, from CosmosWorksLib)."""
    swsStudyExportError_NoError = 0
    swsStudyExportError_OptimizationNotAvailable = 1
    swsStudyExportError_TransientThermalNotAvailable = 2
    swsStudyExportError_DropTestNotAvailable = 3
    swsStudyExportError_CreepMaterial = 4
    swsStudyExportError_RemoteLoadConnectorNotAvailable = 5
    swsStudyExportError_LoadOnPointsNotAvailable = 6
    swsStudyExportError_WrongFileOption = 7
    swsStudyExportError_WrongCosmosExportOptionForNoMesh = 8
    swsStudyExportError_WrongCosmosExportOption = 9
    swsStudyExportError_WrongNastranExportOption = 10
    swsStudyExportError_Wrong_NastranExportUnit = 11
    swsStudyExportError_WrongCosmosExportUnit = 12

class swsStudyExportOption_e(IntEnum):
    """swsStudyExportOption_e (7 constants, from CosmosWorksLib)."""
    swsStudyExportOption_Cosmos = 0
    swsStudyExportOption_Ansys = 1
    swsStudyExportOption_Nastran = 2
    swsStudyExportOption_PatranNeutral = 3
    swsStudyExportOption_IdeasUniversal = 4
    swsStudyExportOption_Exodus = 5
    swsStudyExportOption_Abaqus = 6

class swsStudyMeshError_e(IntEnum):
    """swsStudyMeshError_e (8 constants, from CosmosWorksLib)."""
    swsStudyErrorSuccessful = 0
    swsStudyErrorNoValidShells = 1
    swsStudyErrorNoSolidBody = 2
    swsStudyErrorElementSizeTooSmall = 3
    swsStudyErrorElementSizeTooBig = 4
    swsStudyErrorSpecifyPositiveValue = 5
    swsStudyErrorSpecifyElementSizeScaleFactor = 6
    swsStudyErrorSpecifyToleranceScaleFactor = 7

class swsSuppressionState_e(IntEnum):
    """swsSuppressionState_e (2 constants, from CosmosWorksLib)."""
    swsSupressionStateSuppressed = 0
    swsSupressionStateUnsuppressed = 1

class swsSymmetricalBoltType_e(IntEnum):
    """swsSymmetricalBoltType_e (2 constants, from CosmosWorksLib)."""
    swsSymmtricalBoltTypeOneHalfSymmetry = 0
    swsSymmtricalBoltTypeOneQuarterSymmetry = 1

class swsTableDrivenDistOption_e(IntEnum):
    """swsTableDrivenDistOption_e (2 constants, from CosmosWorksLib)."""
    swsPercentage = 0
    swsDistance = 1

class swsTableDrivenInterpolationType_e(IntEnum):
    """swsTableDrivenInterpolationType_e (2 constants, from CosmosWorksLib)."""
    swsLinear = 0
    swsCubic = 1

class swsTemperatureCurveError_e(IntEnum):
    """swsTemperatureCurveError_e (4 constants, from CosmosWorksLib)."""
    swsTemperatureCurveErrorSuccessful = 0
    swsTemperatureCurveErrorInvalidStudy = 1
    swsTemperatureCurveErrorCurveCannotBeUsed = 2
    swsTemperatureCurveErrorNeedDataPoints = 3

class swsTemperatureEndEditError_e(IntEnum):
    """swsTemperatureEndEditError_e (6 constants, from CosmosWorksLib)."""
    swsTemperatureEndEditErrorSuccessful = 0
    swsTemperatureEndEditErrorNoEntityAtIndex = 1
    swsTemperatureEndEditErrorEntityAlreadyExists = 2
    swsTemperatureEndEditErrorNoEntities = 3
    swsTemperatureEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies = 4
    swsTemperatureEndEditErrorCannotSetInitialTemperatureType = 5

class swsTemperatureError_e(IntEnum):
    """swsTemperatureError_e (5 constants, from CosmosWorksLib)."""
    swsTemperatureErrorSuccessful = 0
    swsTemperatureErrorSelectVerticesEdgesFacesBodiesOrComponents = 1
    swsTemperatureErrorInvalidStudy = 2
    swsTemperatureErrorInvalidArray = 3
    swsTemperatureErrorEmptyArray = 4

class swsTemperatureType_e(IntEnum):
    """swsTemperatureType_e (2 constants, from CosmosWorksLib)."""
    swsTemperatureTypeInital = 0
    swsTemperatureTypeFixed = 1

class swsTemperatureUnit_e(IntEnum):
    """swsTemperatureUnit_e (3 constants, from CosmosWorksLib)."""
    swsTemperatureUnitKelvin = 0
    swsTemperatureUnitFahrenheit = 1
    swsTemperatureUnitCelsius = 2

class swsTensileStressAreaUnit_e(IntEnum):
    """swsTensileStressAreaUnit_e (5 constants, from CosmosWorksLib)."""
    swsTensileStressAreaUnitMillimetersSquared = 0
    swsTensileStressAreaUnitCentimetersSquared = 1
    swsTensileStressAreaUnitMetersSquared = 2
    swsTensileStressAreaUnitInchesSquared = 3
    swsTensileStressAreaUnitFeetSquared = 4

class swsThermalComponent_e(IntEnum):
    """swsThermalComponent_e (9 constants, from CosmosWorksLib)."""
    swsThermalComponentTEMP = 0
    swsThermalComponentGRADX = 1
    swsThermalComponentGRADY = 2
    swsThermalComponentGRADZ = 3
    swsThermalComponentGRADN = 4
    swsThermalComponentHFLUXX = 5
    swsThermalComponentHFLUXY = 6
    swsThermalComponentHFLUXZ = 7
    swsThermalComponentHFLUXN = 8

class swsThermalOption_e(IntEnum):
    """swsThermalOption_e (3 constants, from CosmosWorksLib)."""
    swsThermalOption_InputTemperature = 0
    swsThermalOption_TemperatureFromThermalStudy = 1
    swsThermalOption_TemperatureFromFlow = 2

class swsThermalRelaxationFactor_e(IntEnum):
    """swsThermalRelaxationFactor_e (2 constants, from CosmosWorksLib)."""
    swsThermalRelaxationFactorAutomatic = 0
    swsThermalRelaxationFactorFixed = 1

class swsThermalResultComponentTypes_e(IntEnum):
    """swsThermalResultComponentTypes_e (9 constants, from CosmosWorksLib)."""
    swsThermalResultComponentTypes_TEMP = 0
    swsThermalResultComponentTypes_GRADX = 1
    swsThermalResultComponentTypes_GRADY = 2
    swsThermalResultComponentTypes_GRADZ = 3
    swsThermalResultComponentTypes_GRADN = 4
    swsThermalResultComponentTypes_HFLUXX = 5
    swsThermalResultComponentTypes_HFLUXY = 6
    swsThermalResultComponentTypes_HFLUXZ = 7
    swsThermalResultComponentTypes_HFLUXN = 8

class swsThermalSolutionType_e(IntEnum):
    """swsThermalSolutionType_e (2 constants, from CosmosWorksLib)."""
    swsThermalSolutionTypeTransient = 0
    swsThermalSolutionTypeSteadyState = 1

class swsThreadsPerLengthUnit_e(IntEnum):
    """swsThreadsPerLengthUnit_e (2 constants, from CosmosWorksLib)."""
    swsThreadsPerLengthUnitPerMillimete = 0
    swsThreadsPerLengthUnitPerInch = 1

class swsTimeCurveError_e(IntEnum):
    """swsTimeCurveError_e (5 constants, from CosmosWorksLib)."""
    swsTimeCurveErrorSuccessful = 0
    swsTimeCurveErrorInvalidStudyType = 1
    swsTimeCurveErrorCannotUseWithRestraint = 2
    swsTimeCurveErrorNeedTwoOrMoreDataPoints = 3
    swsTimeCurveErrorInvalidDataPoints = 4

class swsTimeIntegrationMethod_e(IntEnum):
    """swsTimeIntegrationMethod_e (2 constants, from CosmosWorksLib)."""
    swsTimeIntegrationMethod_Newmark = 0
    swsTimeIntegrationMethod_WilsonTheta = 1

class swsTimeUnits_e(IntEnum):
    """swsTimeUnits_e (4 constants, from CosmosWorksLib)."""
    swsSecond = 0
    swsMinute = 1
    swsHour = 2
    swsDay = 3

class swsTopologyActivationOption_e(IntEnum):
    """swsTopologyActivationOption_e (2 constants, from CosmosWorksLib)."""
    ActivationOption_Deactivate = 0
    ActivationOption_Activate = 1

class swsTopologyDemoldDirectionOption_e(IntEnum):
    """swsTopologyDemoldDirectionOption_e (3 constants, from CosmosWorksLib)."""
    swsTopologyDemoldDirection_TwoDirectionMidPlane = 0
    swsTopologyDemoldDirection_PullDirectionOnly = 1
    swsTopologyDemoldDirection_Stamping = 2

class swsTopologyIterationOption_e(IntEnum):
    """swsTopologyIterationOption_e (2 constants, from CosmosWorksLib)."""
    IterationOption_Auto = 0
    IterationOption_UserDef = 1

class swsTopologyPreservedContactConnectorOption_e(IntEnum):
    """swsTopologyPreservedContactConnectorOption_e (4 constants, from CosmosWorksLib)."""
    PreservedContactConnectorOption_ContactsOnly = 0
    PreservedContactConnectorOption_ConnectorsOnly = 1
    PreservedContactConnectorOption_ContactsAndConnectors = 2
    PreservedContactConnectorOption_None = 3

class swsTopologyPreservedRegionOption_e(IntEnum):
    """swsTopologyPreservedRegionOption_e (4 constants, from CosmosWorksLib)."""
    PreservedRegion_LoadsOnly = 0
    PreservedRegion_FixturesOnly = 1
    PreservedRegion_LoadsAndFixtures = 2
    PreservedRegion_None = 3

class swsTopologyStudyConstraintComparator_e(IntEnum):
    """swsTopologyStudyConstraintComparator_e (3 constants, from CosmosWorksLib)."""
    swsTopologyConstraintComparator_IsLessThan = 0
    swsTopologyConstraintComparator_IsGreaterThan = 1
    swsTopologyConstraintComparator_IsInBetween = 2

class swsTopologyStudyConstraintType_e(IntEnum):
    """swsTopologyStudyConstraintType_e (4 constants, from CosmosWorksLib)."""
    swsTopologyConstraintType_Displacement = 0
    swsTopologyConstraintType_Mass = 1
    swsTopologyConstraintType_Stress = 2
    swsTopologyConstraintType_FactorOfSafety = 3

class swsTopologyStudyConstraintValuationOption_e(IntEnum):
    """swsTopologyStudyConstraintValuationOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyConstraintValuationOption_AbsValue = 0
    swsTopologyConstraintValuationOption_MultiplicationFactor = 1

class swsTopologyStudyDisplacementComponentType_e(IntEnum):
    """swsTopologyStudyDisplacementComponentType_e (7 constants, from CosmosWorksLib)."""
    swsTopologyDisplacementCompType_UX = 0
    swsTopologyDisplacementCompType_UY = 1
    swsTopologyDisplacementCompType_UZ = 2
    swsTopologyDisplacementCompType_URES = 3
    swsTopologyDisplacementCompType_UX_ABS = 4
    swsTopologyDisplacementCompType_UY_ABS = 5
    swsTopologyDisplacementCompType_UZ_ABS = 6

class swsTopologyStudyDisplacementConstraintLocationOption_e(IntEnum):
    """swsTopologyStudyDisplacementConstraintLocationOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyDisplacementConstraintLocationOption_Auto = 0
    swsTopologyDisplacementConstraintLocationOption_UserDefine = 1

class swsTopologyStudyDisplacementConstraintValuationOption_e(IntEnum):
    """swsTopologyStudyDisplacementConstraintValuationOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyDisplacementConstraintValuation_AbsValue = 0
    swsTopologyDisplacementConstraintValuation_MultiplicationFactor = 1

class swsTopologyStudyDisplacementCoordinateSysOption_e(IntEnum):
    """swsTopologyStudyDisplacementCoordinateSysOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyDisplacementCoordinateSysOption_Global = 0
    swsTopologyDisplacementCoordinateSysOption_UserDefine = 1

class swsTopologyStudyError_e(IntEnum):
    """swsTopologyStudyError_e (22 constants, from CosmosWorksLib)."""
    swsTopoErrCode_Success = 0
    swsTopoErrCode_TopologyStudyManagerIsNotInitialized = 1
    swsTopoErrCode_InvalidGoalType = 2
    swsTopoErrCode_NoGoalHasBeenSet = 3
    swsTopoErrCode_MinimizeMassGoalHasNotBeenSet = 4
    swsTopoErrCode_MaximizeStiffnessGoalHasNotBeenSet = 5
    swsTopoErrCode_MinimizeMaximumDisplacementGoalHasNotBeenSet = 6
    swsTopoErrCode_OnlyOneMassConstraintCanBeDefined = 7
    swsTopoErrCode_OnlyOneDisplacementConstraintWithAutoDefineCanBeDefined = 8
    swsTopoErrCode_ConstraintNotFound = 9
    swsTopoErrCode_DefaultConstraintCannotBeRemoved = 10
    swsTopoErrCode_ConstraintDefinitionLimitReached = 11
    swsTopoErrCode_ManufacturingControlNotFound = 12
    swsTopoErrCode_OnlyOneThicknessControlCanBeDefined = 13
    swsTopoErrCode_OnlyOneDemoldControlCanBeDefined = 14
    swsTopoErrCode_OnlyOneSymmetryControlCanBeDefined = 15
    swsTopoErrCode_OnlyOneFrequencyConstraintCanBeDefined = 16
    swsTopoErrCode_SetOperationNotSupported = 17
    swsTopoErrCode_CannotCreatFOSIfStressAlrdyPrsnt = 18
    swsTopoErrCode_CannotCreatStressIfFOSAlrdyPrsnt = 19
    swsTopoErrCode_OnlyOneStressConstraintCanBeDefined = 20
    swsTopoErrCode_OnlyOneFOSConstraintCanBeDefined = 21

class swsTopologyStudyFactorOfSafetyComponentType_e(IntEnum):
    """swsTopologyStudyFactorOfSafetyComponentType_e (1 constants, from CosmosWorksLib)."""
    swsTopologyFactorOfSafetyCompType_MaxVONMises = 0

class swsTopologyStudyGoalType_e(IntEnum):
    """swsTopologyStudyGoalType_e (3 constants, from CosmosWorksLib)."""
    swsTopologyGoalType_MaximizeStiffness = 0
    swsTopologyGoalType_MinimizeMaximumDisplacement = 1
    swsTopologyGoalType_MinimizeMass = 2

class swsTopologyStudyMassConstraintOption_e(IntEnum):
    """swsTopologyStudyMassConstraintOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyMassConstraintOption_AbsoluteValue = 0
    swsTopologyMassConstraintOption_Percentage = 1

class swsTopologyStudyStressComponentType_e(IntEnum):
    """swsTopologyStudyStressComponentType_e (1 constants, from CosmosWorksLib)."""
    swsTopologyStressCompType_VONMises = 0

class swsTopologyStudyStressConstraintValuationOption_e(IntEnum):
    """swsTopologyStudyStressConstraintValuationOption_e (2 constants, from CosmosWorksLib)."""
    swsTopologyStressConstraintValuation_AbsValue = 0
    swsTopologyStressConstraintValuation_Percentage = 1

class swsTopologyStudy_DemoldControlErrors_e(IntEnum):
    """swsTopologyStudy_DemoldControlErrors_e (10 constants, from CosmosWorksLib)."""
    swsTopoDCErrCode_Success = 0
    swsTopoDCErrCode_SetOperationNotSupported = 1
    swsTopoDCErrCode_InvalidEntitySelectedAsEdge = 2
    swsTopoDCErrCode_InvalidDirectionOptionSelected = 3
    swsTopoDCErrCode_InvalidEntitySelectedAsPlane = 4
    swsTopoDCErrCode_NotAvailableForCurrentDirectionOption = 5
    swsTopoDCErrCode_PlaneSelectionNotAvailable = 6
    swsTopoDCErrCode_PlaneSelectionRequired = 7
    swsTopoDCErrCode_EdgeSelectionNotAvailable = 8
    swsTopoDCErrCode_EdgeSelectionRequired = 9

class swsTopologyStudy_DisplacementConstraintErrors_e(IntEnum):
    """swsTopologyStudy_DisplacementConstraintErrors_e (19 constants, from CosmosWorksLib)."""
    swsTopoDispErrCode_Success = 0
    swsTopoDispErrCode_SetOperationNotSupported = 1
    swsTopoDispErrCode_InvalidConstraintValue = 2
    swsTopoDispErrCode_LessThanEqualToZeroConstraintValue = 3
    swsTopoDispErrCode_InvalidComponent = 4
    swsTopoDispErrCode_InvalidConstraintValuationOption = 5
    swsTopoDispErrCode_InvalidUnit = 6
    swsTopoDispErrCode_InvalidComparator = 7
    swsTopoDispErrCode_UnitNotAvailable = 8
    swsTopoDispErrCode_InvalidSelectionForVertex = 9
    swsTopoDispErrCode_CannotSetVertex = 10
    swsTopoDispErrCode_InvalidLocationOption = 11
    swsTopoDispErrCode_InvalidVertexCount = 12
    swsTopoDispErrCode_CoordinateSysNAError = 13
    swsTopoDispErrCode_CoordinateSysInvalidOption = 14
    swsTopoDispErrCode_CoordinateSysInvalidSelection = 15
    swsTopoDispErrCode_CoordinateSysNotSelected = 16
    swsTopoDispErrCode_ConstraintNotFound = 17
    swsTopoDispErrCode_InvalidArray = 18

class swsTopologyStudy_FOSConstraintErrors_e(IntEnum):
    """swsTopologyStudy_FOSConstraintErrors_e (9 constants, from CosmosWorksLib)."""
    swsTopoFOSErrCode_Success = 0
    swsTopoFOSErrCode_SetOperationNotSupported = 1
    swsTopoFOSErrCode_InvalidConstraintValue = 2
    swsTopoFOSErrCode_LessThanEqualToZeroConstraintValue = 3
    swsTopoFOSErrCode_InvalidComponent = 4
    swsTopoFOSErrCode_OutOfRangeValue = 5
    swsTopoFOSErrCode_InvalidComparator = 6
    swsTopoFOSErrCode_ConstraintNotFound = 7
    swsTopoFOSErrCode_MaterialWithInvalidYieldStrength = 8

class swsTopologyStudy_FrequencyConstraintErrors_e(IntEnum):
    """swsTopologyStudy_FrequencyConstraintErrors_e (16 constants, from CosmosWorksLib)."""
    swsTopoFreqErrCode_Success = 0
    swsTopoFreqErrCode_SetOperationNotSupported = 1
    swsTopoFreqErrCode_InvalidConstraintValue = 2
    swsTopoFreqErrCode_LessThanEqualToZeroConstraintValue = 3
    swsTopoFreqErrCode_HMSFreqLessThanLMSFreq = 4
    swsTopoFreqErrCode_ModeShapesNotInAscendingOrder = 5
    swsTopoFreqErrCode_EnterRangeOfValues = 6
    swsTopoFreqErrCode_UnequalSizedArrays = 7
    swsTopoFreqErrCode_InvalidModeShapeData = 8
    swsTopoFreqErrCode_InvalidComparatorData = 9
    swsTopoFreqErrCode_InvalidFreqValuesData = 10
    swsTopoFreqErrCode_ModeShapeDataIsNotSet = 11
    swsTopoFreqErrCode_ComparatorDataIsNotSet = 12
    swsTopoFreqErrCode_FreqValuesDataIsNotSet = 13
    swsTopoFreqErrCode_InvalidArray = 14
    swsTopoFreqErrCode_ConstraintNotFound = 15

class swsTopologyStudy_MassConstraintErrors_e(IntEnum):
    """swsTopologyStudy_MassConstraintErrors_e (9 constants, from CosmosWorksLib)."""
    swsTopoMassErrCode_Success = 0
    swsTopoMassErrCode_SetOperationNotSupported = 1
    swsTopoMassErrCode_InvalidConstraintValue = 2
    swsTopoMassErrCode_LessThanEqualToZeroConstraintValue = 3
    swsTopoMassErrCode_GreaterThan100PercentApplied = 4
    swsTopoMassErrCode_GreaterThanTotalMassOfModel = 5
    swsTopoMassErrCode_InvalidUnit = 6
    swsTopoMassErrCode_InvalidPreferenceOption = 7
    swsTopoMassErrCode_ConstraintNotFound = 8

class swsTopologyStudy_MinMaxDisplacementGoalErrors_e(IntEnum):
    """swsTopologyStudy_MinMaxDisplacementGoalErrors_e (10 constants, from CosmosWorksLib)."""
    swsTopoDGErrCode_Success = 0
    swsTopoDGErrCode_SetOperationNotSupported = 1
    swsTopoDGErrCode_InvalidComponent = 2
    swsTopoDGErrCode_CoordinateSysNAError = 3
    swsTopoDGErrCode_CoordinateSysInvalidOption = 4
    swsTopoDGErrCode_CoordinateSysInvalidSelection = 5
    swsTopoDGErrCode_CoordinateSysNotSelected = 6
    swsTopoDGErrCode_InvalidVertexCount = 7
    swsTopoDGErrCode_InvalidArray = 8
    swsTopoDGErrCode_InvalidEntities = 9

class swsTopologyStudy_PreservedRegionErrors_e(IntEnum):
    """swsTopologyStudy_PreservedRegionErrors_e (7 constants, from CosmosWorksLib)."""
    swsTopoPRErrCode_Success = 0
    swsTopoPRErrCode_SetOperationNotSupported = 1
    swsTopoPRErrCode_InvalidFaceCount = 2
    swsTopoPRErrCode_InvalidAreaDepth = 3
    swsTopoPRErrCode_InvalidAreaDepthUnit = 4
    swsTopoPRErrCode_InvalidArray = 5
    swsTopoPRErrCode_InvalidEntities = 6

class swsTopologyStudy_StressConstraintErrors_e(IntEnum):
    """swsTopologyStudy_StressConstraintErrors_e (12 constants, from CosmosWorksLib)."""
    swsTopoStressErrCode_Success = 0
    swsTopoStressErrCode_SetOperationNotSupported = 1
    swsTopoStressErrCode_InvalidConstraintValue = 2
    swsTopoStressErrCode_LessThanEqualToZeroConstraintValue = 3
    swsTopoStressErrCode_InvalidComponent = 4
    swsTopoStressErrCode_InvalidConstraintValuationOption = 5
    swsTopoStressErrCode_InvalidUnit = 6
    swsTopoStressErrCode_InvalidComparator = 7
    swsTopoStressErrCode_UnitNotAvailable = 8
    swsTopoStressErrCode_LessThanPermittedValue = 9
    swsTopoStressErrCode_ConstraintNotFound = 10
    swsTopoStressErrCode_OutOfRangePercentageValue = 11

class swsTopologyStudy_SymmetryControlErrors_e(IntEnum):
    """swsTopologyStudy_SymmetryControlErrors_e (6 constants, from CosmosWorksLib)."""
    swsTopoSCErrCode_Success = 0
    swsTopoSCErrCode_SetOperationNotSupported = 1
    swsTopoSCErrCode_InvalidEntitySelectedAsPlane = 2
    swsTopoSCErrCode_InvalidTypeSelected = 3
    swsTopoSCErrCode_IncorrectPlaneSelectionsForGivenSymmetryType = 4
    swsTopoSCErrCode_SetSymmetryTypeBeforeSelectingPlane = 5

class swsTopologyStudy_ThicknessControlErrors_e(IntEnum):
    """swsTopologyStudy_ThicknessControlErrors_e (4 constants, from CosmosWorksLib)."""
    swsTopoTCErrCode_Success = 0
    swsTopoTCErrCode_SetOperationNotSupported = 1
    swsTopoTCErrCode_InvalidThickness = 2
    swsTopoTCErrCode_InvalidThicknessUnit = 3

class swsTopologySymmetryControlOption_e(IntEnum):
    """swsTopologySymmetryControlOption_e (3 constants, from CosmosWorksLib)."""
    swsTopologySymmetryControlType_HalfSymmetry = 0
    swsTopologySymmetryControlType_QuarterSymmetry = 1
    swsTopologySymmetryControlType_OneEighthSymmetry = 2

class swsTrendTrackerErrorCode_e(IntEnum):
    """swsTrendTrackerErrorCode_e (5 constants, from CosmosWorksLib)."""
    swsTrendTracker_NoError = 0
    swsTrendTracker_InvalidStudyType = 1
    swsTrendTracker_InvalidTrendTrackerObj = 2
    swsTrendTracker_FailedCreation = 3
    swsTrendTracker_SetBaseLineActionFailed = 4

class swsUnitSystem_e(IntEnum):
    """swsUnitSystem_e (4 constants, from CosmosWorksLib)."""
    swsUnitSystemSI = 0
    swsUnitSystemIPS = 1
    swsUnitSystemMKS = 2
    swsUnitSystemSIWithMPA = 3

class swsUnit_e(IntEnum):
    """swsUnit_e (3 constants, from CosmosWorksLib)."""
    swsUnitSI = 0
    swsUnitEnglish = 1
    swsUnitMetric = 2

class swsUserPreferenceDoubleValue_e(IntEnum):
    """swsUserPreferenceDoubleValue_e (5 constants, from CosmosWorksLib)."""
    swsPlotShowHiddenBodyTransparency = 0
    swsPlotShowExcludedBodyTransparency = 1
    swsPlotDeformedShapeSuperImposeModelTranslucentTransparency = 2
    swsPlotBeamDiagramTransparency = 3
    swsPlotBoundaryTransparency = 4

class swsUserPreferenceIntegerValue_e(IntEnum):
    """swsUserPreferenceIntegerValue_e (32 constants, from CosmosWorksLib)."""
    swsDefaultSolverValue = 0
    swsDefaultResultFolder = 1
    swsReportPublishOption = 2
    swsColorChartPosition = 3
    swsPlotSettingsFringeOption = 4
    swsPlotSettingsBoundaryOption = 5
    swsPlotShowExcludedBodiesOption = 6
    swsPlotShowHiddenBodiesOption = 7
    swsPlotBoundaryOptionTranslucentSingleColorSetting = 8
    swsPlotBoundaryOptionMeshColor = 9
    swsPlotShowExcludedBodyTranslucentSingleColor = 10
    swsPlotShowHiddenBodyTranslucentSingleColor = 11
    swsPlotDeformedShapeOptionSetting = 12
    swsPlotDeformedShapeResultScaleContact = 13
    swsPlotDeformedShapeResultScaleLarge = 14
    swsPlotDeformedShapeResultOther = 15
    swsPlotDeformedShapeOptionSetSuperImposeOption = 16
    swsReportPublishOptionReportFolderUserDefinedPath = 17
    swsColorChartPositionUserDefinedXValue = 18
    swsColorChartPositionUserDefinedYValue = 19
    swsColorChartWidthOption = 20
    swsColorChartNumberFormatOption = 21
    swsColorChartColorOptionChartColorNumber = 22
    swsColorChartColorOptionBaseChartColorNumber = 23
    swsColorChartColorOptionLegendType = 24
    swsColorChartNumberFormatLegendPrecision = 25
    swsColorChartNumberFormatUseDiffNoFormatOption = 26
    swsColorChartColorOptionvonMisesColorValue = 27
    swsPlotDeformedShapeOptionTranslucentColor = 28
    swsPlotBoundaryOptionModelColor = 29
    swsEMailType = 30
    swsMesherType = 31

class swsUserPreferenceStringValue_e(IntEnum):
    """swsUserPreferenceStringValue_e (9 constants, from CosmosWorksLib)."""
    swsUserDefinedResultFolderLocation = 0
    swsSolidWorksDocumentFolderSubFolderLocation = 1
    swsSolidWorksUserDefinedReportFolderLocation = 2
    swsEMailSendFrom = 3
    swsEMailSendTo = 4
    swsEMailSMTP = 5
    swsEMailPort = 6
    swsEMailAccount = 7
    swsEMailPassword = 8

class swsUserPreferenceToggle_e(IntEnum):
    """swsUserPreferenceToggle_e (22 constants, from CosmosWorksLib)."""
    swsResultFolderUnderSubFolder = 0
    swsResultFolderKeepTempDataBase = 1
    swsTrendTrackerBackUpModelsRestoreIteration = 2
    swsShowReportOnPublish = 3
    swsPlotAnnotationShowMinValue = 4
    swsPlotAnnotationShowMaxValue = 5
    swsPlotAnnotationShowRangeBasedOnShowCompOnly = 6
    swsPlotShowExcludedBodies = 7
    swsPlotShowHiddenBodies = 8
    swsPlotDeformedShapeOptionSuperImposeModelOnDeformedShape = 9
    swsColorChartDisplay = 10
    swsColorChartDetails = 11
    swsColorChartNumberFormatUseDifferentNumberFormat = 12
    swsColorChartColorNoOfChartColorFlip = 13
    swsColorChartColorSpecifyColorForvonMisesPlot = 14
    swsLoadAllStudies_e = 15
    swsEMailAuthentication = 16
    swsAverageStressesAtMidnodes = 17
    swsEnforceSaveAfterMeshAndAfterSolve = 18
    swsIncludeMeshInCopyStudy = 19
    swsIncludeResultsInCopyStudy = 20
    swsAutomaticallyDetectUnderConstrainedBodies = 21

class swsVelocityComponent_e(IntEnum):
    """swsVelocityComponent_e (8 constants, from CosmosWorksLib)."""
    swsVelocityComponentVX = 0
    swsVelocityComponentVY = 1
    swsVelocityComponentVZ = 2
    swsVelocityComponentVRES = 3
    swsVelocityComponentAVX = 4
    swsVelocityComponentAVY = 5
    swsVelocityComponentAVZ = 6
    swsVelocityComponentAVRES = 7

class swsVelocityUnit_e(IntEnum):
    """swsVelocityUnit_e (4 constants, from CosmosWorksLib)."""
    swsVelocityUnit_MillimetersPerSec = 0
    swsVelocityUnit_CentimetersPerSec = 1
    swsVelocityUnit_MetersPerSec = 2
    swsVelocityUnit_InchesPerSec = 3

class swsWallType_e(IntEnum):
    """swsWallType_e (2 constants, from CosmosWorksLib)."""
    swsWallTypeRigid = 0
    swsWallTypeFlexible = 1

class swsWeakMaterial_e(IntEnum):
    """swsWeakMaterial_e (3 constants, from CosmosWorksLib)."""
    swsWeakMaterialCustom = 0
    swsWeakMaterialFirstFaceMaterial = 1
    swsWeakMaterialSecondFaceMaterial = 2

class swsWeldResultErrorCode_e(IntEnum):
    """swsWeldResultErrorCode_e (8 constants, from CosmosWorksLib)."""
    swsWeldResult_NoError = 0
    swsWeldResult_NoView = 1
    swsWeldResult_InvalidUnit = 2
    swsWeldResult_ResultsNotAvailable = 3
    swsWeldResult_InvalidConnectorName = 4
    swsWeldResult_NoPersistID = 5
    swsWeldResult_MeshDataNotAvailable = 6
    swsWeldResult_NodeIndexListUnAvailable = 7

class swsWeldStrengthUnits_e(IntEnum):
    """swsWeldStrengthUnits_e (5 constants, from CosmosWorksLib)."""
    swsWeldStrengthUnits_NewtonOverMeterSquare = 0
    swsWeldStrengthUnits_PSI = 1
    swsWeldStrengthUnits_KgfOverCentimeterSquare = 2
    swsWeldStrengthUnits_MPa = 3
    swsWeldStrengthUnits_KSI = 4

class swsWindowsBasicColors_e(IntEnum):
    """swsWindowsBasicColors_e (47 constants, from CosmosWorksLib)."""
    swsLightRed = 8421631
    swsLightYellow = 8454143
    swsPaleGreen = 8454016
    swsSpringGreen = 8453888
    swsCyan = 16777088
    swsDodgerBlue = 16744448
    swsPlum = 12615935
    swsViolet = 16744703
    swsRed = 255
    swsYellow = 65535
    swsGreenYellow = 65408
    swsLawnGreen = 4259584
    swsAqua = 16776960
    swsDeepSkyBlue = 12615680
    swsMediumPurple = 12615808
    swsMagenta = 16711935
    swsLightSalmon = 4210816
    swsCoral = 4227327
    swsLime = 65280
    swsTeal = 8421376
    swsRoyalBlue = 8404992
    swsSgiSlateBlue = 16744576
    swsDarkRed = 4194432
    swsSgiSalmon = 8388863
    swsMaroon = 128
    swsOrange = 33023
    swsGreen = 32768
    swsSapGreen = 4227072
    swsBlue = 16711680
    swsMidnightBlue = 10485760
    swsPurple = 8388736
    swsSgiBeet = 16711808
    swsDeepGray = 64
    swsTan = 16512
    swsDarkOliveGreen = 16384
    swsDarkGreen = 4210688
    swsNavy = 8388608
    swsDarkBlue = 4194304
    swsDarkPurple = 4194368
    swsIndigo = 8388672
    swsBlack = 0
    swsOlive = 32896
    swsKhaki = 4227200
    swsGray = 8421504
    swsLightSeaGreen = 8421440
    swsSilver = 12632256
    swsWhite = 16777215

