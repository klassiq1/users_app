document.addEventListener("DOMContentLoaded", function() {
    const tickets = [
        { id: 101, title: "Bug in login page", status: "Open", priority: "High", created: "2025-03-04" },
        { id: 102, title: "Feature request: Dark mode", status: "In Progress", priority: "Medium", created: "2025-03-03" },
        { id: 103, title: "Database error on checkout", status: "Closed", priority: "High", created: "2025-03-02" },
        { id: 104, title: "Update email notifications", status: "Open", priority: "Low", created: "2025-03-01" }
    ];

    function updateDashboard() {
        let total = tickets.length;
        let open = tickets.filter(t => t.status === "Open").length;
        let inProgress = tickets.filter(t => t.status === "In Progress").length;
        let closed = tickets.filter(t => t.status === "Closed").length;

        document.getElementById("total-tickets").textContent = total;
        document.getElementById("open-tickets").textContent = open;
        document.getElementById("in-progress-tickets").textContent = inProgress;
        document.getElementById("closed-tickets").textContent = closed;

        let ticketTable = document.getElementById("ticket-table");
        ticketTable.innerHTML = "";
        tickets.forEach(ticket => {
            let row = `<tr>
                <td>${ticket.id}</td>
                <td>${ticket.title}</td>
                <td>${ticket.status}</td>
                <td>${ticket.priority}</td>
                <td>${ticket.created}</td>
            </tr>`;
            ticketTable.innerHTML += row;
        });
    }

    updateDashboard();
});
