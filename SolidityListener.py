# Generated from Solidity.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SolidityParser import SolidityParser
else:
    from SolidityParser import SolidityParser

# This class defines a complete listener for a parse tree produced by SolidityParser.
class SolidityListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityParser#sourceUnit.
    def enterSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#sourceUnit.
    def exitSourceUnit(self, ctx:SolidityParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#timestamp.
    def enterTimestamp(self, ctx:SolidityParser.TimestampContext):
        pass

    # Exit a parse tree produced by SolidityParser#timestamp.
    def exitTimestamp(self, ctx:SolidityParser.TimestampContext):
        pass


    # Enter a parse tree produced by SolidityParser#unit.
    def enterUnit(self, ctx:SolidityParser.UnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#unit.
    def exitUnit(self, ctx:SolidityParser.UnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#reentrancyAnnotation.
    def enterReentrancyAnnotation(self, ctx:SolidityParser.ReentrancyAnnotationContext):
        pass

    # Exit a parse tree produced by SolidityParser#reentrancyAnnotation.
    def exitReentrancyAnnotation(self, ctx:SolidityParser.ReentrancyAnnotationContext):
        pass


    # Enter a parse tree produced by SolidityParser#reentrancyType.
    def enterReentrancyType(self, ctx:SolidityParser.ReentrancyTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#reentrancyType.
    def exitReentrancyType(self, ctx:SolidityParser.ReentrancyTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:SolidityParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:SolidityParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaSolidity.
    def enterPragmaSolidity(self, ctx:SolidityParser.PragmaSolidityContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaSolidity.
    def exitPragmaSolidity(self, ctx:SolidityParser.PragmaSolidityContext):
        pass


    # Enter a parse tree produced by SolidityParser#pragmaExperimental.
    def enterPragmaExperimental(self, ctx:SolidityParser.PragmaExperimentalContext):
        pass

    # Exit a parse tree produced by SolidityParser#pragmaExperimental.
    def exitPragmaExperimental(self, ctx:SolidityParser.PragmaExperimentalContext):
        pass


    # Enter a parse tree produced by SolidityParser#version.
    def enterVersion(self, ctx:SolidityParser.VersionContext):
        pass

    # Exit a parse tree produced by SolidityParser#version.
    def exitVersion(self, ctx:SolidityParser.VersionContext):
        pass


    # Enter a parse tree produced by SolidityParser#versionOperator.
    def enterVersionOperator(self, ctx:SolidityParser.VersionOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#versionOperator.
    def exitVersionOperator(self, ctx:SolidityParser.VersionOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#importDirective.
    def enterImportDirective(self, ctx:SolidityParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityParser#importDirective.
    def exitImportDirective(self, ctx:SolidityParser.ImportDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityParser#importDeclaration.
    def enterImportDeclaration(self, ctx:SolidityParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#importDeclaration.
    def exitImportDeclaration(self, ctx:SolidityParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractDefinition.
    def enterContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractDefinition.
    def exitContractDefinition(self, ctx:SolidityParser.ContractDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#libraryDefinition.
    def enterLibraryDefinition(self, ctx:SolidityParser.LibraryDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#libraryDefinition.
    def exitLibraryDefinition(self, ctx:SolidityParser.LibraryDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#interfaceDefinition.
    def enterInterfaceDefinition(self, ctx:SolidityParser.InterfaceDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#interfaceDefinition.
    def exitInterfaceDefinition(self, ctx:SolidityParser.InterfaceDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#inheritanceSpecifier.
    def enterInheritanceSpecifier(self, ctx:SolidityParser.InheritanceSpecifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#inheritanceSpecifier.
    def exitInheritanceSpecifier(self, ctx:SolidityParser.InheritanceSpecifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#contractPartDefinition.
    def enterContractPartDefinition(self, ctx:SolidityParser.ContractPartDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#contractPartDefinition.
    def exitContractPartDefinition(self, ctx:SolidityParser.ContractPartDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#usingForDeclaration.
    def enterUsingForDeclaration(self, ctx:SolidityParser.UsingForDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#usingForDeclaration.
    def exitUsingForDeclaration(self, ctx:SolidityParser.UsingForDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#structDefinition.
    def enterStructDefinition(self, ctx:SolidityParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#structDefinition.
    def exitStructDefinition(self, ctx:SolidityParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#modifierDefinition.
    def enterModifierDefinition(self, ctx:SolidityParser.ModifierDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#modifierDefinition.
    def exitModifierDefinition(self, ctx:SolidityParser.ModifierDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SolidityParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SolidityParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#returnsParameters.
    def enterReturnsParameters(self, ctx:SolidityParser.ReturnsParametersContext):
        pass

    # Exit a parse tree produced by SolidityParser#returnsParameters.
    def exitReturnsParameters(self, ctx:SolidityParser.ReturnsParametersContext):
        pass


    # Enter a parse tree produced by SolidityParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SolidityParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SolidityParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateVariableDeclaration.
    def enterStateVariableDeclaration(self, ctx:SolidityParser.StateVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateVariableDeclaration.
    def exitStateVariableDeclaration(self, ctx:SolidityParser.StateVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionFallBackDefinition.
    def enterFunctionFallBackDefinition(self, ctx:SolidityParser.FunctionFallBackDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionFallBackDefinition.
    def exitFunctionFallBackDefinition(self, ctx:SolidityParser.FunctionFallBackDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#inheritance.
    def enterInheritance(self, ctx:SolidityParser.InheritanceContext):
        pass

    # Exit a parse tree produced by SolidityParser#inheritance.
    def exitInheritance(self, ctx:SolidityParser.InheritanceContext):
        pass


    # Enter a parse tree produced by SolidityParser#eventDefinition.
    def enterEventDefinition(self, ctx:SolidityParser.EventDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#eventDefinition.
    def exitEventDefinition(self, ctx:SolidityParser.EventDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumDefinition.
    def enterEnumDefinition(self, ctx:SolidityParser.EnumDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumDefinition.
    def exitEnumDefinition(self, ctx:SolidityParser.EnumDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#environmentalVariable.
    def enterEnvironmentalVariable(self, ctx:SolidityParser.EnvironmentalVariableContext):
        pass

    # Exit a parse tree produced by SolidityParser#environmentalVariable.
    def exitEnvironmentalVariable(self, ctx:SolidityParser.EnvironmentalVariableContext):
        pass


    # Enter a parse tree produced by SolidityParser#visibleType.
    def enterVisibleType(self, ctx:SolidityParser.VisibleTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#visibleType.
    def exitVisibleType(self, ctx:SolidityParser.VisibleTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#constantType.
    def enterConstantType(self, ctx:SolidityParser.ConstantTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#constantType.
    def exitConstantType(self, ctx:SolidityParser.ConstantTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#payableType.
    def enterPayableType(self, ctx:SolidityParser.PayableTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#payableType.
    def exitPayableType(self, ctx:SolidityParser.PayableTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#typeName.
    def enterTypeName(self, ctx:SolidityParser.TypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#typeName.
    def exitTypeName(self, ctx:SolidityParser.TypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#userDefinedTypeName.
    def enterUserDefinedTypeName(self, ctx:SolidityParser.UserDefinedTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#userDefinedTypeName.
    def exitUserDefinedTypeName(self, ctx:SolidityParser.UserDefinedTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionTypeName.
    def enterFunctionTypeName(self, ctx:SolidityParser.FunctionTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionTypeName.
    def exitFunctionTypeName(self, ctx:SolidityParser.FunctionTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#stateMutability.
    def enterStateMutability(self, ctx:SolidityParser.StateMutabilityContext):
        pass

    # Exit a parse tree produced by SolidityParser#stateMutability.
    def exitStateMutability(self, ctx:SolidityParser.StateMutabilityContext):
        pass


    # Enter a parse tree produced by SolidityParser#pureType.
    def enterPureType(self, ctx:SolidityParser.PureTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#pureType.
    def exitPureType(self, ctx:SolidityParser.PureTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#viewType.
    def enterViewType(self, ctx:SolidityParser.ViewTypeContext):
        pass

    # Exit a parse tree produced by SolidityParser#viewType.
    def exitViewType(self, ctx:SolidityParser.ViewTypeContext):
        pass


    # Enter a parse tree produced by SolidityParser#mappingSt.
    def enterMappingSt(self, ctx:SolidityParser.MappingStContext):
        pass

    # Exit a parse tree produced by SolidityParser#mappingSt.
    def exitMappingSt(self, ctx:SolidityParser.MappingStContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionCall.
    def enterFunctionCall(self, ctx:SolidityParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionCall.
    def exitFunctionCall(self, ctx:SolidityParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SolidityParser#functionName.
    def enterFunctionName(self, ctx:SolidityParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#functionName.
    def exitFunctionName(self, ctx:SolidityParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#newConrtact.
    def enterNewConrtact(self, ctx:SolidityParser.NewConrtactContext):
        pass

    # Exit a parse tree produced by SolidityParser#newConrtact.
    def exitNewConrtact(self, ctx:SolidityParser.NewConrtactContext):
        pass


    # Enter a parse tree produced by SolidityParser#value.
    def enterValue(self, ctx:SolidityParser.ValueContext):
        pass

    # Exit a parse tree produced by SolidityParser#value.
    def exitValue(self, ctx:SolidityParser.ValueContext):
        pass


    # Enter a parse tree produced by SolidityParser#gas.
    def enterGas(self, ctx:SolidityParser.GasContext):
        pass

    # Exit a parse tree produced by SolidityParser#gas.
    def exitGas(self, ctx:SolidityParser.GasContext):
        pass


    # Enter a parse tree produced by SolidityParser#plusminusOperator.
    def enterPlusminusOperator(self, ctx:SolidityParser.PlusminusOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#plusminusOperator.
    def exitPlusminusOperator(self, ctx:SolidityParser.PlusminusOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#minusOperator.
    def enterMinusOperator(self, ctx:SolidityParser.MinusOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#minusOperator.
    def exitMinusOperator(self, ctx:SolidityParser.MinusOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#plusOperator.
    def enterPlusOperator(self, ctx:SolidityParser.PlusOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#plusOperator.
    def exitPlusOperator(self, ctx:SolidityParser.PlusOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#twoPlusMinusOperator.
    def enterTwoPlusMinusOperator(self, ctx:SolidityParser.TwoPlusMinusOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#twoPlusMinusOperator.
    def exitTwoPlusMinusOperator(self, ctx:SolidityParser.TwoPlusMinusOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#decrementOperator.
    def enterDecrementOperator(self, ctx:SolidityParser.DecrementOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#decrementOperator.
    def exitDecrementOperator(self, ctx:SolidityParser.DecrementOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#incrementOperator.
    def enterIncrementOperator(self, ctx:SolidityParser.IncrementOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#incrementOperator.
    def exitIncrementOperator(self, ctx:SolidityParser.IncrementOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#muldivOperator.
    def enterMuldivOperator(self, ctx:SolidityParser.MuldivOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#muldivOperator.
    def exitMuldivOperator(self, ctx:SolidityParser.MuldivOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#divRemOperator.
    def enterDivRemOperator(self, ctx:SolidityParser.DivRemOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#divRemOperator.
    def exitDivRemOperator(self, ctx:SolidityParser.DivRemOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#powerOperator.
    def enterPowerOperator(self, ctx:SolidityParser.PowerOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#powerOperator.
    def exitPowerOperator(self, ctx:SolidityParser.PowerOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#mulOperator.
    def enterMulOperator(self, ctx:SolidityParser.MulOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#mulOperator.
    def exitMulOperator(self, ctx:SolidityParser.MulOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#divOperator.
    def enterDivOperator(self, ctx:SolidityParser.DivOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#divOperator.
    def exitDivOperator(self, ctx:SolidityParser.DivOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#callArguments.
    def enterCallArguments(self, ctx:SolidityParser.CallArgumentsContext):
        pass

    # Exit a parse tree produced by SolidityParser#callArguments.
    def exitCallArguments(self, ctx:SolidityParser.CallArgumentsContext):
        pass


    # Enter a parse tree produced by SolidityParser#typeConversion.
    def enterTypeConversion(self, ctx:SolidityParser.TypeConversionContext):
        pass

    # Exit a parse tree produced by SolidityParser#typeConversion.
    def exitTypeConversion(self, ctx:SolidityParser.TypeConversionContext):
        pass


    # Enter a parse tree produced by SolidityParser#typeExpression.
    def enterTypeExpression(self, ctx:SolidityParser.TypeExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#typeExpression.
    def exitTypeExpression(self, ctx:SolidityParser.TypeExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#expression.
    def enterExpression(self, ctx:SolidityParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#expression.
    def exitExpression(self, ctx:SolidityParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#arrayRange.
    def enterArrayRange(self, ctx:SolidityParser.ArrayRangeContext):
        pass

    # Exit a parse tree produced by SolidityParser#arrayRange.
    def exitArrayRange(self, ctx:SolidityParser.ArrayRangeContext):
        pass


    # Enter a parse tree produced by SolidityParser#newDynamicArray.
    def enterNewDynamicArray(self, ctx:SolidityParser.NewDynamicArrayContext):
        pass

    # Exit a parse tree produced by SolidityParser#newDynamicArray.
    def exitNewDynamicArray(self, ctx:SolidityParser.NewDynamicArrayContext):
        pass


    # Enter a parse tree produced by SolidityParser#lvalueOperator.
    def enterLvalueOperator(self, ctx:SolidityParser.LvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#lvalueOperator.
    def exitLvalueOperator(self, ctx:SolidityParser.LvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#plusLvalueOperator.
    def enterPlusLvalueOperator(self, ctx:SolidityParser.PlusLvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#plusLvalueOperator.
    def exitPlusLvalueOperator(self, ctx:SolidityParser.PlusLvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#minusLvalueOperator.
    def enterMinusLvalueOperator(self, ctx:SolidityParser.MinusLvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#minusLvalueOperator.
    def exitMinusLvalueOperator(self, ctx:SolidityParser.MinusLvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#divLvalueOperator.
    def enterDivLvalueOperator(self, ctx:SolidityParser.DivLvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#divLvalueOperator.
    def exitDivLvalueOperator(self, ctx:SolidityParser.DivLvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#mulLvalueOperator.
    def enterMulLvalueOperator(self, ctx:SolidityParser.MulLvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#mulLvalueOperator.
    def exitMulLvalueOperator(self, ctx:SolidityParser.MulLvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#divRemLvalueOperator.
    def enterDivRemLvalueOperator(self, ctx:SolidityParser.DivRemLvalueOperatorContext):
        pass

    # Exit a parse tree produced by SolidityParser#divRemLvalueOperator.
    def exitDivRemLvalueOperator(self, ctx:SolidityParser.DivRemLvalueOperatorContext):
        pass


    # Enter a parse tree produced by SolidityParser#enumValue.
    def enterEnumValue(self, ctx:SolidityParser.EnumValueContext):
        pass

    # Exit a parse tree produced by SolidityParser#enumValue.
    def exitEnumValue(self, ctx:SolidityParser.EnumValueContext):
        pass


    # Enter a parse tree produced by SolidityParser#indexedParameterList.
    def enterIndexedParameterList(self, ctx:SolidityParser.IndexedParameterListContext):
        pass

    # Exit a parse tree produced by SolidityParser#indexedParameterList.
    def exitIndexedParameterList(self, ctx:SolidityParser.IndexedParameterListContext):
        pass


    # Enter a parse tree produced by SolidityParser#indexedParameter.
    def enterIndexedParameter(self, ctx:SolidityParser.IndexedParameterContext):
        pass

    # Exit a parse tree produced by SolidityParser#indexedParameter.
    def exitIndexedParameter(self, ctx:SolidityParser.IndexedParameterContext):
        pass


    # Enter a parse tree produced by SolidityParser#parameterList.
    def enterParameterList(self, ctx:SolidityParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SolidityParser#parameterList.
    def exitParameterList(self, ctx:SolidityParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SolidityParser#parameter.
    def enterParameter(self, ctx:SolidityParser.ParameterContext):
        pass

    # Exit a parse tree produced by SolidityParser#parameter.
    def exitParameter(self, ctx:SolidityParser.ParameterContext):
        pass


    # Enter a parse tree produced by SolidityParser#storageLocation.
    def enterStorageLocation(self, ctx:SolidityParser.StorageLocationContext):
        pass

    # Exit a parse tree produced by SolidityParser#storageLocation.
    def exitStorageLocation(self, ctx:SolidityParser.StorageLocationContext):
        pass


    # Enter a parse tree produced by SolidityParser#block.
    def enterBlock(self, ctx:SolidityParser.BlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#block.
    def exitBlock(self, ctx:SolidityParser.BlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#statement.
    def enterStatement(self, ctx:SolidityParser.StatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#statement.
    def exitStatement(self, ctx:SolidityParser.StatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#uncheckedBlock.
    def enterUncheckedBlock(self, ctx:SolidityParser.UncheckedBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#uncheckedBlock.
    def exitUncheckedBlock(self, ctx:SolidityParser.UncheckedBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#tryCatchStatement.
    def enterTryCatchStatement(self, ctx:SolidityParser.TryCatchStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#tryCatchStatement.
    def exitTryCatchStatement(self, ctx:SolidityParser.TryCatchStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#emitEventStatement.
    def enterEmitEventStatement(self, ctx:SolidityParser.EmitEventStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#emitEventStatement.
    def exitEmitEventStatement(self, ctx:SolidityParser.EmitEventStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#ifStatement.
    def enterIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#ifStatement.
    def exitIfStatement(self, ctx:SolidityParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#whileStatement.
    def enterWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#whileStatement.
    def exitWhileStatement(self, ctx:SolidityParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#forStatement.
    def enterForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#forStatement.
    def exitForStatement(self, ctx:SolidityParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#inlineAssemblyStatement.
    def enterInlineAssemblyStatement(self, ctx:SolidityParser.InlineAssemblyStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#inlineAssemblyStatement.
    def exitInlineAssemblyStatement(self, ctx:SolidityParser.InlineAssemblyStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SolidityParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#condition.
    def enterCondition(self, ctx:SolidityParser.ConditionContext):
        pass

    # Exit a parse tree produced by SolidityParser#condition.
    def exitCondition(self, ctx:SolidityParser.ConditionContext):
        pass


    # Enter a parse tree produced by SolidityParser#placeholderStatement.
    def enterPlaceholderStatement(self, ctx:SolidityParser.PlaceholderStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#placeholderStatement.
    def exitPlaceholderStatement(self, ctx:SolidityParser.PlaceholderStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#continueStatement.
    def enterContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#continueStatement.
    def exitContinueStatement(self, ctx:SolidityParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#breakStatement.
    def enterBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#breakStatement.
    def exitBreakStatement(self, ctx:SolidityParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#deleteStatement.
    def enterDeleteStatement(self, ctx:SolidityParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#deleteStatement.
    def exitDeleteStatement(self, ctx:SolidityParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#returnStatement.
    def enterReturnStatement(self, ctx:SolidityParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#returnStatement.
    def exitReturnStatement(self, ctx:SolidityParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#throwRevertStatement.
    def enterThrowRevertStatement(self, ctx:SolidityParser.ThrowRevertStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#throwRevertStatement.
    def exitThrowRevertStatement(self, ctx:SolidityParser.ThrowRevertStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SolidityParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SolidityParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SolidityParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SolidityParser#varDeclaration.
    def enterVarDeclaration(self, ctx:SolidityParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityParser#varDeclaration.
    def exitVarDeclaration(self, ctx:SolidityParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityParser#inlineAssemblyBlock.
    def enterInlineAssemblyBlock(self, ctx:SolidityParser.InlineAssemblyBlockContext):
        pass

    # Exit a parse tree produced by SolidityParser#inlineAssemblyBlock.
    def exitInlineAssemblyBlock(self, ctx:SolidityParser.InlineAssemblyBlockContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyItem.
    def enterAssemblyItem(self, ctx:SolidityParser.AssemblyItemContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyItem.
    def exitAssemblyItem(self, ctx:SolidityParser.AssemblyItemContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyExpression.
    def enterAssemblyExpression(self, ctx:SolidityParser.AssemblyExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyExpression.
    def exitAssemblyExpression(self, ctx:SolidityParser.AssemblyExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyCall.
    def enterAssemblyCall(self, ctx:SolidityParser.AssemblyCallContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyCall.
    def exitAssemblyCall(self, ctx:SolidityParser.AssemblyCallContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyLocalDefinition.
    def enterAssemblyLocalDefinition(self, ctx:SolidityParser.AssemblyLocalDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyLocalDefinition.
    def exitAssemblyLocalDefinition(self, ctx:SolidityParser.AssemblyLocalDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyAssignment.
    def enterAssemblyAssignment(self, ctx:SolidityParser.AssemblyAssignmentContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyAssignment.
    def exitAssemblyAssignment(self, ctx:SolidityParser.AssemblyAssignmentContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyIdentifierOrList.
    def enterAssemblyIdentifierOrList(self, ctx:SolidityParser.AssemblyIdentifierOrListContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyIdentifierOrList.
    def exitAssemblyIdentifierOrList(self, ctx:SolidityParser.AssemblyIdentifierOrListContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyIdentifierList.
    def enterAssemblyIdentifierList(self, ctx:SolidityParser.AssemblyIdentifierListContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyIdentifierList.
    def exitAssemblyIdentifierList(self, ctx:SolidityParser.AssemblyIdentifierListContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyStackAssignment.
    def enterAssemblyStackAssignment(self, ctx:SolidityParser.AssemblyStackAssignmentContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyStackAssignment.
    def exitAssemblyStackAssignment(self, ctx:SolidityParser.AssemblyStackAssignmentContext):
        pass


    # Enter a parse tree produced by SolidityParser#labelDefinition.
    def enterLabelDefinition(self, ctx:SolidityParser.LabelDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#labelDefinition.
    def exitLabelDefinition(self, ctx:SolidityParser.LabelDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblySwitch.
    def enterAssemblySwitch(self, ctx:SolidityParser.AssemblySwitchContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblySwitch.
    def exitAssemblySwitch(self, ctx:SolidityParser.AssemblySwitchContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyCase.
    def enterAssemblyCase(self, ctx:SolidityParser.AssemblyCaseContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyCase.
    def exitAssemblyCase(self, ctx:SolidityParser.AssemblyCaseContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyFunctionDefinition.
    def enterAssemblyFunctionDefinition(self, ctx:SolidityParser.AssemblyFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyFunctionDefinition.
    def exitAssemblyFunctionDefinition(self, ctx:SolidityParser.AssemblyFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyFunctionReturns.
    def enterAssemblyFunctionReturns(self, ctx:SolidityParser.AssemblyFunctionReturnsContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyFunctionReturns.
    def exitAssemblyFunctionReturns(self, ctx:SolidityParser.AssemblyFunctionReturnsContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyFor.
    def enterAssemblyFor(self, ctx:SolidityParser.AssemblyForContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyFor.
    def exitAssemblyFor(self, ctx:SolidityParser.AssemblyForContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyIf.
    def enterAssemblyIf(self, ctx:SolidityParser.AssemblyIfContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyIf.
    def exitAssemblyIf(self, ctx:SolidityParser.AssemblyIfContext):
        pass


    # Enter a parse tree produced by SolidityParser#assemblyLiteral.
    def enterAssemblyLiteral(self, ctx:SolidityParser.AssemblyLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#assemblyLiteral.
    def exitAssemblyLiteral(self, ctx:SolidityParser.AssemblyLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#subAssembly.
    def enterSubAssembly(self, ctx:SolidityParser.SubAssemblyContext):
        pass

    # Exit a parse tree produced by SolidityParser#subAssembly.
    def exitSubAssembly(self, ctx:SolidityParser.SubAssemblyContext):
        pass


    # Enter a parse tree produced by SolidityParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SolidityParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SolidityParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#tupleExpression.
    def enterTupleExpression(self, ctx:SolidityParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by SolidityParser#tupleExpression.
    def exitTupleExpression(self, ctx:SolidityParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by SolidityParser#nameValueList.
    def enterNameValueList(self, ctx:SolidityParser.NameValueListContext):
        pass

    # Exit a parse tree produced by SolidityParser#nameValueList.
    def exitNameValueList(self, ctx:SolidityParser.NameValueListContext):
        pass


    # Enter a parse tree produced by SolidityParser#comparison.
    def enterComparison(self, ctx:SolidityParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SolidityParser#comparison.
    def exitComparison(self, ctx:SolidityParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SolidityParser#identifier.
    def enterIdentifier(self, ctx:SolidityParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SolidityParser#identifier.
    def exitIdentifier(self, ctx:SolidityParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SolidityParser#elementaryTypeName.
    def enterElementaryTypeName(self, ctx:SolidityParser.ElementaryTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityParser#elementaryTypeName.
    def exitElementaryTypeName(self, ctx:SolidityParser.ElementaryTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:SolidityParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:SolidityParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#arrayElement.
    def enterArrayElement(self, ctx:SolidityParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by SolidityParser#arrayElement.
    def exitArrayElement(self, ctx:SolidityParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by SolidityParser#numberLiteral.
    def enterNumberLiteral(self, ctx:SolidityParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#numberLiteral.
    def exitNumberLiteral(self, ctx:SolidityParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#decimalNumber.
    def enterDecimalNumber(self, ctx:SolidityParser.DecimalNumberContext):
        pass

    # Exit a parse tree produced by SolidityParser#decimalNumber.
    def exitDecimalNumber(self, ctx:SolidityParser.DecimalNumberContext):
        pass


    # Enter a parse tree produced by SolidityParser#versionLiteral.
    def enterVersionLiteral(self, ctx:SolidityParser.VersionLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#versionLiteral.
    def exitVersionLiteral(self, ctx:SolidityParser.VersionLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SolidityParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SolidityParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#numberUnit.
    def enterNumberUnit(self, ctx:SolidityParser.NumberUnitContext):
        pass

    # Exit a parse tree produced by SolidityParser#numberUnit.
    def exitNumberUnit(self, ctx:SolidityParser.NumberUnitContext):
        pass


    # Enter a parse tree produced by SolidityParser#hexNumber.
    def enterHexNumber(self, ctx:SolidityParser.HexNumberContext):
        pass

    # Exit a parse tree produced by SolidityParser#hexNumber.
    def exitHexNumber(self, ctx:SolidityParser.HexNumberContext):
        pass


    # Enter a parse tree produced by SolidityParser#hexLiteral.
    def enterHexLiteral(self, ctx:SolidityParser.HexLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#hexLiteral.
    def exitHexLiteral(self, ctx:SolidityParser.HexLiteralContext):
        pass


    # Enter a parse tree produced by SolidityParser#stringLiteral.
    def enterStringLiteral(self, ctx:SolidityParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SolidityParser#stringLiteral.
    def exitStringLiteral(self, ctx:SolidityParser.StringLiteralContext):
        pass



del SolidityParser