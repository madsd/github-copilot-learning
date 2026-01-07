/**
 * Translated C# Code
 * ===================
 * Complete this translation using Copilot.
 *
 * EXERCISE:
 * 1. Open original_python.py
 * 2. Select sections of code
 * 3. Use Copilot Chat: "Convert this to C#"
 * 4. Paste the translations here
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;

namespace CodeTranslation
{
    // =========================================================================
    // RECORDS (C# 9+ equivalent of Python dataclasses)
    // =========================================================================

    // TODO: Translate User as a C# record


    // TODO: Translate Product as a C# record


    // TODO: Translate Order as a C# record


    // =========================================================================
    // UTILITY FUNCTIONS (Static class)
    // =========================================================================

    public static class Utilities
    {
        // TODO: Translate FormatCurrency method


        // TODO: Translate CalculateDiscount method


        // TODO: Translate ParseDate method

    }

    // =========================================================================
    // LIST/ARRAY OPERATIONS (Using LINQ)
    // =========================================================================

    public static class ProductOperations
    {
        // TODO: Translate FilterActiveUsers using LINQ


        // TODO: Translate GroupByCategory using LINQ


        // TODO: Translate FindTopProducts using LINQ


        // TODO: Translate SearchProducts using LINQ

    }

    // =========================================================================
    // BUSINESS LOGIC
    // =========================================================================

    // TODO: Translate ShoppingCart class


    // =========================================================================
    // ASYNC OPERATIONS (Using async/await)
    // =========================================================================

    public static class OrderOperations
    {
        // TODO: Translate FetchUserOrders as async Task


        // TODO: Translate CalculateUserStatistics as async Task

    }

    // =========================================================================
    // JSON SERIALIZATION (Using System.Text.Json)
    // =========================================================================

    public static class Serialization
    {
        // TODO: Translate UserToJson method


        // TODO: Translate UserFromJson method

    }

    // =========================================================================
    // KEY DIFFERENCES FROM PYTHON
    // =========================================================================
    /*
     * Notes on translating Python to C#:
     * 
     * 1. Use PascalCase for methods and properties
     * 2. Use records (C# 9+) for immutable data classes
     * 3. Use LINQ for collection operations
     * 4. Nullable types use '?' suffix (string?, int?)
     * 5. Dict[K, V] becomes Dictionary<K, V>
     * 6. List[T] becomes List<T> or IList<T>
     * 7. Tuple[A, B] becomes (A, B) or Tuple<A, B>
     * 8. async def becomes async Task<T>
     * 9. Exception handling uses try/catch
     * 10. String interpolation uses $ prefix: $"Hello {name}"
     */
}
