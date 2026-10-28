odoo.define('stock_picking_import_docs.FieldImportDocPreview', function (require) {
    'use strict';

    var fieldRegistry = require('web.field_registry');
    var FieldBinaryFile = require('web.basic_fields').FieldBinaryFile;

    /**
     * Binary file widget that previews the document in a new tab instead
     * of downloading it, and shows a PDF icon in readonly mode.
     */
    var FieldImportDocPreview = FieldBinaryFile.extend({
        /**
         * Open the document inline (new tab) instead of downloading it.
         * The /web/content route serves the file with an inline
         * Content-Disposition, so the browser renders the PDF full screen.
         *
         * @override
         */
        on_save_as: function (ev) {
            ev.stopPropagation();
            if (!this.value) {
                return;
            }
            var url;
            if (this.res_id) {
                url = '/web/content?' + $.param({
                    model: this.model,
                    field: this.name,
                    id: this.res_id,
                });
            } else {
                var binData = atob(this.value);
                var bytes = new Uint8Array(binData.length);
                for (var i = 0; i < binData.length; i++) {
                    bytes[i] = binData.charCodeAt(i);
                }
                url = URL.createObjectURL(
                    new Blob([bytes], {type: 'application/pdf'}));
            }
            window.open(url, '_blank');
        },

        /**
         * Show a PDF icon instead of the download icon.
         *
         * @override
         */
        _renderReadonly: function () {
            var visible = !!(this.value && this.res_id);
            this.$el.empty().css('cursor', 'not-allowed');
            this.do_toggle(visible);
            if (visible) {
                this.$el.css('cursor', 'pointer')
                        .text(this.filename_value || '')
                        .prepend($('<span class="fa fa-file-pdf-o"/>'), ' ');
            }
        },
    });

    fieldRegistry.add('import_doc_preview', FieldImportDocPreview);

    return FieldImportDocPreview;
});
