package com.ianhanniballake.contractiontimer.ui

import android.app.Dialog
import android.os.Bundle
import androidx.appcompat.app.AlertDialog
import androidx.fragment.app.DialogFragment

class DonateDialogFragment : DialogFragment() {
    override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
        return AlertDialog.Builder(requireContext())
            .setTitle("PartoFácil")
            .setMessage("Obrigado por usar o PartoFácil!\n\nEste aplicativo foi desenvolvido para auxiliar você de forma simples e segura durante o monitoramento de suas contrações.")
            .setPositiveButton("OK") { dialog, _ -> dialog.dismiss() }
            .create()
    }
}
