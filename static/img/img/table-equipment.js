"use strict";
!function($) {
    $.fn.mdbEditor = function() {
        return this.map(function(i, e) {
            var $selectedRow = void 0, $selectedTable = $(e), $selectedTableId = $selectedTable.closest(".wrapper-modal-editor").find("table").attr("id"), $selectedTableSharp = $("#" + $selectedTableId), $table = $("#" + $selectedTableId).DataTable(), $wrapperModalEditor = $selectedTableSharp.closest(".wrapper-modal-editor"), $createShowP = $wrapperModalEditor.find(".createShowP"), $buttonEdit = $wrapperModalEditor.find(".buttonEdit"), $buttonDelete = $wrapperModalEditor.find(".buttonDelete"), $buttonAddFormWrapper = $wrapperModalEditor.find(".buttonAddFormWrapper"), $buttonEditWrapper = $wrapperModalEditor.find(".buttonEditWrapper"), $editInsideWrapper = $wrapperModalEditor.find(".editInsideWrapper"), $deleteButtonsWrapper = $wrapperModalEditor.find(".deleteButtonsWrapper"), editInside = $wrapperModalEditor.find(".editInside"), trColorSelected = ".tr-color-selected", addNewRows = function addNewRows() {
                for (var $newRow = [], _i = 0; _i < $wrapperModalEditor.find(".addNewInputs input").length; _i++)
                    $newRow.push($wrapperModalEditor.find(".addNewInputs input").eq(_i).val());
                $table.row.add($newRow).draw()
            }, btnToModalAdd = function btnToModalAdd(e) {
                var $etargetClosetWrapper = $(e.target).closest(".wrapper-modal-editor");
                $etargetClosetWrapper.find(".addNewInputs input").val(""),
                $etargetClosetWrapper.find(".addNewInputs label").removeClass("active"),
                $etargetClosetWrapper.find(".addNewInputs input").removeClass("valid")
            }, addColorToTr = function addColorToTr(e) {
                return $(e.target).parent().not("thead tr").not("tfoot tr").toggleClass("tr-color-selected").siblings().removeClass("tr-color-selected")
            }, toggleDisabledToButtons = function toggleDisabledToButtons(e) {
                $selectedRow = $(e.target).parent(),
                $(e.target).parent().not("thead tr").not("tfoot tr").hasClass("tr-color-selected") ? ($buttonEdit.prop("disabled", !1),
                $buttonDelete.prop("disabled", !1),
                $createShowP.html("1 row selected")) : $("tr").hasClass("tr-color-selected") || ($buttonEdit.prop("disabled", !0),
                $buttonDelete.prop("disabled", !0),
                $createShowP.html("0 row selected"))
            }, buttonEditInput = function buttonEditInput(e) {
                for (var _i2 = 0; _i2 < $(e.target).closest(".wrapper-modal-editor").find("thead tr").children().length; _i2++)
                    $table.row($wrapperModalEditor.find(".modalEditClass input").eq(_i2).val($table.cell($selectedRow, _i2).data()))
            }, addClassActiveToLabel = function addClassActiveToLabel() {
                return $(".modalEditClass label").addClass("active")
            }, buttonEditInside = function buttonEditInside(e) {
                for (var _i3 = 0; _i3 < $(e.target).closest(".wrapper-modal-editor").find("thead tr").children().length; _i3++)
                    $table.cell($(trColorSelected).find("td").eq(_i3)).data($wrapperModalEditor.find(".modalEditClass input").eq(_i3).val())
            }, removeColorClassFromTr = function removeColorClassFromTr() {
                return $selectedTable.find(".tr-color-selected").removeClass("tr-color-selected")
            }, disabledButtons = function disabledButtons() {
                $buttonEdit.prop("disabled", !0),
                $buttonDelete.prop("disabled", !0)
            }, selectedZeroRowsNews = function selectedZeroRowsNews() {
                $createShowP.html("0 row selected"),
                $table.draw(!1)
            }, buttonDeleteYes = function buttonDeleteYes() {
                $buttonEdit.prop("disabled", !0),
                $buttonDelete.prop("disabled", !0),
                $createShowP.html("0 row selected"),
                $table.row($(trColorSelected)).remove().draw()
            }, bindEvents;
            (function bindEvents() {
                $buttonAddFormWrapper.on("click", ".buttonAdd", addNewRows),
                $selectedTableSharp.on("click", "tr", addColorToTr),
                $selectedTableSharp.on("click", "tr", toggleDisabledToButtons),
                $buttonEditWrapper.on("click", $buttonEdit, buttonEditInput),
                $buttonEditWrapper.on("click", $buttonEdit, addClassActiveToLabel),
                $deleteButtonsWrapper.on("click", ".btnYesClass", buttonDeleteYes),
                $editInsideWrapper.on("click", editInside, buttonEditInside),
                $editInsideWrapper.on("click", editInside, removeColorClassFromTr),
                $editInsideWrapper.on("click", editInside, disabledButtons),
                $editInsideWrapper.on("click", editInside, selectedZeroRowsNews),
                $(".wrapperToBtnModalAdd").on("click", ".btnToModalAdd", btnToModalAdd)
            }
            )()
        })
    }
    ,
    $.fn.mdbEditorRow = function() {
        var _this = this;
        return this.map(function(i, e) {
            var editRow = ".editRow", saveRow = ".saveRow", tdLast = "td:last", $removeColumns = $(".removeColumns"), $this = $(e), $tableId = $this.closest(".wrapper-row-editor").find("table").attr("id"), $sharpTableId, $tableData = $("#" + $tableId).DataTable(), addNewColumn = ".addNewColumn", $buttonWrapper = $(".buttonWrapper"), $closeByClick = $(".closeByClick"), $showForm = $(".showForm"), addNewTr = function addNewTr(e) {
                $(document).find($(e.target).parents().eq(1)).map(function(i, event) {
                    $(event).find("tr").map(function(i, ev) {
                        $(ev).find(tdLast).not(".td-editor").after('<td class="text-center td-editor" style="border-top: 1px solid #dee2e6; border-bottom:1px solid #dee2e6"><button class="btn btn-sm editRow btn-sm btn-teal"><i class="far fa-edit"></i></button></td>')
                    })
                })
            }, removeDisabledButtons = function removeDisabledButtons(e) {
                var $tableId = $(e.target).closest(".wrapper-row-editor").find("table").attr("id")
                  , $findButton = $("#" + $tableId).closest(".wrapper-row-editor").find(".removeColumns");
                1 == $("#" + $tableId).find("td").hasClass("td-editor") ? $findButton.prop("disabled", !1) : $findButton.prop("disabled", !0),
                $("#" + $tableId).closest(".wrapper-row-editor").find("td.td-editor").hasClass("td-editor") || $findButton.prop("disabled", !0)
            }, editRowAndAddClassToTr = function editRowAndAddClassToTr(e) {
                for (var $closestTrTd = $(e.target).closest(".wrapper-row-editor tr").find("td"), $closestTrEdit = $(e.target).closest(".wrapper-row-editor tr").find(editRow), divWrapper = '<div class="d-flex justify-content-center div-to-remove"></div>', editButton = '<td class="text-center td-editor td-yes" style="border:none"><button class="btn btn-sm btn-danger deleteRow" style="cursor:pointer;"><i class="fas fa-trash-alt"></i></b></td>', saveButton = '<td class="text-center td-editor td-yes" style="border:none"><button class="btn btn-sm btn-primary saveRow" style="cursor:pointer;"><i class="fas fa-check"></i></button></td>', _i4 = 0; _i4 < $(e.target).closest(".wrapper-row-editor").find("table thead th").length; _i4++)
                    $closestTrTd.eq(_i4).html('<input type="text" class="val' + _i4 + ' form-control" value="' + $closestTrTd.eq(_i4).text() + '">');
                $closestTrEdit.after($(divWrapper).append(saveButton, editButton)),
                $($("#" + $tableId)).on("click", ".deleteRow", function() {
                    $($("#" + $tableId).closest(".wrapper-row-editor").find(".showForm, .closeByClick").removeClass("d-none"))
                })
            }, clickBtnCBCaddDnone = function clickBtnCBCaddDnone(e) {
                $(e.target).addClass("d-none"),
                $showForm.addClass("d-none")
            }, addDnoneByClickBtns = function addDnoneByClickBtns() {
                $showForm.addClass("d-none"),
                $closeByClick.addClass("d-none")
            }, addColorClassAndPy = function addColorClassAndPy(e) {
                var $closestTr = $(e.target).closest("tr");
                $closestTr.addClass("tr-color-selected"),
                $closestTr.find("td").not(".td-editor").addClass("py-5")
            }, addDisabledButtonsByEditBtn = function addDisabledButtonsByEditBtn(e) {
                $(e.target).prop("disabled", !0),
                $(e.target).closest(".wrapper-row-editor").find($removeColumns).prop("disabled", !0)
            }, saveRowAndRemovePy = function saveRowAndRemovePy(e) {
                for (var $closestTr = $(e.target).closest("tr"), _i5 = 0; _i5 < $(e.target).closest(".wrapper-row-editor").find("table thead th").length; _i5++)
                    $tableData.cell($closestTr.find("td").eq(_i5)).data($closestTr.find(".val" + _i5).val());
                $closestTr.find("td").removeClass("py-5")
            }, removeDisabledColorAdnTdYes = function removeDisabledColorAdnTdYes(e) {
                var $closestTr = $(e.target).closest("tr");
                $closestTr.find(editRow).prop("disabled", !1),
                $closestTr.removeClass("tr-color-selected"),
                $closestTr.find(".td-yes").remove(),
                $tableData.draw(!1),
                $("#" + $(_this).closest(".wrapper-row-editor").find("table").attr("id")).closest(".wrapper-row-editor").find(".removeColumns").prop("disabled", !1)
            }, saveRowClickRemoveDiv = function saveRowClickRemoveDiv() {
                return $(".div-to-remove").remove()
            }, removeColorInTrAndDraw = function removeColorInTrAndDraw(e) {
                var $tableId = $(e.target).closest(".wrapper-row-editor").find("table").attr("id");
                $tableData.row($("#" + $tableId).find("tr.tr-color-selected")).remove().draw(!1),
                $("#" + $tableId + " tr").hasClass("td-editor") ? $("#" + $tableId).closest(".wrapper-row-editor").find($removeColumns).prop("disabled", !0) : $("#" + $tableId).closest(".wrapper-row-editor").find($removeColumns).prop("disabled", !1)
            }, removeSelectedButtonsFromRow = function removeSelectedButtonsFromRow(e) {
                var $tableId = $(e.target).closest(".wrapper-row-editor").find("table").attr("id");
                !0 == !$("#" + $tableId).hasClass("td-editor") && $(e.target).closest(".wrapper-row-editor").find(".removeColumns").attr("disabled", !0),
                !1 === $("#" + $tableId).hasClass("td-editor") && !1 === $("#" + $tableId + " tr").hasClass("tr-color-selected") && ($("#" + $tableId).find(".td-editor").remove(),
                $("#" + $tableId).find(".tr-color-selected").remove(),
                $tableData.draw(!1))
            }, bindEvents;
            (function bindEvents() {
                $buttonWrapper.on("click", addNewColumn, addNewTr),
                $buttonWrapper.on("click", addNewColumn, removeDisabledButtons),
                $this.on("click", editRow, editRowAndAddClassToTr),
                $this.on("click", editRow, addColorClassAndPy),
                $this.on("click", editRow, addDisabledButtonsByEditBtn),
                $this.on("click", saveRow, saveRowAndRemovePy),
                $this.on("click", saveRow, removeDisabledColorAdnTdYes),
                $this.on("click", saveRow, saveRowClickRemoveDiv),
                $(".buttonYesNoWrapper").on("click", ".btnYes", removeColorInTrAndDraw),
                $buttonWrapper.on("click", ".removeColumns", removeSelectedButtonsFromRow),
                $showForm.on("click", ".btnYes, .button-x, .btnNo", addDnoneByClickBtns),
                $closeByClick.on("click", clickBtnCBCaddDnone)
            }
            )(),
            !0 === $closeByClick.hasClass("d-none") && $(document).keyup(function(e) {
                27 === e.keyCode && ($closeByClick.addClass("d-none"),
                $showForm.addClass("d-none"))
            })
        })
    }
    ,
    $(".buttonWrapper").on("click", ".addNewRows", function(e) {
        for (var $newRow = [], i = 0; i < $(e.target).closest(".wrapper-row-editor").find("table thead th").length; i++)
            $newRow.push($(e.target).val());
        $("#" + $(e.target).closest(".wrapper-row-editor").find("table").attr("id")).DataTable().row.add($newRow).draw()
    })
}(jQuery);
$(document).ready(function() {
    $('#editibleTable').mdbEditor();
    $('.dataTables_length').addClass('bs-select');
});

